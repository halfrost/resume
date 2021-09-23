+++
# Experience widget.
widget = "experience"  # See https://sourcethemes.com/academic/docs/page-builder/
headless = true  # This file represents a page section.
active = true  # Activate this widget? true/false
weight = 40  # Order that this section will appear.

title = "Experience"
subtitle = ""

# Date format for experience
#   Refer to https://sourcethemes.com/academic/docs/customization/#date-format
date_format = "Jan 2006"

# Experiences.
#   Add/remove as many `[[experience]]` blocks below as you like.
#   Required fields are `title`, `company`, and `date_start`.
#   Leave `date_end` empty if it's your current employer.
#   Begin/end multi-line descriptions with 3 quotes `"""`.
[[experience]]
  title = "Staff Engineer"
  company = "Binance.com"
  company_url = ""
  location = "Singapore City, Singapore"
  date_start = "2021-05-01"
  date_end = ""
  description = """
<img data-src="/media/binance.jpg" alt="alibaba" style="padding-bottom: 30px;" class="lazyload">

- Led a team consisting of 7 engineers to implement from scratch and successfully launch the firm’s first Strategy Distribution Engine – Themis, a smart strategy engine based on traffic flow and predicate conditions’ strategy, which provides handy service for vendors and consumers; Build strategy ecosystem, including Themis backend service, Themis-cli (deployment tool), Themis-admin(management configuration system), and Themis-SDK (developers suite of integrated for iOS/Android/H5). 
- Designed architecture of native service mesh cloud app on top of Golang backend services, using MySQL and Redis as high-performance database, Prow, Bazel as CI/CD, Hive, ClickHouse as data statistics and AWS by K8s + Istio as deployment environment.
- Themis ecosystem managed to accumulate 200 million users within 10 days of its release to the public, with delivery rate above 97%, daily peak value over  5000k and online connections averaged 10k-15k QPS.

"""

[[experience]]
  title = "Senior Back End Engineer ｜Senior Research And Development Engineer"
  company = "Alibaba Group"
  company_url = ""
  location = "Shanghai, China"
  date_start = "2018-04-01"
  date_end = "2021-05-01"
  description = """
<img data-src="/media/alibaba.jpg" alt="alibaba" style="padding-bottom: 30px;" class="lazyload">

-	Participated in Tmall Double Eleven online shopping promotion for 2 consecutive years; led team consisting of 5 engineers to build Taco ecosystem, including Taco (a distributed Golang-based message streaming platform, which served 300 million users and 20 third-party partners), Taco-cli (deployment tool), Taco-console (cost calculation and analytics service), and Taco-SDK (suite of templates for iOS/Android/H5). 
-	Enriched Taco ecosystem by implementing Taco V2, an infura-like API gateway on top of Golang backend services, which used MySQL and Redis as high-performance database, RabbitMQ and Kafka as message queue, Hive, Blink and Elasticsearch as data and message pipeline query, and gRPC, Apache Thrift and HTTP as communication protocol.
-	Taco ecosystem successfully handles 1100 million+ push notifications per day, with delivery rate above 97% and delivery time of 0.72-1.2 seconds; daily peak value can reach 750k online connections with 30k-50k QPS.

"""

