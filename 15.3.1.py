#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import base64

message = "零基础Python从入门到精通"

msg = base64.b64encode(message.encode())

print("原文：", message)
print("base64 编码后的结果是：", msg)

text = base64.b64decode(msg)
print("base64 解码后的文本：", text.decode())
