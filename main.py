from core.ExportUtil import ExportCore
from tel import config
from tel.scrapy import Tel_Proxy

if __name__ == '__main__':
    # export = ExportCore()
    # export.save_yml()
    # export.save_origin()  # 这个origin有了后就只能直接调用clash进行转化
    tel_proxy = Tel_Proxy()
    tel_proxy.get()
