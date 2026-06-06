import allure
import pytest

from common.readyaml import get_testcase_yaml
from base.apiutil import RequestBase
from base.generateId import m_id, c_id

# 这部分是单接口测试，主要测试用户管理模块的增删改查功能。
# 测试主体文件是 test_debug_api.py ，通过读取不同的 YAML 文件来测试不同的接口功能。
# 核心技术是使用 pytest 的 @pytest.mark.parametrize 装饰器实现数据驱动测试，测试数据和代码分离。
# 每条 YAML 数据对应一条测试用例，在测试函数中调用 RequestBase().specification_yaml() 发送请求并验证结果。

@allure.feature(next(m_id) + '用户管理模块（单接口）')
class TestUserManager:

    # 场景，allure报告的目录结构
    @allure.story(next(c_id) + "新增用户")
    # 测试用例执行顺序设置
    @pytest.mark.run(order=1)
    # 参数化，yaml数据驱动
    @pytest.mark.parametrize('base_info,testcase', get_testcase_yaml("./testcase/Single interface/addUser.yaml"))
    # get_testcase_yaml，将 YAML 文件中的测试数据转换为 pytest 参数化所需的格式。
    # 一个 baseInfo 对应多个 testCase ，最终返回一个列表，每个元素是 [baseInfo, testCase] 的组合。
    def test_add_user(self, base_info, testcase):
        allure.dynamic.title(testcase['case_name'])
        RequestBase().specification_yaml(base_info, testcase)

    @allure.story(next(c_id) + "修改用户")
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize('base_info,testcase', get_testcase_yaml("./testcase/Single interface/updateUser.yaml"))
    def test_update_user(self, base_info, testcase):
        allure.dynamic.title(testcase['case_name'])
        RequestBase().specification_yaml(base_info, testcase)

    @allure.story(next(c_id) + "删除用户")
    @pytest.mark.run(order=3)
    @pytest.mark.parametrize('base_info,testcase', get_testcase_yaml("./testcase/Single interface/deleteUser.yaml"))
    def test_delete_user(self, base_info, testcase):
        allure.dynamic.title(testcase['case_name'])
        RequestBase().specification_yaml(base_info, testcase)

    @allure.story(next(c_id) + "查询用户")
    @pytest.mark.run(order=4)
    @pytest.mark.parametrize('base_info,testcase', get_testcase_yaml("./testcase/Single interface/queryUser.yaml"))
    def test_query_user(self, base_info, testcase):
        allure.dynamic.title(testcase['case_name'])
        RequestBase().specification_yaml(base_info, testcase)
