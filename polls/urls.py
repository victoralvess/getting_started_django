from django.urls import path

from . import views
# 'app_name' is used to distinguish different app templates in the project
app_name = 'polls'
# The 'name' value will be used by the {% url %} template tag
urlpatterns = [
	path('', views.index, name='index'),
	path('hello/<name>', views.say_hello, name='hello'),
	path('goodbye/<name>', views.say_goodbye, name='goodbye'),
	path('<int:question_id>/', views.detail, name='detail'),
	path('<int:question_id>/results/', views.results, name='results'),
	path('<int:question_id>/vote/', views.vote, name='vote'),
]