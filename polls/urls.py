from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('hello/<name>', views.say_hello, name='hello'),
	path('goodbye/<name>', views.say_goodbye, name='goodbye'),
]