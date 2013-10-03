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

public class SelfJoin {

    static private final int NUM_ATTRS = 2;
    static private final int LEFT_ATTR = 1;
    static private final int RIGHT_ATTR = 0;
    static private final int LEFT = 0;
    static private final int RIGHT = 1;

    public static class TupleWritable implements Writable {
      private int side;
      private int[] attrValues;

      public int getSide() {
        return side;
      }

      public int[] getAttrValues() {
        return attrValues;
      }

      public TupleWritable() {
        side = -1;
        attrValues = null; 
      }
     
      public TupleWritable(int side, int[] attrValues) {
        this.side = side;
        this.attrValues = attrValues;
      }
 
      public void write(DataOutput out) throws IOException {
        out.writeInt(side);
        out.writeInt(attrValues.length);
        for (int i = 0; i < attrValues.length; i++) {
          out.writeInt(attrValues[i]);
        }
      }
       
      public void readFields(DataInput in) throws IOException {
        side = in.readInt();
        int numAttrs = in.readInt();
        attrValues = new int[numAttrs];
        for (int i = 0; i < numAttrs; i++) {
          attrValues[i] = in.readInt();
        }
      }
       
      public static TupleWritable read(DataInput in) throws IOException {
        TupleWritable w = new TupleWritable();
        w.readFields(in);
        return w;
      }

      public static TupleWritable concat(final TupleWritable t1, final TupleWritable t2) {
        int[] newAttrs = new int[t1.attrValues.length + t2.attrValues.length];
        System.arraycopy(t1.attrValues, 0, newAttrs, 0, t1.attrValues.length);
        System.arraycopy(t2.attrValues, 0, newAttrs, t1.attrValues.length, t2.attrValues.length);
        TupleWritable newT = new TupleWritable(RIGHT, newAttrs);
        return newT;
      }
    }

    public static class Map extends MapReduceBase implements Mapper<LongWritable, Text, IntWritable, TupleWritable> {
      private Text word = new Text();


      public void map(LongWritable key, Text value, OutputCollector<IntWritable, TupleWritable> output, Reporter reporter) throws IOException {
        String line = value.toString();
        StringTokenizer tokenizer = new StringTokenizer(line);
        int attrs[] = new int[NUM_ATTRS];
        for (int i = 0; i < NUM_ATTRS; i++) {
          word.set(tokenizer.nextToken());
          attrs[i] = Integer.parseInt(word.toString());
        }
        output.collect(new IntWritable(attrs[LEFT_ATTR]), new TupleWritable(LEFT, attrs));
        output.collect(new IntWritable(attrs[RIGHT_ATTR]), new TupleWritable(RIGHT, attrs));
      }
    }

    public static class Reduce extends MapReduceBase implements Reducer<IntWritable, TupleWritable, IntWritable, TupleWritable> {

      private void probe(IntWritable key, final TupleWritable t, final List<TupleWritable> l1, final List<TupleWritable> l2, final OutputCollector<IntWritable, TupleWritable> output) throws IOException {
        l1.add(t);
        for (TupleWritable ti : l2) {
          output.collect(key, TupleWritable.concat(t, ti));        
        }
      }

      public void reduce(IntWritable key, Iterator<TupleWritable> values, OutputCollector<IntWritable, TupleWritable> output, Reporter reporter) throws IOException {
        List<TupleWritable> left = new ArrayList<TupleWritable>();
        List<TupleWritable> right = new ArrayList<TupleWritable>();
      
        while (values.hasNext()) {
          final TupleWritable t = values.next();
          if (t.getSide() == LEFT) {
            probe(key, t, left, right, output);
          }
          else {
            probe(key, t, right, left, output);
          }
        }
      }
    }

    public static void main(String[] args) throws Exception {
      JobConf conf = new JobConf(SelfJoin.class);
      conf.setJobName("wordcount");

      conf.setOutputKeyClass(IntWritable.class);
      conf.setOutputValueClass(TupleWritable.class);

      conf.setMapperClass(Map.class);
      conf.setReducerClass(Reduce.class);

      conf.setInputFormat(TextInputFormat.class);
      conf.setOutputFormat(TextOutputFormat.class);

      FileInputFormat.setInputPaths(conf, new Path(args[0]));
      FileOutputFormat.setOutputPath(conf, new Path(args[1]));

      JobClient.runJob(conf);
    }
}
