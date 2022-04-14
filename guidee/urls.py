from django.urls import path, include

from .views import gdlst, gdprofile

urlpatterns=[
    path('<str:field>/guidelist',gdlst, name='gdlst'),
    path('guidecontactlist',gdlst, name="gdcontactlst"),
    path('<str:field>/<str:guide>', gdprofile, name='gdprofile'),
]