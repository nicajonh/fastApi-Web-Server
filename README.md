# FastAPI脚手架


## 项目介绍

> 实现用权限某块，微信授权登录，JWT登录，日志模块等，计划开发中,



## 项目结构

```
├── app
│   ├── __init__.py
│   ├── api
│   │   ├── __init__.py
│   │   ├── v1
│   │   │   ├── __init__.py
│   │   │   ├── user.py
│   │   │   ├── user_router.py
│   │   │   └── user_service.py
│   │   └── v2
│   │       ├── __init__.py
│   │       ├── user.py
│   │       ├── user_router.py
│   │       └── user_service.py
│   ├── config
│   │   ├── __init__.py
│   │   ├── config.py
│   │   └── settings.py
│   ├── core
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── exceptions.py
│   │   ├── middlewares.py
│   │   └── security.py
│   ├── extensions
│   │   ├── __init__.py
│   │   ├── db.py
│   │   ├── logger.py
│   │   └── redis.py
│   ├── models
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── user.py
│   └── schemas
│       ├── __init__.py
│       ├── user.py
│       └── user_schema.py
├── .gitignore
├── README.md
├── requirements.txt
└── app.py
```

## 项目启动
要求：python > 3.10+
```bash
# 安装依赖
pip install -r requirements.txt

# 启动项目
uvicorn main:app --reload --host 0.0.0.0 --port 8000
或者直接运行 python app.py
```
