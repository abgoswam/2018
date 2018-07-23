/**
  * Created by abgoswam on 12/8/16.
  */

import org.apache.spark._
import org.apache.spark.streaming._

object HelloStreaming {
  val conf = new SparkConf().setAppName("HelloStreaming").setMaster("local[*]")
  val ssc = new StreamingContext(conf, Seconds(1))


}
