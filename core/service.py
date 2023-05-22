import json
import random
from datetime import datetime, timedelta

from utils.BaseEncode import base64_decode
from utils.Converter import ToYaml, ToOrigin
from concurrent import futures

from utils.urltools import GetUrl


def get_random():
    return '_' + str(random.randint(11, 71))


class ProxyList:
    def __init__(self):
        self.mydate_now = datetime.now()
        self.mydate_today = self.mydate_now.strftime('%m%d')
        self.mydate = (self.mydate_now - timedelta(days=1)).strftime('%m%d')
        self.mydate_year = self.mydate_now.strftime('%Y')
        self.mydate_month = self.mydate_now.strftime('%m')
        self.mydate_day = (self.mydate_now - timedelta(days=1)).strftime('%Y%m%d')
        self.url_get = GetUrl()
        self.yto = ToOrigin()
        self.oty = ToYaml()
        pass

    def get_url_content(self, index_url):
        return self.url_get.get_content(index_url), index_url
        pass

    def get_origin_lst(self):
        with open('linkurls.txt', 'r', encoding='utf8') as f:
            content = f.read()
        content_list = content.split('\n')
        self.origin_lst = []
        with futures.ThreadPoolExecutor() as executor:
            to_do = []
            for raw_item in content_list:
                if raw_item != '':
                    my_item = raw_item.replace('{date}', self.mydate).replace('{year}', self.mydate_year).replace(
                        '{month}',
                        self.mydate_month).replace(
                        '{day}', self.mydate_day)
                    sub = executor.submit(self.get_url_content, my_item)
                    to_do.append(sub)
        for _ in futures.as_completed(to_do):
            content = _.result()[0]
            my_item = _.result()[1]
            if 'yaml' in my_item or 'yml' in my_item:  # 首先是yaml格式的转化
                self.origin_lst.extend(self.yto.func_yml_to_origin(content))
            elif 'vmess://' in content or 'ss://' in content or 'ssr://' in content or 'trojan://' in content:  # 原始
                self.origin_lst.extend(list(filter(lambda x: x.strip(), content.split('\n'))))
                # result_list.append(self.oty.func_origin_to_yml(content))
            else:
                raw_content = base64_decode(content)
                self.origin_lst.extend(list(filter(lambda x: x.strip(), raw_content.split('\n'))))
                # result_list.append(self.oty.func_origin_to_yml(raw_content))
        return self.origin_lst

    def parse_origin_to_yml(self):
        self.yml_lst = self.oty.func_origin_to_yml(self.origin_lst)
        return self.yml_lst
        pass

    def write_origin(self, origin_nodes):
        with open(f'{self.mydate_day}.yaml', 'w', encoding='utf8') as f:
            for origin_node_item in origin_nodes:
                f.write(origin_node_item + '\n')
        pass

    def generate_yml(self):
        proxy_nodes_name = []
        proxy_nodes = []
        proxy_nodes_name_lst = []
        self.yml_lst = set(self.yml_lst)
        for yml_res_item in self.yml_lst:
            if yml_res_item:
                proxy_node_name = 'leilei' + get_random() if not json.loads(yml_res_item)['name'] else \
                    json.loads(yml_res_item)['name'].replace('(Youtube:不良林)', '')
                if proxy_node_name in proxy_nodes_name_lst:
                    continue
                else:
                    proxy_nodes_name_lst.append(proxy_node_name)
                    proxy_nodes.append(yml_res_item)
                    proxy_nodes_name.append(proxy_node_name)
        with open('core/rules.txt', 'r', encoding='utf8') as f:
            export_rules = f.read()
        return proxy_nodes_name, proxy_nodes, export_rules
        pass


if __name__ == '__main__':
    proxy_lst = ProxyList()
    origin_res_lst = proxy_lst.get_origin_lst()
    yml_res_lst = proxy_lst.parse_origin_to_yml()
    proxy_nodes = []
    for yml_res_item in yml_res_lst:
        proxy_node_name = json.loads(yml_res_item)['name'] if json.loads(yml_res_item)['name'] != None else 'leilei'
        proxy_node = yml_res_item.replace('"', '')
        proxy_nodes.append(proxy_node)
    with open('rules.txt', 'r', encoding='utf8') as f:
        export_rules = f.read()
