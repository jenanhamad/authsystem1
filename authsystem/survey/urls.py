from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path("surveys/", views.survey_list, name="survey-list"),
    path("surveys/<int:pk>/", views.detail, name="survey-detail"),
    path("surveys/create/", views.create, name="survey-create"),
    path("surveys/<int:pk>/delete/", views.delete, name="survey-delete"),
    path("surveys/<int:pk>/edit/", views.edit, name="survey-edit"),
    path("surveys/<int:pk>/question/", views.question_create, name="survey-question-create"),
    path(
        "surveys/<int:survey_pk>/question/<int:question_pk>/option/",
        views.option_create,
        name="survey-option-create",
    ),
    path("surveys/<int:pk>/start/", views.start, name="survey-start"),
    path("surveys/<int:survey_pk>/submit/<int:sub_pk>/", views.submit, name="survey-submit"),
    path("surveys/<int:pk>/thanks/", views.thanks, name="survey-thanks"),

]
