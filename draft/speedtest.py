import requests
import time

def test_proxy_delay(proxy):
    try:
        start_time = time.time()
        response = requests.get("http://www.gstatic.com/generate_204", proxies={"http": proxy, "https": proxy}, timeout=10)
        end_time = time.time()
        if response.status_code == 204:
            delay = (end_time - start_time) * 1000
            return delay
        else:
            return None
    except Exception as e:
        return None

def test_proxy_speed(proxy):
    url = "https://speed.hetzner.de/10MB.bin"
    try:
        start_time = time.time()
        response = requests.get(url, proxies={"http": proxy, "https": proxy}, timeout=10)
        end_time = time.time()
        if response.status_code == 200:
            speed = len(response.content) / (end_time - start_time) / 1024 / 1024
            return speed
        else:
            return None
    except Exception as e:
        return None

# 示例用法
proxy = "http://127.0.0.1:7890"
delay = test_proxy_delay(proxy)
if delay is not None:
    print(f"代理服务器 {proxy} 的延迟为 {delay:.2f} ms")
else:
    print(f"代理服务器 {proxy} 无法访问")

speed = test_proxy_speed(proxy)
if speed is not None:
    print(f"代理服务器 {proxy} 的速度为 {speed:.2f} MB/s")
else:
    print(f"代理服务器 {proxy} 无法访问")