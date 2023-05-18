import json
import base64

# SS节点信息，包括加密的密码和加密方式
ss_node = "ss://YWVzLTI1Ni1nY206d3p2MjB2b2w="
ss_node_parts = ss_node.split("://")[1].split(":")
ss_password = base64.urlsafe_b64decode(ss_node_parts[1] + "=" * (-len(ss_node_parts[1]) % 4))
ss_method = ss_node_parts[0]

# 解析插件参数
plugin_opts = {"mode": "", "host": ""}
plugin_opts_str = getUrlArg(ss_node_parts[4], "plugin-opts")
if plugin_opts_str:
    plugin_opts_str = base64.urlsafe_b64decode(plugin_opts_str + "=" * (-len(plugin_opts_str) % 4)).decode()
    plugin_opts_parts = plugin_opts_str.split(";")
    for part in plugin_opts_parts:
        if part.startswith("obfs="):
            plugin_opts["mode"] = part[5:]
        elif part.startswith("obfs-host="):
            plugin_opts["host"] = part[10:]

# 构建SS节点信息的JSON对象
ss_info = {
    "method": ss_method,
    "password": ss_password.decode(),
    "plugin": "obfs",
    "plugin-opts": plugin_opts
}

# 输出解析后的结果
print(json.dumps(ss_info, indent=4))
