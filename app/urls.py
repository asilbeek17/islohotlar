from django.urls import path
from app.views import *

urlpatterns = [
    path('', index, name='index'),
    path('ru/', index_ru, name='index_ru'),
    path('en/', index_en, name='index_en'),

    path('contact/', contact_view, name='contact'),

    path('uz/project/', project_uz, name='project_uz'),
    path('ru/project/', project_ru, name='project_ru'),
    path('en/project/', project_en, name='project_en'),

    path('uz/sanoat_project/', sanoat_project_uz, name='sanoat_project_uz'),
    path('uz/qishloq_project/', qishloq_project_uz, name='qishloq_project_uz'),
    path('uz/xizmat_project/', xizmat_project_uz, name='xizmat_project_uz'),

    path('ru/sanoat_project/', sanoat_project_ru, name='sanoat_project_ru'),
    path('ru/qishloq_project/', qishloq_project_ru, name='qishloq_project_ru'),
    path('ru/xizmat_project/', xizmat_project_ru, name='xizmat_project_ru'),

    path('en/sanoat_project/', sanoat_project_en, name='sanoat_project_en'),
    path('en/qishloq_project/', qishloq_project_en, name='qishloq_project_en'),
    path('en/xizmat_project/', xizmat_project_en, name='xizmat_project_en'),

    path('uz/sort_1/', sort_1_uz, name='sort_1_uz'),
    path('uz/sort_2/', sort_2_uz, name='sort_2_uz'),
    path('uz/sort_3/', sort_3_uz, name='sort_3_uz'),
    path('uz/sort_4/', sort_4_uz, name='sort_4_uz'),
    path('uz/sort_5/', sort_5_uz, name='sort_5_uz'),
    path('uz/sort_6/', sort_6_uz, name='sort_6_uz'),
    path('uz/sort_7/', sort_7_uz, name='sort_7_uz'),
    path('uz/sort_8/', sort_8_uz, name='sort_8_uz'),

    path('ru/sort_1/', sort_1_ru, name='sort_1_ru'),
    path('ru/sort_2/', sort_2_ru, name='sort_2_ru'),
    path('ru/sort_3/', sort_3_ru, name='sort_3_ru'),
    path('ru/sort_4/', sort_4_ru, name='sort_4_ru'),
    path('ru/sort_5/', sort_5_ru, name='sort_5_ru'),
    path('ru/sort_6/', sort_6_ru, name='sort_6_ru'),
    path('ru/sort_7/', sort_7_ru, name='sort_7_ru'),
    path('ru/sort_8/', sort_8_ru, name='sort_8_ru'),

    path('en/sort_1/', sort_1_en, name='sort_1_en'),
    path('en/sort_2/', sort_2_en, name='sort_2_en'),
    path('en/sort_3/', sort_3_en, name='sort_3_en'),
    path('en/sort_4/', sort_4_en, name='sort_4_en'),
    path('en/sort_5/', sort_5_en, name='sort_5_en'),
    path('en/sort_6/', sort_6_en, name='sort_6_en'),
    path('en/sort_7/', sort_7_en, name='sort_7_en'),
    path('en/sort_8/', sort_8_en, name='sort_8_en'),
]
