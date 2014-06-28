
source /usr/local/hadoop-1.2.1/conf/hadoop-env.sh
export PATH=$PATH:/usr/local/hadoop-1.2.1/bin
export PATH=$PATH:/usr/local/pig-0.11.1/bin

hadoop fs -rmr /input/twitter
hadoop fs -rmr /output/twitter

hadoop fs -put /Users/valmeida/code/triangles/twitter.small.csv /input/twitter

javac -classpath /usr/local/hadoop-1.2.1/hadoop-core-1.2.1.jar -d class SelfJoinForTriangles.java
javac -classpath /usr/local/hadoop-1.2.1/hadoop-core-1.2.1.jar -d class Triangles.java

jar -cvf triangles.jar -C class .


hadoop jar triangles.jar org.myorg.SelfJoinForTriangles /input/twitter /output/twitter/triangles/input

hadoop jar triangles.jar org.myorg.Triangles /output/twitter/triangles/input/part* /output/twitter/triangles/output

hadoop fs -cat /output/twitter/triangles/output/part* | wc -l

