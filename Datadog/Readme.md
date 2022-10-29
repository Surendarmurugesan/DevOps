# Datadog
It collects the Metrics, Logs, Traces, Events. 
### (Everything in One Place)


#   APM (Application performance management):: 
The translation of IT metrics into business meaning. A practice to monitor application insights, so we can:
1. Improve application/Infra/etc.. performance (Frontend app, Backend app, Infrastructure)
2. Improve user experience
3. Reduce issue and errors

# How is APM (Application performance management) monitoring performed?
1. Performance trends at-a-glance
2. Insights from the user perspective
3. Root cause analysis(RCA)
4. Generate alerts on anomalies
5. Tracks individual SQL statements
6. Code-level diagnostics
        
# Alternative Top APM tools apart from DATADOG ::
1. New Relic
2. Loupe
3. Traverse
4. Retrace

# What does Datadog can monitor?
* Infrastructure
* Log Management
* APM & Continuous profiler
* Database monitoring
* Synthetic Monitoring
* Incident management
* Real User monitoring
* CI visibility
* Severless
* Network Monitoring
* Cloud SIEM
* CSPM
* Sensitive Data Scanner
* Workload security

# How does Datadog collects data ??
There are multiple ways of sending the data to Datadog::
* From Datadog Agent
* Using Datadog API
* Integrations

# How does Datadog works ??

* Download & Install Datadog agent in your **Destination Host** servers.
* After installation, Sending the **data** from server to **Datadog**. (**Metrics, Events, Logs, Traces**)
* Using **Datadog Dashboard**, Able to use the data in **Alerts & Queries**.

# Monitoring key focus:
It prevents all replication for incidents and system failures. Managing and Maintaining the key aspects::
* **Availability**
* **Reliability**
* **Scalability**
* **Duration**

# What do I use Datadog ?
* To write easy and fast query on **traces/logs/metrics**.
* To monitor **Server/Host downtime**
* To monitor **Application/Services downtime**
* Service request/response **error rates**
* Service request/response **latency**
* SQL queries **duration**
* SLO(**Service Level Objectives**)'s like success requests/ total requests, duration/requests.

# How Datadog agent works?
Datadog agent is software that runs on your hosts. After installation, it automatically starts to collect events and metrics from hosts and sends them to Datadog, where you can search, filter, aggregate and alert on information.

Datadog agent acts like a **middle layer** between your application and datadog website.

There are two main components:
* **Collector**- Which collects data from your host on every 15 seconds.
* **Forwarder**- Which sends data to Datadog over https.

image.png
