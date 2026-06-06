import shutil
import pytest
import os
import webbrowser
from conf.setting import REPORT_TYPE

# - Python 会 先执行整个 conf/setting.py 文件
# - 执行完后，只把 REPORT_TYPE 这个变量导入到当前作用域
# - 其他变量（如 LOG_LEVEL 、 API_TIMEOUT ）虽然也执行了，但 不会导入到当前作用域

if __name__ == '__main__':

    if REPORT_TYPE == 'allure':
        pytest.main(
            ['-s', '-v', '--alluredir=./report/temp', './testcase', '--clean-alluredir',
             '--junitxml=./report/results.xml'])

        shutil.copy('./environment.xml', './report/temp')
        os.system(f'allure serve ./report/temp')

    elif REPORT_TYPE == 'tm':
        pytest.main(['-vs', '--pytest-tmreport-name=testReport.html', '--pytest-tmreport-path=./report/tmreport'])
        webbrowser.open_new_tab(os.getcwd() + '/report/tmreport/testReport.html')

# 当面试官问你"为什么两种报告的启动方式不同？"，你可以这样回答：
# "Allure 报告是一个动态的 Web 服务，需要通过 allure serve 命令启动本地服务器来渲染报告；
# 而 TM 报告是静态 HTML 文件，测试执行完成后直接生成，可以用 webbrowser 模块直接打开。
# 这两种方式都是为了让用户方便地查看测试报告，只是技术实现方式不同。"
