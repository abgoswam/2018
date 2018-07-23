## Kafka.

> This post is part of the series on [Getting Started and Beyond](https://github.com/abgoswam/getting-started-and-beyond)


### Command line tools

#### zookeeper-server-start.sh
~~~
> bin/zookeeper-server-start.sh config/zookeeper.properties
~~~

#### kafka-server-start.sh
~~~
> bin/kafka-server-start.sh config/server.properties
~~~

#### kafka-topics.sh

- Create Topic

~~~
> bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic test
~~~

- List Topic

~~~
> bin/kafka-topics.sh --list --zookeeper localhost:2181
~~~

- Describe Topic

~~~
> bin/kafka-topics.sh --describe --zookeeper localhost:2181 --topic test
~~~

#### kafka-console-producer.sh

~~~
> bin/kafka-console-producer.sh --broker-list localhost:9092 --topic test
This is a message
This is another message
~~~

#### kafka-console-consumer.sh

~~~
> bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic test --from-beginning
This is a message
This is another message
~~~

#### connect-standalone.sh

~~~
> bin/connect-standalone.sh config/connect-standalone.properties config/connect-file-source.properties config/connect-file-sink.properties
~~~

### Config Files.
- config/zookeeper.properties
- config/server.properties
- config/connect-standalone.properties
- config/connect-file-source.properties
- config/connect-file-sink.properties

### References:

- [I ❤ Logs: Apache Kafka and Real-time Data Integration](https://www.safaribooksonline.com/library/view/i-logs/9781491908310/)
- [Going Real Time. Data Collection and Stream Processing with Apache Kafka](https://www.safaribooksonline.com/library/view/large-scale-real-time-stream/9781491931028/part01.html)
- [Distributed Stream Processing with Apache Kafka](https://www.safaribooksonline.com/library/view/the-real-time-video/9781491965818/video247133.html)
- [Benchmarking Apache Kafka: 2 Million Writes Per Second (On Three Cheap Machines)](https://engineering.linkedin.com/kafka/benchmarking-apache-kafka-2-million-writes-second-three-cheap-machines)
- [Getting Started with Apache Kafka for the Baffled, Part 1](http://www.shayne.me/blog/2015/2015-06-16-everything-about-kafka-part-1/)
- [The Log: What every software engineer should know about real-time data's unifying abstraction](https://engineering.linkedin.com/distributed-systems/log-what-every-software-engineer-should-know-about-real-time-datas-unifying)
- [1.3 Quickstart](http://kafka.apache.org/documentation.html#quickstart)
- [Introducing the Kafka Consumer](https://www.confluent.io/blog/tutorial-getting-started-with-the-new-apache-kafka-0-9-consumer-client/)
- [Tutorialspoint](https://www.tutorialspoint.com/apache_kafka/index.htm)
    - I liked the into to Kafka that was there in Tutorials Point
