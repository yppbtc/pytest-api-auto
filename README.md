# pytest-api-auto

基于 pytest + Allure 的接口自动化测试框架，采用分层架构设计，支持数据驱动测试和接口间数据关联。

## 🛠 技术栈

- **框架**: pytest
- **报告**: Allure
- **HTTP请求**: requests
- **数据解析**: jsonpath
- **配置管理**: configparser
- **数据格式**: YAML

## 📁 项目结构

```
pythonproject/
├── base/              # 基础工具层
│   ├── apiutil.py     # 请求处理核心
│   └── apiutil_business.py  # 业务请求封装
├── common/            # 公共组件层
│   ├── sendrequest.py # HTTP请求封装
│   ├── assertions.py  # 断言验证
│   ├── readyaml.py    # YAML数据读写
│   └── recordlog.py   # 日志记录
├── conf/              # 配置层
│   ├── config.ini     # 环境配置
│   └── setting.py     # 项目配置
├── data/              # 测试数据层
│   └── loginName.yaml # 登录数据
├── testcase/          # 测试用例层
│   ├── conftest.py    # Fixture配置
│   ├── Single interface/  # 单接口测试
│   └── ProductManager/    # 业务场景测试
├── report/            # 测试报告
├── run.py             # 项目入口
├── pytest.ini         # pytest配置
└── requirements.txt   # 依赖清单
```

## 🚀 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 配置环境

修改 `conf/config.ini` 配置测试环境：

```ini
[api_envi]
host = http://your-api-host.com
```

### 3. 运行测试

```bash
# 运行所有测试
python run.py

# 生成 Allure 报告
allure serve ./report/temp
```

## 📝 测试用例编写

### 单接口测试

在 `testcase/Single interface/` 目录下创建 YAML 文件：

```yaml
- baseInfo:
    url: /api/user/query
    method: POST
    header:
      Content-Type: application/json
  testCase:
    - case_name: 查询用户成功
      data:
        user_id: ${get_extract_data(user_id)}
      extract:
        token: $.data.token
      validation:
        - eq:
            status_code: 200
        - contains:
            msg: 查询成功
```

### 业务场景测试

在 `testcase/ProductManager/` 目录下创建业务流程测试用例。

## 🔧 核心功能

### 1. 数据驱动测试
- 支持 YAML 文件管理测试数据
- 一条 YAML 数据对应一条测试用例

### 2. Fixture 机制
- **session 级别**: 自动登录，整个测试会话只执行一次
- **function 级别**: 每个测试函数的前后置操作

### 3. 变量替换
- 使用 `${get_extract_data(key)}` 引用之前提取的数据

### 4. 数据提取
- 从接口响应中提取数据保存到 `extract.yaml`
- 支持 JSONPath 语法

### 5. 断言类型
- `eq`: 相等断言
- `contains`: 包含断言
- `ne`: 不相等断言
- `rv`: 任意值断言
- `db`: 数据库断言

## 📊 测试报告

生成的 Allure 报告包含：
- 测试用例执行结果
- 接口请求/响应详情
- 测试执行时间
- 错误日志

## 📄 License

MIT License