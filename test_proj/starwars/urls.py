from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from starwars.sith.views import (RecruterView, AnswerView, SithView,
                                 EnrollRecruterView, ChooseSithView,
                                 AllSithsView, SithsMore1View)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', TemplateView.as_view(template_name='index.html'), name='index'),
    path('recruter/', RecruterView.as_view(), name='recruter'),
    path('answer/<int:recruter_id>/', AnswerView.as_view(), name='answer'),
    path('choosesith/', ChooseSithView.as_view(), name='choosesith'),
    path('sith/', SithView.as_view(), name='sith'),
    path('allsiths/', AllSithsView.as_view(), name='allsiths'),
    path('sithsmore1/', SithsMore1View.as_view(), name='sithsmore1'),
    path('enroll/<int:recruter_id>/<int:sith_id>', EnrollRecruterView.as_view(),
         name='enroll'),
    path('counterror/', TemplateView.as_view(template_name='counterror.html'),
         name='counterror'),
]
