import base64

ssr_url = "ssr://YWVzLTEyOC1jZmI6UWF6RWRjVGdiMTU5QCQq@14.29.124.168:24003#%E4%B8%AD%E5%9B%BD-311.5KB%2Fs%28Youtube%3A%E4%B8%8D%E8%89%AF%E6%9E%97%29"
ssr_info = ssr_url[6:]  # 去掉链接头的"ssr://"

# 解码并解析SSR参数
info = base64.urlsafe_b64decode(ssr_info + '=' * (4 - len(ssr_info) % 4)).decode()
params = info.split(":")
server_params = params[0].split("/")
server_addr = server_params[0]
server_port = server_params[1]
protocol = params[1]
method = params[2]
obfs_params = params[3].split("/")
obfs = obfs_params[0]
base64_pwd = obfs_params[1]

# 将密码和其他参数解码
pwd = base64.urlsafe_b64decode(base64_pwd + '=' * (4 - len(base64_pwd) % 4)).decode('utf-8')
remark = base64.urlsafe_b64decode(params[5] + '=' * (4 - len(params[5]) % 4)).decode('utf-8')

# 构造输出字典
output_dict = {
    'host': server_addr,
    'port': server_port,
    'password': pwd,
    'protocol': protocol,
    'method': method,
    'obfs': obfs,
    'remark': remark
}

print(output_dict)
