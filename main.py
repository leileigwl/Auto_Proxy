from core.ExportUtil import ExportCore
from tel import config

if __name__ == '__main__':
    export = ExportCore()
    export.save_yml()
    export.save_origin()  # 这个origin有了后就只能直接调用clash进行转化
    print('xixix' + config.api_id)
