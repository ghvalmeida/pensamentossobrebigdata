package org.myorg;

import java.io.IOException;
import java.io.DataInput;
import java.io.DataOutput;
import java.util.*;

import org.apache.hadoop.fs.Path;
import org.apache.hadoop.conf.*;
import org.apache.hadoop.io.*;
import org.apache.hadoop.mapred.*;
import org.apache.hadoop.util.*;

public class Triangles {

    static private final int NUM_ATTRS = 2;
    static private final int[] LEFT_ATTRS = {1,0};
    static private final int[] RIGHT_ATTRS = {0,3};
    static private final int MIDDLE = 1;
    static private final int LEFT = 0;
    static private final int RIGHT = 1;

    public static class IntArrayWritable extends ArrayWritable implements WritableComparable<IntArrayWritable> {
      public IntArrayWritable() {
        super(IntWritable.class);
      }

      @Override
      public int compareTo(IntArrayWritable other) {
        for (int i = 0; i < get().length; i++) {
          if (((IntWritable)get()[i]).compareTo((IntWritable)other.get()[i]) != 0) {
            return ((IntWritable)get()[i]).compareTo((IntWritable)other.get()[i]);
          }
        }
        return 0;
      }

      @Override
      public int hashCode() {
        return Arrays.hashCode(get());
      }
          
      @Override
      public String toString() {
        StringBuilder sb = new StringBuilder();
        for (Writable w : get()) {
          sb.append(w.toString()).append(" ");
        }
        return sb.toString();
      }
 
      public static IntArrayWritable copy(IntArrayWritable t) {
        IntArrayWritable newT = new IntArrayWritable();
        IntWritable[] attrs = new IntWritable[t.get().length];
        System.arraycopy(t.get(), 0, attrs, 0, t.get().length);
        newT.set(attrs);
        return newT;
      }

      public static IntArrayWritable concat(IntArrayWritable t1, IntArrayWritable t2) {
        IntArrayWritable l, r;
        if ( ((IntWritable)t1.get()[0]).get() == LEFT ) {
          l = t1;
          r = t2;
        }
        else {
          l = t2;
          r = t1;
        }

        IntWritable[] newAttrs = new IntWritable[1 + l.get().length-1 + r.get().length-1];
        newAttrs[0] = new IntWritable(RIGHT);
        for (int i = 1; i < l.get().length; i++ ) {
          newAttrs[i] = (IntWritable)l.get()[i];
        }
        for (int i = 1; i < r.get().length; i++) {
          newAttrs[l.get().length-1+i] = (IntWritable)r.get()[i];
        }
        IntArrayWritable newT = new IntArrayWritable();
        newT.set(newAttrs);
        return newT;
      }

    }

    public static class Map extends MapReduceBase implements Mapper<LongWritable, Text, IntArrayWritable, IntArrayWritable> {
      private Text word = new Text();


      public void map(LongWritable key, Text value, OutputCollector<IntArrayWritable, IntArrayWritable> output, Reporter reporter) throws IOException {
        String line = value.toString();
        StringTokenizer tokenizer = new StringTokenizer(line);
        
        // ignore the first value. last job's reduce key.
        word.set(tokenizer.nextToken());

        // second value is the side: LEFT or RIGHT
        word.set(tokenizer.nextToken());
        int side = Integer.parseInt(word.toString());

        int size = -1;
        int[] attrs = null;
        if (side == LEFT) {
          size = NUM_ATTRS;
          attrs = LEFT_ATTRS;
        }
        else {
          size = 2 * NUM_ATTRS;
          attrs = RIGHT_ATTRS; 
        }

        IntWritable[] vals = new IntWritable[size+1];
        vals[0] = new IntWritable(side);

        // the rest are the attributes
        for (int i = 0; i < size; i++) {
          word.set(tokenizer.nextToken());
          int attr = Integer.parseInt(word.toString());
          vals[i+1] = new IntWritable(attr);
        }
        IntArrayWritable intArr = new IntArrayWritable();
        intArr.set(vals);

        IntArrayWritable keyArr = new IntArrayWritable();
        IntWritable[] keys = new IntWritable[attrs.length];
        for (int i = 0; i < attrs.length; i++) {
          keys[i] = vals[attrs[i]+1];
        }
        keyArr.set(keys);
        output.collect(keyArr, intArr);
      }
    }

    public static class Reduce extends MapReduceBase implements Reducer<IntArrayWritable, IntArrayWritable, IntArrayWritable, IntArrayWritable> {

      private void probe(IntArrayWritable key, IntArrayWritable t, List<IntArrayWritable> l1, List<IntArrayWritable> l2, OutputCollector<IntArrayWritable, IntArrayWritable> output) throws IOException {
        l1.add(t);
        for (IntArrayWritable ti : l2) {
          IntArrayWritable newT = IntArrayWritable.concat(t, ti);
          int u = ((IntWritable)newT.get()[LEFT_ATTRS[0]+1]).get();
          int v = ((IntWritable)newT.get()[LEFT_ATTRS[1]+1]).get();
          int w = ((IntWritable)newT.get()[MIDDLE+NUM_ATTRS+1]).get();
          if (u < v && v < w || u > v && v > w) {
            output.collect(key, newT);        
          }
        }
      }

      public void reduce(IntArrayWritable key, Iterator<IntArrayWritable> values, OutputCollector<IntArrayWritable, IntArrayWritable> output, Reporter reporter) throws IOException {
        ArrayList<IntArrayWritable> left = new ArrayList<IntArrayWritable>();
        ArrayList<IntArrayWritable> right = new ArrayList<IntArrayWritable>();
      
        while (values.hasNext()) {
          IntArrayWritable t = values.next();
          IntArrayWritable t1 = IntArrayWritable.copy(t);
          if (((IntWritable)t1.get()[0]).get() == LEFT) {
            probe(key, t1, left, right, output);
          }
          else {
            probe(key, t1, right, left, output);
          }
        }
      }
    }

    public static void main(String[] args) throws Exception {
      JobConf conf = new JobConf(Triangles.class);
      conf.setJobName("wordcount");

      conf.setOutputKeyClass(IntArrayWritable.class);
      conf.setOutputValueClass(IntArrayWritable.class);

      conf.setMapperClass(Map.class);
      conf.setReducerClass(Reduce.class);

      conf.setInputFormat(TextInputFormat.class);
      conf.setOutputFormat(TextOutputFormat.class);

      FileInputFormat.setInputPaths(conf, new Path(args[0]));
      FileOutputFormat.setOutputPath(conf, new Path(args[1]));

      JobClient.runJob(conf);
    }
}
