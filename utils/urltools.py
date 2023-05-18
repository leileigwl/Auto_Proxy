from fake_useragent import UserAgent
import requests
from loguru import logger


class GetUrl():
    def __init__(self):
        pass

    def get_content(self, yml_url):
        headers = {
            "authority": "raw.fastgit.org",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "accept-language": "en,zh-CN;q=0.9,zh;q=0.8",
            "cache-control": "no-cache",
            "pragma": "no-cache",
            "sec-ch-ua": "\"Google Chrome\";v=\"113\", \"Chromium\";v=\"113\", \"Not-A.Brand\";v=\"24\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "none",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "user-agent": UserAgent().random}
        # proxies = {
        #     'http': 'http://localhost:7890',
        #     'https': 'http://localhost:7890'
        # }
        try:
            response = requests.get(yml_url, headers=headers)
            resp_code = response.status_code
            if resp_code == 200:
                return response.text
            # https: // juejin.cn / post / 7062150108590112804 获取响应304
        except requests.exceptions.RequestException:
            logger.warning(yml_url)
            raise Exception('请求不稳定，请关闭代理试试')
# index_url = 'https://nodefree.org/dy/2023/05/20230517.yaml'
# print(GetUrl.get_content(index_url))
