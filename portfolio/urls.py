from django.urls import path

from portfolio import views

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("login/", views.login, name="login"),
    path("signup/", views.signup, name="signup"),
    path("adminpage/", views.adminpage, name="adminpage"),
    path("experiences/", views.experiences, name="experiences"),
    path("resumes/", views.resumes, name="resumes"),
    path(
        "internship_experience/",
        views.Internship_Experience,
        name="internship_experience",
    ),
    path("projects/", views.projects, name="projects"),
    path("favicon.ico/", views.favicon, name="favicon"),
    path("project_info/", views.project_info, name="project_info"),
    path(
        "internship_experience/",
        views.Internship_Experience,
        name="Internship_Experience",
    ),
    path("logout/", views.logout_view, name="logout"),
    path("resume_info/", views.resume_info, name="resume_info"),
]
