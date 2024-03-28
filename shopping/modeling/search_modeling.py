from django.shortcuts import render, HttpResponse, redirect
from accounts.models import User
from product.models import Product,Tag
from datetime import datetime
import pytz

#tag 저장
def user_tag(req,res):
    if Tag.objects.filter(user_id = res).exists():
        tag = Tag.objects.filter(user_id = req) 
        Tag.objects.create(tag = req, user_id = res, create_at = datetime.now(pytz.timezone('Asia/Seoul')))
def usersss():
    # tag 일괄 분류
    # TimeLine 기준
    # 빈도수 검색 
    # 추천모델
    pass