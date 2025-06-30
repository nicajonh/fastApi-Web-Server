# -*- coding:utf-8 -*-
"""
@Created on : 2022/4/22 22:02
@Author: binkuolo
@Des: 中间件
"""

from log import logger
import time
from starlette.datastructures import MutableHeaders
from starlette.types import ASGIApp, Receive, Scope, Send, Message
from fastapi import Request,Response
from core.Utils import random_str
from starlette.middleware.base import BaseHTTPMiddleware
import json


class BaseMiddleware:
    """
    Middleware
    """

    def __init__(
            self,
            app: ASGIApp,
    ) -> None:
        self.app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        if scope["type"] not in ("http", "websocket"):  # pragma: no cover
            await self.app(scope, receive, send)
            return
        start_time = time.time()
        req = Request(scope, receive, send)
        if not req.session.get("session"):
            req.session.setdefault("session", random_str())

        async def send_wrapper(message: Message) -> None:
            process_time = time.time() - start_time
            if message["type"] == "http.response.start":
                headers = MutableHeaders(scope=message)
                headers.append("X-Process-Time", str(process_time))
            await send(message)
        await self.app(scope, receive, send_wrapper)


class ExcludeNoneMiddleware(BaseHTTPMiddleware):
    """全局排除None字段的中间件"""
    async def dispatch(self, request: Request, call_next) -> None:
        response = await call_next(request)
        # 只处理JSON响应
        if response.headers.get("content-type") == "application/json":
            # 获取响应体
            body = b""
            async for chunk in response.body_iterator:
                body += chunk  
            # 解析并重新编码，排除None值
            try:
                data = json.loads(body)
                clean_data = self._remove_none_values(data)
                new_body = json.dumps(clean_data, ensure_ascii=False)
                new_headers = dict(response.headers) # 移除原有的Content-Length
                new_headers.pop("content-length", None)
                return Response(
                    content=new_body,
                    status_code=response.status_code,
                    headers=new_headers,
                    media_type="application/json"
                )
            except Exception as e:
                # 如果处理失败，返回原响应
                logger.error(f"ExcludeNoneMiddleware processing response Error: {e}")
                return response
                    
        return response
    
    def _remove_none_values(self, obj):
        """递归移除None值"""
        if isinstance(obj, dict):
            return {k: self._remove_none_values(v) for k, v in obj.items() if v is not None}
        elif isinstance(obj, list):
            return [self._remove_none_values(item) for item in obj]
        else:
            return obj
