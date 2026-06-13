---
title: "Efficient Cross-GPU Communication for Disaggregated LLM Serving"
authors:
- me
date: "2026-06-12T00:00:00Z"
publishDate: "2026-06-12T00:00:00Z"
publication_types: ["manuscript"]
publication:
  name: "Manuscript in preparation"
abstract: >-
  Large Language Model (LLM) serving increasingly relies on disaggregated architectures to improve resource utilization and scalability. However, existing LLM systems often depend on hardware-specific communication libraries tightly coupled to particular RDMA transports, resulting in fragmented implementations, limited portability, and significant engineering overhead when deploying across heterogeneous cloud environments.

  In this paper, we present CommBridge, a portable communication runtime for distributed LLM serving. CommBridge introduces a unified abstraction layer that decouples LLM communication primitives from underlying RDMA implementations, enabling seamless deployment across diverse networking backends including InfiniBand, RoCE, and AWS Elastic Fabric Adapter (EFA). The system exposes a minimal set of communication primitives optimized for key LLM workloads such as KV-cache migration, Mixture-of-Experts (MoE) dispatch and aggregation, model weight synchronization, and distributed inference scheduling.

  We implement CommBridge in production-scale LLM serving environments and evaluate it across clusters ranging from 64 to 2,048 GPUs. Experimental results demonstrate that CommBridge achieves performance comparable to highly optimized vendor-specific implementations while significantly reducing system complexity and improving deployment portability. Across representative LLM inference and training workloads, CommBridge improves end-to-end throughput by up to 2.3x and reduces communication latency by up to 47% compared with existing framework-integrated approaches.

  Our results suggest that communication portability can be achieved without sacrificing performance, providing a practical foundation for next-generation cloud-native LLM infrastructure.
summary: >-
  CommBridge is a portable communication runtime for disaggregated LLM serving that decouples LLM communication primitives from RDMA backends, improving deployment portability across InfiniBand, RoCE, and AWS EFA while preserving high-performance cross-GPU communication.
tags:
- LLM Serving
- Distributed Systems
- GPU Communication
- RDMA
- Machine Learning Systems
- Cloud Infrastructure
links: []
image:
  caption: ""
  focal_point: ""
  preview_only: false
projects: []
slides: ""
---
