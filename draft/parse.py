import urllib.parse
from utils.Converter import ToYaml

url = "https://example.com/?q=%E4%BD%A0%E5%A5%BD"
index_url = 'trojan://shibushi@jp.kuaitao.xyz:443?allowInsecure=1&sni=jp.kuaitao.xyz#%E6%97%A5%E6%9C%AC-4.19MB%2Fs%28Youtube%3A%E4%B8%8D%E8%89%AF%E6%9E%97%29'
decoded_url = urllib.parse.unquote(index_url)
# print(decoded_url)

# temurl = '%22Host%22:%22livestream2.tv360.vn%22'

temtem = 'aes-128-gcm:83XvX4Vo%*3a:216.52.183.243:80/?plugin=obfs-local%3Bobfs%3Dhttp'
print(urllib.parse.unquote(temtem))
# ss_url = 'YWVzLTEyOC1nY206ODNYdlg0Vm8lKjNh@216.52.183.243:80/?plugin=obfs-local%3Bobfs%3Dhttp#%28%E5%B7%B2%E5%AD%98%E6%B4%BB1%E5%A4%A9%29%E7%BE%8E%E5%9B%BD-1.53MB%2Fs%28Youtube%3A%E4%B8%8D%E8%89%AF%E6%9E%97%29'
# toy = ToYaml()
# ctx = toy.to_ss(ss_url)
# print(ctx)

