## SBT.

I started doing Martin Odersky's course [Functional Programming Principles in Scala](https://www.coursera.org/learn/progfun1) and one of the the very first thing that you will have to pick up on is SBT

> This post is part of the series on [Getting Started and Beyond](https://github.com/abgoswam/getting-started-and-beyond)


## Topics Covered

- [Getting Started](#getting-started)
	- [What is SBT?](#what-is-sbt)
	- [Installation](#installation)
- [Going Beyond](#going-beyond)
	- [SBT Tasks](#sbt-tasks)
	- [SBT Modes](#sbt-modes)
	- [Hello World using Scala + SBT](#hello-world-using-scala-sbt)
	- [build.sbt](#buildsbt)
	- [Synchronizing SBT](#synchronizing-sbt)
	- [Dependencies](#dependencies)
	- [Running Tests](#running-tests)
- [Misc Tips](#misc-tips)
- [References](#references)

## Getting Started

The official [Getting Started with SBT](http://www.scala-sbt.org/0.13/docs/Getting-Started.html) is a good place to get started with SBT. However, it has a lot of advanced stuff. So let's take things gradually here.

### What is SBT?

SBT is an open source build tool for Scala and Java projects, similar to Java's Maven or Ant.

The features I have noticed so far are:

1. It has a defined project layout.
    - The Project layout is similar to what [Maven](https://maven.apache.org/) has
2. It has Scala REPL integration
    - What I mean here is that you will be able to reach the scala console from inside SBT
3. Native support for compiling Scala code and integrating with many Scala test frameworks

### Installation

There is a [Tools Setup](https://www.coursera.org/learn/progfun1/supplement/BNOBK/tools-setup-please-read) guide in Week1 of the course that had good instructions about installing SBT.

To verify the installation try running `sbt about`.

~~~
$ sbt about
[info] Set current project to raw (in build file:/F:/Complex/Raw/)
[info] This is sbt 0.13.12
[info] The current project is {file:/F:/Complex/Raw/}raw 0.1-SNAPSHOT
[info] The current project is built against Scala 2.10.6
[info] Available Plugins: sbt.plugins.IvyPlugin, sbt.plugins.JvmPlugin, sbt.plugins.CorePlugin, sbt.plugins.JUnitXmlReportPlugin
[info] sbt, sbt plugins, and build definitions are using Scala 2.10.6
~~~

In my case, I am running SBT on a Windows 10 PC. As you can see above the version of SBT I am running is `sbt 0.13.12`

## Going Beyond

### SBT Tasks

In `sbt` a task is an action that you want to execute. You can view all the tasks applicable to a project by running the `sbt tasks` task.

~~~
$ sbt tasks
~~~

The above task would produce the following output

~~~
[info] Set current project to raw (in build file:/F:/Complex/Raw/)

This is a list of tasks defined for the current project.
It does not list the scopes the tasks are defined in; use the 'inspect' command for that.
Tasks produce values.  Use the 'show' command to run the task and print the resulting value.

  clean            Deletes files produced by the build, such as generated sources, compiled classes, and task caches.
  compile          Compiles sources.
  console          Starts the Scala interpreter with the project classes on the classpath.
  consoleProject   Starts the Scala interpreter with the sbt and the build definition on the classpath and useful imports.
  consoleQuick     Starts the Scala interpreter with the project dependencies on the classpath.
  copyResources    Copies resources to the output directory.
  doc              Generates API documentation.
  package          Produces the main artifact, such as a binary jar.  This is typically an alias for the task that actually does the packaging.
  packageBin       Produces a main artifact, such as a binary jar.
  packageDoc       Produces a documentation artifact, such as a jar containing API documentation.
  packageSrc       Produces a source artifact, such as a jar containing sources and resources.
  publish          Publishes artifacts to a repository.
  publishLocal     Publishes artifacts to the local Ivy repository.
  publishM2        Publishes artifacts to the local Maven repository.
  run              Runs a main class, passing along arguments provided on the command line.
  runMain          Runs the main class selected by the first argument, passing the remaining arguments to the main method.
  test             Executes all tests.
  testOnly         Executes the tests provided as arguments or all tests if no arguments are provided.
  testQuick        Executes the tests that either failed before, were not run or whose transitive dependencies changed, among those provided as arguments.
  update           Resolves and optionally retrieves dependencies, producing a report.

More tasks may be viewed by increasing verbosity.  See 'help tasks'.
~~~

### SBT Modes

One of the interesting things about `sbt` is that it can run in 2 modes. There is a command line mode (e.g. running `sbt compile`) that we can use to execute specific sbt tasks.

The other mode is to run it in the interactive mode. We can just type `sbt` in the command line to enter the interactive mode.  From within the interactive mode, we can start the Scala Interpreter by running the `console` tasks

~~~
$ sbt
[info] Set current project to raw (in build file:/F:/Complex/Raw/)
> console
[info] Starting scala interpreter...
[info]
Welcome to Scala version 2.10.6 (Java HotSpot(TM) 64-Bit Server VM, Java 1.8.0_101).
Type in expressions to have them evaluated.
Type :help for more information.

scala> 1+1
res0: Int = 2
~~~   

### Hello World using Scala + SBT

Week 1 of the course also has a [nice tutorial](https://www.coursera.org/learn/progfun1/supplement/VuJFf/intellij-idea-tutorial) detailing how to go about having a 'Hello World' Program running using Scala + SBT.

> The code for this example is available in [GitHub](https://github.com/abgoswam/getting-started-and-beyond/tree/master/01-sbt/HelloWorld)

There are 2 ways to run this Hello World program.

1. From within intellij
    - This is simply achieved by right clicking on the object and saying `Run 'LetsSayHello'`
2. Using the SBT command line

~~~
>sbt
Java HotSpot(TM) 64-Bit Server VM warning: ignoring option MaxPermSize=256m; support was removed in 8.0
[info] Loading project definition from E:\hackerreborn\getting-started-and-beyond\01-sbt\HelloWorld\project
[info] Set current project to HelloWorld (in build file:/E:/hackerreborn/getting-started-and-beyond/01-sbt/HelloWorld/)

> run
[info] Updating {file:/E:/hackerreborn/getting-started-and-beyond/01-sbt/HelloWorld/}helloworld...
[info] Resolving jline#jline;2.14.1 ...
[info] Done updating.
[info] Compiling 1 Scala source to E:\hackerreborn\getting-started-and-beyond\01-sbt\HelloWorld\target\scala-2.12\classes...
[info] 'compiler-interface' not yet compiled for Scala 2.12.0. Compiling...
[info]   Compilation completed in 26.195 s
[info] Running LetsSayHello
Lets Say Hello!
[success] Total time: 33 s, completed Nov 2, 2016 11:24:01 AM
~~~

### build.sbt

[TBD]

### Synchronizing SBT

[TBD]

### Dependencies

[TBD]

### Running Tests

[TBD]

## Misc Tips

[TBD]

## References

- https://github.com/shekhargulati/52-technologies-in-2016/tree/master/02-sbt
