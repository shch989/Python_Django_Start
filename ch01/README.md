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
