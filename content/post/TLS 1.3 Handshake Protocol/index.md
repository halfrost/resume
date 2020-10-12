---
title: TLS 1.3 Handshake Protocol
date: 2018-10-21T10:05:36.983Z
summary: The handshake protocol is used to negotiate the security parameters of the connection. The handshake messages are provided to the TLS recording layer, where they are encapsulated into one or more TLSPlaintext or TLSCiphertext, and they are processed and transmitted according to the current active connection state. Protocol messages must be sent in a certain order (see below for the order). If the peer finds that the received handshake messages are not in the right order, they must use the "unexpected_message" alert message to abort the handshake.
draft: false
featured: false
authors:
  - halfrost
tags:
  - HTTPS
  - PROTOCOL
categories:
  - PROTOCOL
image:
  filename: featured.png
  focal_point: Smart
  preview_only: false
links:
  - name: Read More
    url: 'https://halfrost.com/tls_1-3_handshake_protocol/'

---

握手协议用于协商连接的安全参数。握手消息被提供给 TLS 记录层，在记录层它们被封装到一个或多个 TLSPlaintext 或 TLSCiphertext 中，它们按照当前活动连接状态进行处理和传输。

```c
      enum {
          client_hello(1),
          server_hello(2),
          new_session_ticket(4),
          end_of_early_data(5),
          encrypted_extensions(8),
          certificate(11),
          certificate_request(13),
          certificate_verify(15),
          finished(20),
          key_update(24),
          message_hash(254),
          (255)
      } HandshakeType;

      struct {
          HandshakeType msg_type;    /* handshake type */
          uint24 length;             /* remaining bytes in message */
          select (Handshake.msg_type) {
              case client_hello:          ClientHello;
              case server_hello:          ServerHello;
              case end_of_early_data:     EndOfEarlyData;
              case encrypted_extensions:  EncryptedExtensions;
              case certificate_request:   CertificateRequest;
              case certificate:           Certificate;
              case certificate_verify:    CertificateVerify;
              case finished:              Finished;
              case new_session_ticket:    NewSessionTicket;
              case key_update:            KeyUpdate;
          };
      } Handshake;
```

协议消息必须按照一定顺序发送(顺序见下文)。如果对端发现收到的握手消息顺序不对，必须使用 “unexpected\_message” alert 消息来中止握手。

点击[阅读更多](https://halfrost.com/tls_1-3_handshake_protocol/)看全文。