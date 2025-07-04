# -*- coding:utf-8 -*-
"""
@Time : 2022/4/27 5:29 PM
@Author: binkuolo
@Des: schemas模型
"""
from datetime import datetime
from pydantic import Field, BaseModel, validator
from typing import Optional, List
from schemas.base import BaseResp, ResAntTable
from core.Decorator import time_formatter


class CreateUser(BaseModel):
    username: str = Field(min_length=3, max_length=10)
    password: str = Field(min_length=6, max_length=12)
    user_phone: Optional[str] = Field(regex="^1[34567890]\\d{9}$")
    user_status: Optional[bool]
    remarks: Optional[str]
    roles: Optional[List[int]]


class UpdateUser(BaseModel):
    id: int
    username: Optional[str] = Field(min_length=3, max_length=10)
    password: Optional[str] = Field(min_length=6, max_length=12)
    user_phone: Optional[str] = Field(regex="^1[34567890]\\d{9}$")
    user_status: Optional[bool]
    remarks: Optional[str]


class SetRole(BaseModel):
    user_id: int
    roles: Optional[List[int]] = Field(default=[], description="角色")


class AccountLogin(BaseModel):
    username: Optional[str] = Field(min_length=3, max_length=10, description="用户名")
    password: Optional[str] = Field(min_length=6, max_length=12, description="密码")
    mobile: Optional[str] = Field(regex="^1[34567890]\\d{9}$", description="手机号")
    captcha: Optional[str] = Field(min_length=6, max_length=6, description="6位验证码")


class ModifyMobile(BaseModel):
    mobile: str = Field(regex="^1[34567890]\\d{9}$", description="手机号")
    captcha: str = Field(min_length=6, max_length=6, description="6位验证码")


class UserInfo(BaseModel):
    username: str
    age: Optional[int]
    user_type: bool
    nickname: Optional[str]
    user_phone: Optional[str]
    user_email: Optional[str]
    full_name: Optional[str]
    scopes: Optional[List[str]]
    user_status: bool
    header_img: Optional[str]
    sex: int
    


@time_formatter({
    'create_time': '%Y-%m-%d %H:%M:%S',
    'update_time': '%Y-%m-%d %H:%M:%S'
})
class UserListItem(BaseModel):
    key: int
    id: int
    username: str
    age: Optional[int]
    user_type: bool
    nickname: Optional[str]
    user_phone: Optional[str]
    user_email: Optional[str]
    full_name: Optional[str]
    user_status: bool
    header_img: Optional[str]
    sex: int
    remarks: Optional[str]
    create_time: datetime
    update_time: datetime
    

class CurrentUser(BaseResp):
    data: UserInfo


class AccessToken(BaseModel):
    token: Optional[str]
    expires_in: Optional[int]


class UserLogin(BaseResp):
    data: AccessToken


class UserListData(ResAntTable):
    data: List[UserListItem]


class UpdateUserInfo(BaseModel):
    nickname: Optional[str]
    user_email: Optional[str] = Field(regex="^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$",description="邮箱")
    header_img: Optional[str]
    user_phone: Optional[str] = Field(regex="^1[34567890]\\d{9}$", description="手机号")
    password: Optional[str] = Field(min_length=6, max_length=12, description="密码")

    @validator('*')
    def blank_strings(cls, v):
        if v == "":
            return None
        return v
