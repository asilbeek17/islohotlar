from django.urls import path

from app.views import *

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact_view, name='contact'),
    # path('category/', category, name='category'),
    path('project/', project, name='project'),

    path('sanoat_project/', sanoat_project, name='sanoat_project'),
    path('qishloq_project/', qishloq_project, name='qishloq_project'),
    path('xizmat_project/', xizmat_project, name='xizmat_project'),

    path('sort_1/', sort_1, name='sort_1'),
    path('sort_2/', sort_2, name='sort_2'),
    path('sort_3/', sort_3, name='sort_3'),
    path('sort_4/', sort_4, name='sort_4'),
    path('sort_5/', sort_5, name='sort_5'),
    path('sort_6/', sort_6, name='sort_6'),
    path('sort_7/', sort_7, name='sort_7'),
    path('sort_8/', sort_8, name='sort_8'),
]
