---
title: Weex layout engine powered by FlexBox algorithm
date: 2017-03-31T10:05:36.983Z
summary: In the last article, we talked about the basic process of Weex working on the iOS client. This article will analyze in detail how Weex lays out the native interface with high performance, and then will compare with the existing layout methods to see how Weex layout performance is. Open the Layout folder of Weex's source code, and you will see two c files. These two files are the Weex layout engine we are going to talk about today.
draft: false
featured: false
authors:
  - halfrost
tags:
  - Weex
categories:
  - Weex
image:
  filename: featured.png
  focal_point: Smart
  preview_only: false
links:
  - name: Read More
    url: 'https://halfrost.com/weex_flexbox/'

---

在上篇文章里面谈了Weex在iOS客户端工作的基本流程。这篇文章将会详细的分析Weex是如何高性能的布局原生界面的，之后还会与现有的布局方法进行对比，看看Weex的布局性能究竟如何。

打开Weex的源码的Layout文件夹，就会看到两个c的文件，这两个文件就是今天要谈的Weex的布局引擎。

Layout.h和Layout.c最开始是来自于React-Native里面的代码。也就是说Weex和React-Native的布局引擎都是同一套代码。

当前React-Native的代码里面已经没有这两个文件了，而是换成了Yoga。

点击[阅读更多](https://halfrost.com/weex_flexbox/)看全文。