[[experience]]
  title = "Senior iOS Engineer | Front-End Engineer"
  company = "ele.me"
  company_url = "https://www.ele.me/"
  location = "Shanghai, China"
  date_start = "2017-02-01"
  date_end = "2018-04-01"
  description = """
<img data-src="/media/eleme.jpg" alt="eleme" style="padding-bottom: 30px;" class="lazyload">

Front-End Engineer
-	Development and maintenance of the company's basic services, StormEye, a weather service that will affect the company’s daily revenue. Different weathers have different revenue for each takeaway order. Worked on various small full stack projects with high proficiency in Golang, JavaScript and Objective-C.
-	Was responsible for Designed backend architecture with implementation in Golang, leveraging SOA-based microservices. RabbitMQ is used as the messaging queue and Apache Thrift as the communication protocol for Android, iOS and Web clients. In severe weather conditions, within China, it can help the company save 3 million per month on average.
-	Using Google S2 algorithm and Drove the efforts of building better scalability and performance across both PostgreSQL and application layers to achieve low latency with millions of requests per day on tens of millions of records. Service’s performance improved by 120%. Machine resources were reduced from 200 to 4, saving 98% of server resource.


Senior iOS Engineer
-	Developed the iOS application, Talaris, which was an aggregated same-day delivery platform for internal and third-party retailer using JavaScript, Objective-C and Ruby. Was in charge of building better scalability and performance across both Weex and Native application layers. The application’s monthly active users reached 90,000.
-	Was responsible for MVVM architecture design, routing design and API convergence management. Successfully decreased the crash rate from 7/10000 to 3/10000. Optimized the network layer, power and application fluency performance to help the team saving 15% power consumption and 7% network traffic consumption.
-	Training new engineers on MVVM architecture expertise, communicating with external deliveryman on technical difficulties, and sharing multiple-time technical topic within the team.

"""

[[experience]]
  title = "iOS Team Leader"
  company = "Shanghai Fangchuang Financial Information Service Co., Ltd."
  company_url = "https://www.fangchuang.com/"
  location = "Shanghai, China"
  date_start = "2016-05-01"
  date_end = "2017-02-01"
  description = """
<img data-src="/media/fangchuang.jpg" alt="fangchuang" style="padding-bottom: 30px;" class="lazyload">

- Led engineer team to develop 2nd version of iOS app Func, a product to help investors find and fund the most innovative start-ups; mainly responsible for technology architecture design, MVVM architecture reconstruction, Realm database replacement, instant messaging module migration and UI rewriting; 
- Worked closely with clients in investment banking and legal industries to collect user feedback and develop new features; actively applied Bugtags to monitor user behavior and optimize user experience. 
- Successfully decreased crash rate from 5/10000 to 1/10000 and increased network request success rate from 78% to 98%, the application having more than 50k monthly active users.

"""

[[experience]]
  title = "Senior iOS Engineer"
  company = "Shanghai Ping An Smart Technology Co., Ltd."
  company_url = "https://www.yqb.com/"
  location = "Shanghai, China"
  date_start = "2015-11-01"
  date_end = "2016-04-30"
  description = """
<img data-src="/media/yqb.jpg" alt="yqb" style="padding-bottom: 30px;" class="lazyload">

-	Was mainly responsible for the development of the 1QB Wallet hybird plug-in, using the Cordova framework to develop a payment plug-in for the 1QB Wallet app client, and burying points to count user behavior.
-	Building the Code Review platform in the team. Developed H5 webpack package deployment and remote backup distribution platform, including Jenkins integrated static code scanning on a daily basis and the CI/CD pipeline.


"""

[[experience]]
  title = "Junior iOS Engineer"
  company = "Quatanium Technology Co., Ltd."
  company_url = "https://github.com/quatanium"
  location = "Shanghai, China"
  date_start = "2013-06-01"
  date_end = "2015-11-01"
  description = """
<img data-src="/media/quatanium.jpg" alt="quatanium" style="padding-bottom: 30px;" class="lazyload">

-	Implemented and launched the very first iOS application, Qhome,  a smart home client, which provided an easy-to-use home automation solutions for both businesses and consumers. Was in charge of the camera research and development (Foscam, Haikang, WRT access control plug-in), real-time viewing, intercom, playback, and interaction with the server.
-	Improved the fluency by 30%, reduced the power consumption by 20% and network disconnect by 40% using Instrument (Core Animation, Time Profiler, Energy Diagnostics, Network) Optimization method.  Also optimized the code structure and compress pictures and finally reduced the total size of the app installation package by 50%.
-	Processed the user’s Crashlog with the third-party crash logging tool Crashlytics and the official TestFlight. Using statistics management tool Flurry to monitor user behavior and collect data for background data mining

"""

+++
