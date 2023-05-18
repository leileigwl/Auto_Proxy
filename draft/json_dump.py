import json

text = '''
- {name: _23, server: 170.187.134.190, port: 8443, type: trojan, password: cf4295378e209e70d12c5bdd017144dfd1c772d3, sni: 170-187-134-190.ipv4.rush.ml, skip-cert-verify: true, udp: true} 
'''


def parse_text(content):
    result = {}
    ctx = str(content).replace('{', '').replace('}', '').replace('\n', '')
    title_list = ctx.split(',')
    for item in title_list:
        item_list = item.split(':')
        result[item_list[0].replace(' ', '')] = item_list[1].replace(' ', '')
    res = json.dumps(result, ensure_ascii=False)  # 将dict转换为json
    return res


list_res = text.split('@')
for i in list_res:
    print(parse_text(i))
