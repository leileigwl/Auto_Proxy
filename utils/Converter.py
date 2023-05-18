# 用来获取yml中的节点
# 并把节点拼接成对应的节点类型添加为其原本格式
import json
import re
import urllib.parse
import yaml
from utils.BaseEncode import base64_decode, base64_encode
import random


def get_random():
    return '_' + str(random.randint(11, 71))


class ToOrigin:
    def __init__(self):
        pass

    def func_yml_to_origin(self, content):
        # vmess 的内容转换成yaml
        result_list = []
        raw_content = yaml.load(content, Loader=yaml.BaseLoader)
        prxoy_list = raw_content.get('proxies')
        # print(prxoy_list)
        for proxy_item in prxoy_list:
            if proxy_item.get('type') == 'vmess':  # 这个里面全是yaml 的节点 最后要转换成vmess节点
                result_node = self.parse_node(proxy_item, 'vmess')  # 传的参数都是一个json节点,返回一个完成的vmess节点，并合并成加密合并成一行
            elif proxy_item.get('type') == 'ss':
                result_node = self.parse_node(proxy_item, 'ss')
            elif proxy_item.get('type') == 'ssr':
                result_node = self.parse_node(proxy_item, 'ssr')
            elif proxy_item.get('type') == 'trojan':
                result_node = self.parse_node(proxy_item, 'trojan')
            else:
                continue
            result_list.append(result_node)
        return result_list

    def parse_node(self, content, node_type):  # 将yaml节点转换成vmess/ss/ssr/trojan
        raw_node = {}
        raw_node['type'] = content['type']
        raw_node['ps'] = content['name']
        raw_node['add'] = content['server']
        raw_node['port'] = content['port']
        if 'udp' in content:
            raw_node['udp'] = content['udp']
        if node_type == 'vmess':
            result_node = self.parse_vmess(content, raw_node)  # 用来解析vmess节点
        elif node_type == 'ss':
            result_node = self.parse_ss(content)
        elif node_type == 'ssr':
            result_node = self.parse_ssr(content, raw_node)
        elif node_type == 'trojan':
            result_node = self.parse_trojan(content)
        # print(result_node)
        return result_node

    def parse_vmess(self, content, raw_node):  # 将yml转成 vmess
        raw_node['v'] = '2'
        raw_node['type'] = 'none'
        raw_node['id'] = content['uuid']
        raw_node['aid'] = content['alterId']
        raw_node['net'] = content['network'] if 'network' in content else 'tcp'
        raw_node['sni'] = content['servername'] if 'servername' in content else ''
        raw_node['tls'] = 'tls' if content['tls'] == 'true' else ''
        vmess_net = raw_node['net']
        if vmess_net == 'ws':
            if 'ws-opts' in content:
                raw_node['path'] = content['ws-opts']['path'] if 'path' in content['ws-opts'] else '/'
                if 'headers' in content['ws-opts']:
                    raw_node['host'] = content['ws-opts']['headers']['Host']
            pass
        elif vmess_net == 'http':
            raw_node['path'] = content['http-opts']['path'][0]
            raw_node['hots'] = content['http-opts']['Host'][0]
            pass
        elif vmess_net == 'h2':
            raw_node['path'] = content["h2-opts"]["path"]
            raw_node['host'] = content["h2-opts"]["host"][0]
            pass
        elif vmess_net == 'grpc':
            raw_node['path'] = content["grpc-opts"]["grpc-service-name"]
            raw_node['host'] = content["servername"]
            pass
        vmess_node = json.dumps(raw_node, sort_keys=False, indent=2,
                                ensure_ascii=False)
        # 这里可以用dict转化一下顺序然后就可以直接导入vray2
        # 或者去设计一个类，用继承的方式；同时写一个方法，将这些信息转化成json串
        result_node = str('vmess://' + base64_encode(vmess_node))
        return result_node
        pass

    def parse_ss(self, content):
        raw_content = str(content['cipher']) + ':' + str(content['password']) + '@' + str(
            content['server']) + ':' + str(
            content['port'])
        encode_content = base64_encode(raw_content)
        result_node = str('ss://' + encode_content + '#' + str(urllib.parse.quote(content['name'])))
        return result_node
        pass

    def parse_trojan(self, content):
        trojan_proxy = str(
            'trojan://' + str(content['password']) + '@' + str(content['server']) + ':' + str(
                content['port']) + '#' + str(
                urllib.parse.quote(content['name'])))
        return trojan_proxy
        pass

    def parse_ssr(self, content, raw_node):
        raw_content = str(content['cipher']) + ':' + str(content['password']) + '@' + str(
            content['server']) + ':' + str(
            content['port'])
        encode_content = base64_encode(raw_content)
        result_node = str('ssr://' + encode_content + '#' + str(urllib.parse.quote(content['name'])))
        return result_node
        pass


