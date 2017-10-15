# my-first-blog

Django Exam

17.10.12
http://127.0.0.1:8000/bookmarks/ 에 접속 에러가 나타남.
Template 설정에서 잘못된 부분이 있는 듯 한데, 어디서 설정을 수정해야 될지 모르겠음.
p.s> 장고걸스 예제에서 완성된 것에서 이어서 bookmarks 간단예제를 추가하는 것임.

에러난 부분은 mysite/urls.py 
> url(r'^blog', include('blog.urls')),
에서 url(r'', include('blog.urls')), 로 변경 (^blog를 삭제해야 정상적으로 나타난다.)
