import logging
import requests
import time
import random
import json
from typing import List, Dict, Any
import os
import sys

# 修复 Windows PowerShell 中文乱码问题
if sys.platform == 'win32':
    try:
        # 设置标准输出编码为 UTF-8
        if sys.stdout.encoding != 'utf-8':
            sys.stdout.reconfigure(encoding='utf-8')
        if sys.stderr.encoding != 'utf-8':
            sys.stderr.reconfigure(encoding='utf-8')
    except (AttributeError, ValueError):
        # Python < 3.7 或无法重配置时，使用环境变量
        import io
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
        sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

# 配置日志
log_level = os.environ.get('LOG_LEVEL', 'INFO').upper()
logging.basicConfig(
    level=getattr(logging, log_level, logging.INFO),
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

class JuejinHelper:
    def __init__(self):
        self.user = None
        try:
            with open('config.json', 'r', encoding='utf-8') as f:
                config = json.load(f)
                self.cookie = config.get('cookie')
                logger.info("成功加载配置文件")
        except Exception as e:
            logger.error(f"加载配置文件失败: {str(e)}")
            raise
            
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'referer': 'https://juejin.cn/',
            'origin': 'https://juejin.cn'
        }
    
    def login(self, cookie: str):
        """登录掘金"""
        logger.info("开始登录掘金")
        self.cookie = cookie
        self.headers['cookie'] = cookie
        
        # 获取用户信息
        url = 'https://api.juejin.cn/user_api/v1/user/get'
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()  # 检查HTTP状态码
            
            # 检查响应内容
            if not response.text:
                raise Exception('响应内容为空')
            
            try:
                data = response.json()
            except json.JSONDecodeError as e:
                logger.error(f"JSON解析失败，响应内容: {response.text[:200]}")
                raise Exception(f'响应不是有效的JSON格式: {str(e)}')
            
            if data.get('err_no', -1) != 0:
                logger.error(f"登录失败: {data.get('err_msg', '未知错误')}")
                raise Exception('登录失败')
            self.user = data['data']
            logger.info(f"登录成功: {self.user['user_name']}")
            return self.user
        except requests.exceptions.RequestException as e:
            logger.error(f"登录请求异常: {str(e)}")
            raise
        except Exception as e:
            logger.error(f"登录处理异常: {str(e)}")
            raise

class Growth:
    def __init__(self, helper: JuejinHelper):
        self.helper = helper
        
    def get_today_status(self) -> bool:
        """获取今日签到状态"""
        logger.info("检查今日签到状态")
        url = 'https://api.juejin.cn/growth_api/v1/get_today_status'
        try:
            response = requests.get(url, headers=self.helper.headers, timeout=10)
            response.raise_for_status()
            
            if not response.text:
                raise Exception('响应内容为空')
            
            try:
                data = response.json()
            except json.JSONDecodeError as e:
                logger.error(f"JSON解析失败，响应内容: {response.text[:200]}")
                raise Exception(f'响应不是有效的JSON格式: {str(e)}')
            
            if data.get('err_no', -1) != 0:
                logger.error(f"获取签到状态失败: {data.get('err_msg', '未知错误')}")
                raise Exception('获取签到状态失败')
            status = data['data']
            logger.info(f"今日{'已' if status else '未'}签到")
            return status
        except requests.exceptions.RequestException as e:
            logger.error(f"获取签到状态请求异常: {str(e)}")
            raise
        except Exception as e:
            logger.error(f"获取签到状态异常: {str(e)}")
            raise
    
    def check_in(self) -> Dict:
        """签到"""
        logger.info("执行签到")
        url = 'https://api.juejin.cn/growth_api/v1/check_in'
        try:
            response = requests.post(url, headers=self.helper.headers, timeout=10)
            response.raise_for_status()
            
            # 检查响应内容
            if not response.text:
                raise Exception('响应内容为空')
            
            # 记录响应内容用于调试
            logger.debug(f"签到响应状态码: {response.status_code}")
            logger.debug(f"签到响应内容: {response.text[:500]}")
            
            try:
                data = response.json()
            except json.JSONDecodeError as e:
                logger.error(f"JSON解析失败，响应内容: {response.text[:200]}")
                logger.error(f"响应状态码: {response.status_code}")
                logger.error(f"响应头: {dict(response.headers)}")
                raise Exception(f'响应不是有效的JSON格式: {str(e)}')
            
            if data.get('err_no', -1) != 0:
                logger.error(f"签到失败: {data.get('err_msg', '未知错误')}, err_no: {data.get('err_no')}")
                raise Exception(f"签到失败: {data.get('err_msg', '未知错误')}")
            logger.info(f"签到成功，获得{data['data']['incr_point']}矿石")
            return data['data']
        except requests.exceptions.RequestException as e:
            logger.error(f"签到请求异常: {str(e)}")
            raise
        except Exception as e:
            logger.error(f"签到处理异常: {str(e)}")
            raise
    
    def get_counts(self) -> Dict:
        """获取签到统计"""
        logger.info("获取签到统计信息")
        url = 'https://api.juejin.cn/growth_api/v1/get_counts'
        try:
            response = requests.get(url, headers=self.helper.headers, timeout=10)
            response.raise_for_status()
            
            if not response.text:
                raise Exception('响应内容为空')
            
            try:
                data = response.json()
            except json.JSONDecodeError as e:
                logger.error(f"JSON解析失败，响应内容: {response.text[:200]}")
                raise Exception(f'响应不是有效的JSON格式: {str(e)}')
            
            if data.get('err_no', -1) != 0:
                logger.error(f"获取签到统计失败: {data.get('err_msg', '未知错误')}")
                raise Exception('获取签到统计失败')
            logger.info(f"获取签到统计成功")
            return data['data']
        except requests.exceptions.RequestException as e:
            logger.error(f"获取签到统计请求异常: {str(e)}")
            raise
        except Exception as e:
            logger.error(f"获取签到统计异常: {str(e)}")
            raise
    
    def get_current_point(self) -> int:
        """获取当前矿石数"""
        logger.info("获取当前矿石数")
        url = 'https://api.juejin.cn/growth_api/v1/get_cur_point'
        try:
            response = requests.get(url, headers=self.helper.headers, timeout=10)
            response.raise_for_status()
            
            if not response.text:
                raise Exception('响应内容为空')
            
            try:
                data = response.json()
            except json.JSONDecodeError as e:
                logger.error(f"JSON解析失败，响应内容: {response.text[:200]}")
                raise Exception(f'响应不是有效的JSON格式: {str(e)}')
            
            if data.get('err_no', -1) != 0:
                logger.error(f"获取当前矿石数失败: {data.get('err_msg', '未知错误')}")
                raise Exception('获取当前矿石数失败')
            point = data['data']
            logger.info(f"当前矿石数: {point}")
            return point
        except requests.exceptions.RequestException as e:
            logger.error(f"获取当前矿石数请求异常: {str(e)}")
            raise
        except Exception as e:
            logger.error(f"获取当前矿石数异常: {str(e)}")
            raise

