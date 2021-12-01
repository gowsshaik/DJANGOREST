from django.contrib import admin
from django.urls import path
# from .views import createdet,updatedyn,exp,display
# from .views import DetView,detUpd
from .views import DetGen


urlpatterns = [
    # path('create/',createdet),
    # path('upd/<int:pk>/',updatedyn),
    # path('exp',exp),
    # path('disp',display)
    # path('det',DetView.as_view()),
    # path('upd/<int:id>/',detUpd.as_view())
    path('detgen',DetGen.as_view()),
    path('detgen/<int:id>/',DetGen.as_view())
]