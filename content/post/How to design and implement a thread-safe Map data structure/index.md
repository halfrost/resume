---
title: How to design and implement a thread-safe Map data structure
date: 2017-09-10T10:05:36.983Z
summary: Map is a very common data structure used to store some unordered key-value pairs. In mainstream programming languages, it comes with its implementation by default. STL in C and C++ implements Map, JavaScript also has Map, Java has HashMap, Swift and Python have Dictionary, Go has Map, and Objective-C has NSDictionary and NSMutableDictionary. Are all the above maps thread-safe? The answer is no, not all thread-safe. How can a thread-safe Map be implemented? To answer this question, you need to start with how to implement a Map.
draft: false
featured: false
authors:
  - halfrost
tags:
  - Go
categories:
  - Golang
image:
  filename: featured.png
  focal_point: Smart
  preview_only: false
links:
  - name: Read More
    url: 'https://halfrost.com/go_map_chapter_one/'

---

Map 是一种很常见的数据结构，用于存储一些无序的键值对。在主流的编程语言中，默认就自带它的实现。C、C++ 中的 STL 就实现了 Map，JavaScript 中也有 Map，Java 中有 HashMap，Swift 和 Python 中有 Dictionary，Go 中有 Map，Objective-C 中有 NSDictionary、NSMutableDictionary。

上面这些 Map 都是线程安全的么？答案是否定的，并非全是线程安全的。那如何能实现一个线程安全的 Map 呢？想回答这个问题，需要先从如何实现一个 Map 说起。

点击[阅读更多](https://halfrost.com/go_map_chapter_one/)看全文。
