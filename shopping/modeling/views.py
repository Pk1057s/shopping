from django.shortcuts import render
from product.models import SearchData
from datetime import datetime, timedelta
from django.db.models import Count

def extract(id, days = None, topToSearch = None):
    search_days = 30 if days is None else days
    top = 5 if topToSearch is None else topToSearch

    # tag 일괄 분류
    if SearchData.objects.filter(user_id = id).exists():
        current_date = datetime.now()
        serach_date_ago = current_date - timedelta(days=search_days)

        # 현재에서 기간 이내의 데이터 필터링
        filtered_tag = SearchData.objects.filter(user_id = id, value__gte=serach_date_ago, value__lte=current_date)

        # tag를 그룹화하고 빈도수 계산
        tag_count_list = filtered_tag.values('tag').annotate(tag_count=Count('tag'))

        # 빈도수를 기준으로 내림차순으로 정렬
        sorted_tags = sorted(tag_count_list, key=lambda x: x['tag_count'], reverse=True)

        # 상위 5개의 name 값 추출
        top_tags = [tag['tag'] for tag in sorted_tags[:top]]
        return top_tags
    else:
        print("error")
    # TimeLine 기준
    # 빈도수 검색 
    # 추천모델
        
def render_extracted_tag(req):
    id = req.session.get('user_id')
    days = req.session.get('days')
    topToSearch = req.session.get('topToSearch')
    extracted_tag = extract(id, days, topToSearch)
    return render(req, "index.html", {"extracted_tag":extracted_tag})