class ToYaml:
    def __init__(self):
        pass

    def to_vmess(self, content):  # 将vmess节点转化成clash
        result_node = {}
        content = json.loads(base64_decode(content))
        result_node['name'] = urllib.parse.unquote(content['ps']).replace('\r', '').replace(' ', '') + get_random()
        result_node['server'] = content['add']
        result_node['port'] = content['port']
        result_node['type'] = 'vmess'
        result_node['uuid'] = '00000000-0000-0000-0000-000000000000' if content['id'] == '' else content['id']
        result_node['alterId'] = content['aid']
        result_node['cipher'] = 'auto'
        result_node['tls'] = False if content['tls'] == '' else True
        result_node['skip-cert-verify'] = True
        if not content['net'] == 'tcp' or content['net'] == 'http':
            result_node['network'] = content['net']
        if content['net'] == 'ws':  # 这里只支持了ws,tcp,http，后续还有拓展
            result_node['ws-opts'] = {}
            result_node['ws-opts']['path'] = content['path'] if 'path' in content else '/'
            # result_node['ws-opts']['headers']['Host'] = content['host'] if 'host' in content else ''
            if 'host' in content:
                result_node['ws-opts']['headers'] = {}
                if '%' in content['host']:
                    pass_str = '"'
                    content['host'] = f'{pass_str}{content["host"]}{pass_str}'
                    # content['host'] = urllib.parse.unquote(content['host']).replace('\\', '"')
                result_node['ws-opts']['headers']['Host'] = content['add'] if content['host'] == '' else content[
                    'host']
        elif content['net'] == 'quic':
            pass
        elif content['net'] == 'kcp':
            pass
        result_node['udp'] = True
        result_str = json.dumps(result_node, sort_keys=False, ensure_ascii=False)
        return result_str
        pass

    def to_ss(self, content):
        result_node = {}
        content_list = content.split('#')  # 左右分割
        if '@' in content_list[0]:
            ss_index_list = content_list[0].split('@')  # 前面的 服务器字段
            ss_info = base64_decode(ss_index_list[0]) + ":" + ss_index_list[1]
        else:
            ss_info = base64_decode(content_list[0])
        ss_info_list = ss_info.split(':')
        result_node['name'] = urllib.parse.unquote(content_list[1]).replace('\r', '').replace(' ', '') + get_random()
        result_node['server'] = ss_info_list[2]
        result_node['port'] = ss_info_list[-1]
        result_node['type'] = 'ss'
        result_node['cipher'] = ss_info_list[0]
        result_node['password'] = ss_info_list[1]
        result_node['udp'] = True
        result_str = json.dumps(result_node, ensure_ascii=False, sort_keys=False)
        return result_str
        pass

    def to_ssr(self, content):
        pass

    def to_trojan(self, content):
        result_node = {}
        content_lst = content.split('#')
        result_node['name'] = urllib.parse.unquote(content_lst[1]).replace('\r', '').replace(' ', '') + get_random()
        trojan_info_list = re.split(r':|@|\?', content_lst[0])
        result_node['server'] = trojan_info_list[1]
        result_node['port'] = trojan_info_list[2]
        result_node['type'] = 'trojan'
        result_node['password'] = trojan_info_list[0]
        if 'sni' in content_lst[0]:
            result_node['sni'] = trojan_info_list[-1].split('&')[-1]
        result_node['skip-cert-verify'] = True
        result_node['udp'] = True
        result_str = json.dumps(result_node, sort_keys=False, ensure_ascii=False)
        return result_str

    def parse_nodes(self, nodes_lst):  # 传入list数组
        result_lst = []
        for content_item in nodes_lst:
            if not content_item == '':
                node_list = content_item.split('://')
                node_type = node_list[0]
                node_value = node_list[1]
                if node_type == 'vmess':
                    yaml_node = self.to_vmess(node_value)
                elif node_type == 'ss':
                    yaml_node = self.to_ss(node_value)
                elif node_type == 'ssr':
                    yaml_node = self.to_ssr(node_value)
                elif node_type == 'trojan':
                    yaml_node = self.to_trojan(node_value)
                else:
                    continue
                result_lst.append(yaml_node)
        return result_lst

    def func_origin_to_yml(self, content):
        if not type(content) == type(''):
            return self.parse_nodes(content)
        else:
            return self.parse_nodes(content.split('\n'))

        pass

    def export(self, content):
        pass


# index_url = 'https://raw.fastgit.org/oslook/clash-freenode/main/clash.yaml'
# ctxx = urltools.yml_get(index_url)
# parse_yml(ctxx)

if __name__ == '__main__':
    # with open('draft.yml', 'r', encoding='utf-8') as f:  # yaml to vmess测试
    #     ctx = f.read()
    # # print(ctx)
    # yto = ToOrigin()
    # yto.func_yml_to_origin(ctx)
    # with open('single_test.yml', 'r', encoding='utf8') as f:
    #     ctx = f.read()
    # yto = Yaml_to_origin()
    # yto.decode_yml(ctx)
    # with open('111.txt', 'r', encoding='utf8') as f:  # vmess to yaml 测试
    #     content = f.read()
    # oty = ToYaml()
    # response = oty.func_origin_to_yml(content)
    # print(response)
    pass