class CheckIn:
    def __init__(self, cookie: str):
        self.cookie = cookie
        self.username = ''
        self.growth_task = None
        
    def run(self):
        helper = JuejinHelper()
        try:
            helper.login(self.cookie)
        except Exception as e:
            print(f'登录失败: {str(e)}')
            raise Exception('登录失败,请尝试更新Cookie!')
            
        self.username = helper.user['user_name']
        growth = Growth(helper)
        
        # 签到
        today_status = growth.get_today_status()
        if not today_status:
            check_in_result = growth.check_in()
            self.growth_task = {
                'status': 1,
                'incr_point': check_in_result['incr_point'],
                'sum_point': check_in_result['sum_point']
            }
        else:
            # 已签到时，获取当前矿石数
            current_point = growth.get_current_point()
            self.growth_task = {
                'status': 2,
                'sum_point': current_point
            }
            
        # 获取签到统计
        counts = growth.get_counts()
        self.growth_task.update({
            'cont_count': counts['cont_count'], 
            'sum_count': counts['sum_count']
        })
        
        return self.growth_task['status']
        
    def __str__(self):
        status_map = {
            0: '签到失败',
            1: f'签到成功 +{self.growth_task.get("incr_point", 0)} 矿石',
            2: '今日已完成签到'
        }
        
        # 获取状态消息
        status_msg = status_map[self.growth_task['status']]
        
        return f'''
掘友: {self.username}
{status_msg}
连续签到天数 {self.growth_task['cont_count']}
累计签到天数 {self.growth_task['sum_count']}
当前矿石数 {self.growth_task.get('sum_point', '未知')}
'''.strip()

def get_users_cookie(env_dict: Dict) -> List[str]:
    """从环境变量获取cookie列表"""
    cookies = []
    if env_dict.get('COOKIE'):
        cookies.append(env_dict['COOKIE'])
    for i in range(2, 6):
        cookie = env_dict.get(f'COOKIE_{i}')
        if cookie:
            cookies.append(cookie)
    return cookies

def random_sleep(min_seconds: int = 1, max_seconds: int = 5):
    """随机等待"""
    time.sleep(random.uniform(min_seconds, max_seconds))

def run():
    logger.info("开始执行签到任务")
    
    # 优先从环境变量获取配置（适用于GitHub Actions等CI环境）
    cookies = get_users_cookie(os.environ)
    
    # 如果环境变量中没有，则从配置文件读取
    if not cookies:
        try:
            helper = JuejinHelper()
            if helper.cookie:
                cookies = [helper.cookie]
        except Exception as e:
            logger.warning(f"从配置文件读取cookie失败: {str(e)}")
    
    if not cookies:
        logger.error("未找到任何cookie配置，请设置环境变量COOKIE或创建config.json文件")
        return
        
    logger.info(f"找到{len(cookies)}个用户配置")
    
    message_list = []
    for i, cookie in enumerate(cookies, 1):
        logger.info(f"开始处理第{i}个用户")
        checkin = CheckIn(cookie)
        random_sleep()  # 随机等待1-5秒
        
        try:
            checkin.run()
            content = str(checkin)
            logger.info(content)
            message_list.append(content)
        except Exception as e:
            logger.error(f"处理第{i}个用户时出错: {str(e)}")
            continue
    
    # 发送通知
    if message_list:
        message = '\n' + '-'*15 + '\n'.join(message_list)
        logger.info("所有任务执行完成，准备发送通知")
        # 这里需要实现通知发送逻辑
    else:
        logger.warning("没有成功执行的任务")
    
if __name__ == '__main__':
    try:
        run()
    except Exception as e:
        logger.error(f"程序执行出错: {str(e)}") 