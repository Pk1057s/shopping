from django.shortcuts import render

def usersss(req):
    # tag 일괄 분류
    # TimeLine 기준
    # 빈도수 검색 
    # 추천모델
    pass

def shows(req):
    tag = usersss(req)
    return render(req, 'index.html', {'product' : tag})