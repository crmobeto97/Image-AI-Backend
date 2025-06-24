# Performance Testing with JMeter

This readme file provides information on performing performance tests using JMeter within our organization. JMeter is a popular open-source tool for load testing and measuring the performance of applications. Below, you will find details on installing JMeter, along with a brief description of the types of testing that can be conducted using JMeter.

## JMeter Documentation

To gain a comprehensive understanding of JMeter and its capabilities, please refer to the official JMeter documentation. The documentation provides in-depth information on various aspects of JMeter, including installation, configuration, test planning, and result analysis. You can access the official documentation at the following link:

[JMeter Official Documentation](https://jmeter.apache.org/usermanual/index.html)

## Installation Guide

To install JMeter, follow these steps:

1.  Install [Java 8](https://www.java.com/es/download/manual.jsp)
2.  Visit the [JMeter Downloads](https://jmeter.apache.org/download_jmeter.cgi) page.
3.  Download the latest stable release of JMeter.
4.  Extract the downloaded package to your desired location.
5.  JMeter does not require any formal installation process. You can simply run the JMeter executable file present in the extracted package.

For detailed installation instructions, refer to the official JMeter documentation mentioned above.

## Request Testing with JMeter

JMeter offers a wide range of testing capabilities. Some common types of request testing that can be performed using JMeter include:

1.  **Load Testing**: Simulate a high load on the system by generating a large number of concurrent requests. This type of testing helps identify the system's performance under expected and peak load conditions.

2.  **Stress Testing**: Determine the system's behavior under extreme conditions by overwhelming it with an exceptionally high load. This testing helps identify performance bottlenecks and potential failure points.

3.  **Performance Testing**: Measure the performance of various system components, such as web servers, application servers, databases, and APIs. Performance testing helps assess response times, throughput, and resource usage.

4.  **API Testing**: Test the performance and responsiveness of APIs by simulating multiple concurrent requests and verifying the API's behavior under different load scenarios.

5.  **Endurance Testing**: Evaluate the system's performance over an extended period by subjecting it to a consistent load for a prolonged duration. This testing helps identify any degradation in performance or resource utilization over time.

These are just a few examples of the testing scenarios that can be performed using JMeter. The tool offers a rich set of features and flexibility to cater to various testing requirements.

Please refer to the official JMeter documentation for detailed information on configuring test plans, creating test scenarios, analyzing results, and utilizing advanced features of JMeter.

## Quick Start

### Prepare the .jmx with the UI

1.  Execute the file "ApacheJMeter.jar" in "\apache-jmeter-X.X\bin\" in the folder extrac from the Instalation step (X.X is the Jmeter versión)
2.  Configure the Test Plan, you can use [Base_Performance_Plan_Test.jmx](/baseline/performance-test/jmeter/Base_Performance_Plan_Test.jmx) for fast configuration
3.  Configure the http requests in the UI
    -   Sample request: is used for pages without parameters, like a home page
    -   API Request with random parameters: use for page with parameters you can request like integers random numbers for real request, like ask for object in a list
    -   API Request with CSV Parameters: use for page with complex parameters you need with combinations alphanumerics or another complex patron
4.  Save the plan accordin the standard in [taggin](/baseline/style-guides/taggin/README.md) (Resource Name)

with this steps, finish the test plan and you can run manualy the performance/stress test

### Configure container test

1.  Take the [Dockerfile Jmeter Base](/baseline/containers/jmeter/Dockerfile)
2.  Create a Folder name "reports"
3.  Build the image with the .jmx and the run_test.sh in the same folder with the command   
```Dockerfile
docker build . -t "jmeter"
```
4.  Run the container with the command (in linux)
```Dockerfile
docker run -v "$(pwd)/reports:/home/jmeter/reports" jmeter
```
5.  After running the container, the final report will be found in the "report" folder, save the report

### Github Actions

For implementing in Github Actions, take the workflow [deploy-2-qa-and-E2E-Performance-testing.yml](/baseline/ci-cd/deploy-2-qa-and-E2E-Performance-testing.yml), in specific, [Performance testing phase](/baseline/ci-cd/deploy-2-qa-and-E2E-Performance-testing.yml#Performance_Testing_Phase)

