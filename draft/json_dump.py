import json

text = '''
{
  name: 🇩🇪 德国-3.18MB/s(Youtube:不良林) 2,
  server: 217.79.184.18,
  port: 443,
  type: trojan,
  password: 27af95ea-e457-4bc9-9e36-8042ae657f4e,
  sni: download.xn--mes358a9urctx.com,
  skip-cert-verify: true,
  udp: true
}


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
