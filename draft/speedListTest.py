import requests

# 要测试的代理服务器
proxy_server = "yes.iamagoodman.net"
proxy_port = 16617

# 要测试的URL
url = "http://www.gstatic.com/generate_204"

# 构造代理服务器的URL
proxy_url = f"http://{proxy_server}:{proxy_port}"

# 设置代理服务器
proxies = {"http": proxy_url, "https": proxy_url}

# 发送HTTP请求并计算响应时间
try:
    response = requests.get(url, proxies=proxies, timeout=10)
    if response.status_code == 200:
        response_time = response.elapsed.total_seconds() * 1000
        print(f"代理服务器 {proxy_server}:{proxy_port} 的延迟为 {response_time:.2f} ms")
    else:
        print(f"代理服务器 {proxy_server}:{proxy_port} 请求失败，状态码为 {response.status_code}")
except Exception as e:
    print(f"代理服务器 {proxy_server}:{proxy_port} 请求失败，错误信息为 {str(e)}")