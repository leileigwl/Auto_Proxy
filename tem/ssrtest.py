import base64

# 给定的 SSR 节点信息
ssr_node_str = "ssr://c2ctYW0zLmVxc3Vuc2hpbmUuY29tOjMyMDAxOm9yaWdpbjphZXMtMjU2LWNmYjp0bHMxLjJfdGlja2V0X2F1dGg6TTJjd1pFaHNTMDFGLz9ncm91cD1VMU5TVUhKdmRtbGtaWEkmcmVtYXJrcz01cGF3NVlxZzVaMmhMVE11TWpCTlFpOXpLRmx2ZFhSMVltVTY1TGlONkltdjV1N0Y2N3lZK3Z1N3lZJnByb3RvcGFyYW09JnByb3RvcGFyYW09"

# 对节点信息进行解码
ssr_node_bytes = base64.urlsafe_b64decode(ssr_node_str[6:])
ssr_node_info = ssr_node_bytes.decode()

# 将节点信息转换为字典
ssr_node_info_list = ssr_node_info.split(":")
ssr_node = {
    "server": ssr_node_info_list[0],
    "server_port": int(ssr_node_info_list[1]),
    "protocol": ssr_node_info_list[2],
    "method": ssr_node_info_list[3],
    "obfs": ssr_node_info_list[4],
    "password": base64.b64decode(ssr_node_info_list[5]).decode(),
    "obfs_param": ssr_node_info_list[6],
    "protocol_param": ssr_node_info_list[7],
}

# 添加其他参数
ssr_node.update({
    "name": "新加坡-3.20MB/s(Youtube:不良林)",
    "type": "ssr",
    "cipher": "aes-256-cfb",
    "udp": True
})

# 打印节点信息
print(ssr_node)