# URL 및 View

## 프로젝트 생성
### monthly_challenges 장고 프로젝트 생성
```
django-admin startproject monthly_challenges
```

### 또 다른 프로젝트 생성 challenges
```
python manage.py startapp challenges
``` 

### Main폴더의 urls.py에서 URL 설정
```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("challenges/", include("<폴더명>.urls"))
]
```

### 또 다른 프로젝트<challenges>에서 URL 설정
#### views.py에서 실행할 로직 작성
```
from django.shortcuts import render
from django.http import HttpResponse

def index(request): 
  return HttpResponse("This works!")
```

#### urls.py 파일을 생성 후 URL 설정
```
from django.urls import path
from . import views

urlpatterns = [
  path("january", views.index)
]
```

#### 프로젝트 폴더에서 실행 후 확인
```
python manage.py runserver
```
http://localhost:8000/challenges/january

## Param 기능 사용
### <param> 을 사용하여 Django에서 param 기능 구현 (urls.py)
```
urlpatterns = [
    path("<month>", views.monthly_challenges)
]
```
### URL에 입력된 값을 기반으로 로직 출력
```
...
from django.http import HttpResponse, HttpResponseNotFound
...

def monthly_challenges(request, month):
  challenge_text = None
  if month == 'january':
    challenge_text = "Eat no meat for the entire month!!"
  elif month == "fabruary":
    challenge_text = "Walk for at least 20 minutes every day!"
  elif month == "march":
    challenge_text = "Learn Django for at least 20 minutes every day!"
  else:
    return HttpResponseNotFound("This month is not supported!")
  
  return HttpResponse(challenge_text)
```

## Param 타입 지정
### Param에 입력될 타입을 지정할 수 있다.
```
urlpatterns = [
    path("<int:month>", views.monthly_challenges_by_number), # int 값
    path("<str:month>", views.monthly_challenges) # string 값
]
```

## URL 패턴에서 동적으로 인자 받기
### URL 패턴에 이름 부여
#### urls.py (name을 통해 URL 패턴에 이름부여)
```
path("<str:month>", views.monthly_challenge, name="month-challenge")
```
#### views.py (URL 패턴에 이름 가져오기)
```
redirect_path = reverse("month-challenge")
```
#### views.py (URL 패턴에 Param 가져오기)
```
redirect_path = reverse("month-challenge", args=[redirect_month])
```

## Django에서 Html 코드 반환
```
response_data = f"<h1>{challenge_text}</h1>"
return HttpResponse(response_data)
```
