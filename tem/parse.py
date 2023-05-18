import urllib.parse

url = "https://example.com/?q=%E4%BD%A0%E5%A5%BD"
index_url = 'trojan://shibushi@jp.kuaitao.xyz:443?allowInsecure=1&sni=jp.kuaitao.xyz#%E6%97%A5%E6%9C%AC-4.19MB%2Fs%28Youtube%3A%E4%B8%8D%E8%89%AF%E6%9E%97%29'
decoded_url = urllib.parse.unquote(index_url)
print(decoded_url)

temurl = '%22Host%22:%22livestream2.tv360.vn%22'
# print(urllib.parse.unquote(temurl))
