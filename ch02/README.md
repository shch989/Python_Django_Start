# 템플릿 및 정적 파일
## 템플릿 폴더 등록 
### 메인폴더에서 템플릿 폴더 위치 등록 (settings.py)
```
"DIRS": [
  BASE_DIR / "<프로젝트 폴더명>" / "<템플릿 폴더명>"
],
```
```
"DIRS": [
  BASE_DIR / "challenges" / "templates"
],
```
### 자동으로 템플릿 폴더를 인식하도록 설정 (settings.py)
```
INSTALLED_APPS = [
    '<프로젝트 폴더명>',
    ...
]
```
```
INSTALLED_APPS = [
    'challenges',
    ...
]
```

### 템플릿 파일 반환 (render_to_string)
#### 등록된 템플릿 폴더 위치에서 challenges/challenge.html 경로의 html 파일 반환
```
...
from django.template.loader import render_to_string
...

response_data = render_to_string("challenges/challenge.html")
return HttpResponse(response_data)
```

### 템플릿 파일 반환 (render)
```
return render(request, "challenges/challenge.html")
```

## 템플릿 데이터 전송
### views.py 에서 데이터 전송
```
return render(request, "challenges/challenge.html", {
    "text": challenge_text
})
```
### challenge.html 에서 데이터 받기
```
<body>
  <h1>This Month's Challenge</h1>
  <h2>{{ text }}</h2>
</body>
```