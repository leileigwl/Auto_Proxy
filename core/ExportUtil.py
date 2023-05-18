from jinja2 import Template
from core.service import ProxyList

epxort_str = '''port: 7890
socks-port: 7891
allow-lan: true
mode: Rule
log-level: info
external-controller: 127.0.0.1:9090
proxies:{% for proxy_node in proxy_nodes %}
- {{proxy_node}}{% endfor %}
proxy-groups:
  - name: 🚀 节点选择
    type: select
    proxies:
      - ♻️ 自动选择
      - DIRECT{% for proxy_name in proxy_nodes_name %}
      - {{proxy_name}}{% endfor %}
  - name: ♻️ 自动选择
    type: url-test
    url: http://www.gstatic.com/generate_204
    interval: 300
    tolerance: 50
    proxies:{% for proxy_name in proxy_nodes_name %}
      - {{proxy_name}}{% endfor %}
  - name: 🌍 国外媒体
    type: select
    proxies:
      - 🚀 节点选择
      - ♻️ 自动选择
      - 🎯 全球直连{% for proxy_name in proxy_nodes_name %}
      - {{proxy_name}}{% endfor %}
  - name: 📲 电报信息
    type: select
    proxies:
      - 🚀 节点选择
      - 🎯 全球直连{% for proxy_name in proxy_nodes_name %}
      - {{proxy_name}}{% endfor %}
  - name: Ⓜ️ 微软服务
    type: select
    proxies:
      - 🎯 全球直连
      - 🚀 节点选择{% for proxy_name in proxy_nodes_name %}
      - {{proxy_name}}{% endfor %}
  - name: 🍎 苹果服务
    type: select
    proxies:
      - 🚀 节点选择
      - 🎯 全球直连{% for proxy_name in proxy_nodes_name %}
      - {{proxy_name}}{% endfor %}
  - name: 📢 谷歌FCM
    type: select
    proxies:
      - 🚀 节点选择
      - 🎯 全球直连
      - ♻️ 自动选择{% for proxy_name in proxy_nodes_name %}
      - {{proxy_name}}{% endfor %}
  - name: 🎯 全球直连
    type: select
    proxies:
      - DIRECT
      - 🚀 节点选择
      - ♻️ 自动选择
  - name: 🛑 全球拦截
    type: select
    proxies:
      - REJECT
      - DIRECT
  - name: 🍃 应用净化
    type: select
    proxies:
      - REJECT
      - DIRECT
  - name: 🐟 漏网之鱼
    type: select
    proxies:
      - 🚀 节点选择
      - 🎯 全球直连
      - ♻️ 自动选择{% for proxy_name in proxy_nodes_name %}
      - {{proxy_name}}{% endfor %}
rules:
{{export_rules}}
'''


class ExportCore():
    def __init__(self):
        self.myproxy = ProxyList()
        self.myproxy.get_origin_lst()

    def save_yml(self):
        template = Template(epxort_str)
        self.myproxy.parse_origin_to_yml()
        proxy_nodes_name, proxy_nodes, export_rules = self.myproxy.generate_yml()
        out = template.render(proxy_nodes=proxy_nodes, proxy_nodes_name=proxy_nodes_name, export_rules=export_rules)
        with open(f'proxies/{self.myproxy.mydate_today}/{self.myproxy.mydate_today}.yaml', 'w', encoding='utf8') as f:
            f.write(out)

    def save_origin(self):
        with open(f'proxies/{self.myproxy.mydate_today}/{self.myproxy.mydate_today}.txt', 'w', encoding='utf8') as f:
            for origin_lst_item in self.myproxy.origin_lst:
                f.write(origin_lst_item + '\n')


def test2():  # 离线测试
    from utils.Converter import ToYaml, ToOrigin
    template = Template(epxort_str)
    myproxy = ProxyList()
    with open('../utils/111.txt', 'r', encoding='utf8') as f:
        content = f.read()
    pass
    oty = ToYaml()
    myproxy.yml_lst = oty.func_origin_to_yml(content)
    proxy_nodes_name, proxy_nodes, export_rules = myproxy.generate_yml()
    out = template.render(proxy_nodes=proxy_nodes, proxy_nodes_name=proxy_nodes_name, export_rules=export_rules)

    with open('result.yaml', 'w', encoding='utf8') as f:
        f.write(out)


def test3():
    from utils.urltools import GetUrl
    from utils.BaseEncode import base64_decode
    url_get = GetUrl()
    # url_index = 'https://raw.fastgit.org/chfchf0306/jeidian4.18/main/4.18'
    # url_index='https://raw.fastgit.org/freefq/free/master/v2'
    url_index = 'https://raw.fastgit.org/pojiezhiyuanjun/freev2/master/0518.txt'
    resp = url_get.get_content(url_index)
    res = base64_decode(resp)
    with open('../utils/111.txt', 'w', encoding='utf8') as f:
        f.write(res)

    pass


if __name__ == '__main__':
    pass
