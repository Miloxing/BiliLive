import json
import logging
import time


# 返回当前时间
def get_current_time():
    return time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))


g_config = None


# 加载配置
def load_config(file="./config.json"):
    global g_config
    if g_config:
        return g_config
    else:
        try:
            with open(file, 'r') as config:
                g_config = json.load(config)
            return g_config
        except Exception:
            logging.error('配置文件加载错误！')


# 计时装饰器,返回函数执行时间
def time_cal(func):
    def _time_cal(*args, **kw):
        start_time = time.time()
        func(*args, **kw)
        end_time = time.time()
        return end_time - start_time

    return _time_cal
