# -*- coding:utf-8 -*-
"""
@Time : 2025/6/30
@Auth : nicajonh
@Des : 响应模型
"""
from pydantic import BaseModel
from typing import TypeVar, Generic,Optional

T = TypeVar('T') # TypeVar for generic response

class GenericResponse(BaseModel, Generic[T]):
    """通用响应模型"""
    code: int 
    message: str 
    data: Optional[T] = None  # 可选字段，数据可以是任意类型
    total: Optional[int]  # 可选字段，用于分页等场景
    @classmethod
    def success(cls, data: T = None, message: str = "success")-> 'GenericResponse[T]':
        """成功响应"""
        return cls(code=200, message=message, data=data)

    @classmethod
    def fail(cls, message: str = "fail", code: int = 400)-> 'GenericResponse[T]':
        """失败响应"""
        return cls(code=code, message=message, data=None)

    @classmethod
    def res_antd(cls, data: T = None, total: int = 0)-> 'GenericResponse[T]':
        """Ant Design Table格式响应"""
        if data is None:
            data = []
        return cls(code=200, message="success", data=data, total=total)

