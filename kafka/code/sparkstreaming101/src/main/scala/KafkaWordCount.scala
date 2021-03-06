/**
  * Created by abgoswam on 12/6/16.
  */

import java.util.HashMap

import org.apache.kafka.clients.producer.{KafkaProducer, ProducerConfig, ProducerRecord}
import org.apache.spark.SparkConf
import org.apache.spark.streaming._
import org.apache.spark.streaming.kafka._

object KafkaWordCount {
  def main(args: Array[String]) {
//    if (args.length < 4) {
//      System.err.println("Usage: KafkaWordCount <zkQuorum><group> <topics> <numThreads>")
//      System.exit(1)
//    }

//    val Array(zkQuorum, group, topics, numThreads) = ("localhost:2181", "testgrp",  "test", "2")

    val sparkConf = new SparkConf().setAppName("KafkaWordCount").setMaster("local[*]")
    val ssc = new StreamingContext(sparkConf, Seconds(10))
//    ssc.checkpoint("checkpoint")

//    val topicMap = topics.split(",").map((_, numThreads.toInt)).toMap
    val topicMap = "test".split(",").map((_, "5".toInt)).toMap
    val lines = KafkaUtils.createStream(ssc, "localhost:2181", "testgrp", topicMap).map(_._2)
    val words = lines.flatMap(_.split(" "))
//    val wordCounts = words.map(x => (x, 1L))
//      .reduceByKeyAndWindow(_ + _, _ - _, Seconds(30), Seconds(10), 2)

    val wordCounts = words.map(x => (x, 1)).reduceByKey(_ + _)
    wordCounts.print()

    ssc.start()
    ssc.awaitTermination()
  }
}
