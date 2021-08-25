from django.urls import path 
from django.conf import settings
from django.conf.urls.static import static

from .views import *
app_name = 'polls'
urlpatterns = [
   path('',IndexView.as_view(),name='index'),
   path('<int:pk>/',DetailView.as_view(),name='detail'),
   path('<int:pk>/results/',ResultView.as_view(),name='results'),
   path('<int:question_id>/vote/',vote,name='vote'),
   path('signup/',signup,name='signup'),
   path('login/',login,name='login'),
   path('logout/',logout_view,name='logout')

]

if settings.DEBUG:
        urlpatterns + static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)


'''
from .views import index,detail,results,vote
urlpatterns = [
   path('',index,name='index'),
   path('<int:question_id>/',detail,name='detail'),
   path('<int:question_id>/results/',results,name='results'),
   path('<int:question_id>/vote/',vote,name='vote')

]
'''
