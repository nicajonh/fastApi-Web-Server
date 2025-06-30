# -*- coding:utf-8 -*-
from functools import wraps
from typing import Dict, Callable, Optional, Any
from datetime import datetime

def time_formatter(field_formats: Dict[str, str]):
    """
    时间格式化装饰器 (Pydantic V1 最佳兼容方案)
    field_formats: 字段名到格式字符串的映射
    例如: {'create_time': '%Y-%m-%d %H:%M:%S', 'birth_date': '%Y-%m-%d'}
    """
    def decorator(cls):
        # 保存时间格式配置
        cls._time_field_formats = field_formats
        
        # 重写 dict 方法进行时间格式化
        original_dict = getattr(cls, 'dict', None)
        
        def formatted_dict(self, **kwargs):
            # 获取原始数据
            if original_dict:
                result = original_dict(self, **kwargs) 
            else:
                result = super(cls, self).dict(**kwargs)
            
            # 应用时间格式化
            for field_name, format_str in getattr(self.__class__, '_time_field_formats', {}).items():
                if field_name in result and result[field_name] is not None:
                    value = result[field_name]
                    if isinstance(value, datetime):
                        result[field_name] = value.strftime(format_str)
            
            return result
        
        # 重写 json 方法
        def formatted_json(self, **kwargs):
            import json
            data = self.dict(**kwargs)
            return json.dumps(data, ensure_ascii=False, default=str)
        
        # 绑定方法到类
        cls.dict = formatted_dict
        cls.json = formatted_json
        
        # 确保有 Config 类
        if not hasattr(cls, 'Config'):
            class Config:
                pass
            cls.Config = Config
        
        return cls
    return decorator
