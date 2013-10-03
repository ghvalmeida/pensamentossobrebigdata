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

public class SelfJoinForTriangles {

    static private final int NUM_ATTRS = 2;
    static private final int LEFT_ATTR = 1;
    static private final int RIGHT_ATTR = 0;
    static private final int LEFT = 0;
    static private final int RIGHT = 1;

    public static class IntArrayWritable extends ArrayWritable {
      public IntArrayWritable() {
        super(IntWritable.class);
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

    public static class Map extends MapReduceBase implements Mapper<LongWritable, Text, IntWritable, IntArrayWritable> {
      private Text word = new Text();


      public void map(LongWritable key, Text value, OutputCollector<IntWritable, IntArrayWritable> output, Reporter reporter) throws IOException {
        String line = value.toString();
        StringTokenizer tokenizer = new StringTokenizer(line);
        IntWritable[] leftVals = new IntWritable[NUM_ATTRS+1];
        leftVals[0] = new IntWritable(LEFT);
        for (int i = 0; i < NUM_ATTRS; i++) {
          word.set(tokenizer.nextToken());
          int attr = Integer.parseInt(word.toString());
          leftVals[i+1] = new IntWritable(attr);
        }
        IntArrayWritable leftIntArr = new IntArrayWritable();
        leftIntArr.set(leftVals);
        output.collect(leftVals[LEFT_ATTR+1], leftIntArr);

        IntWritable[] rightVals = new IntWritable[NUM_ATTRS+1];
        System.arraycopy(leftVals, 0, rightVals, 0, leftVals.length);
        rightVals[0] = new IntWritable(RIGHT);
        IntArrayWritable rightIntArr = new IntArrayWritable();
        rightIntArr.set(rightVals);
        output.collect(rightVals[RIGHT_ATTR+1], rightIntArr);
      }
    }

    public static class Reduce extends MapReduceBase implements Reducer<IntWritable, IntArrayWritable, IntWritable, IntArrayWritable> {

      private void probe(IntWritable key, IntArrayWritable t, List<IntArrayWritable> l1, List<IntArrayWritable> l2, OutputCollector<IntWritable, IntArrayWritable> output) throws IOException {
        l1.add(t);
        for (IntArrayWritable ti : l2) {
          output.collect(key, IntArrayWritable.concat(t, ti));        
        }
      }

      public void reduce(IntWritable key, Iterator<IntArrayWritable> values, OutputCollector<IntWritable, IntArrayWritable> output, Reporter reporter) throws IOException {
        ArrayList<IntArrayWritable> left = new ArrayList<IntArrayWritable>();
        ArrayList<IntArrayWritable> right = new ArrayList<IntArrayWritable>();
      
        while (values.hasNext()) {
          IntArrayWritable t = values.next();
          IntArrayWritable t1 = IntArrayWritable.copy(t);
          if (((IntWritable)t1.get()[0]).get() == LEFT) {
            output.collect(key, t1);
            probe(key, t1, left, right, output);
            //left.add(t1);
          }
          else {
            //output.collect(key, t1);
            probe(key, t1, right, left, output);
            //right.add(t1);
          }
        }
        //for (int i = 0; i < left.size(); i++) {
        //  output.collect(key, left.get(i));
        //}
        //for (int i = 0; i < right.size(); i++) {
        //  output.collect(key, right.get(i));
        //}
      }
    }

    public static void main(String[] args) throws Exception {
      JobConf conf = new JobConf(SelfJoinForTriangles.class);
      conf.setJobName("wordcount");

      conf.setOutputKeyClass(IntWritable.class);
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
