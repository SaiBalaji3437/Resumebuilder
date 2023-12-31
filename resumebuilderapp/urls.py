from django.urls import path
from . import views

urlpatterns = [
    path("", views.index_view, name="index"),
    path("tempsel/", views.tempsel_view, name="tempsel"),
    path("jobs/", views.jobs_view, name="jobs"),
    path("contact/", views.contact_view, name="contact"),
    path("JAI/", views.JAI_view, name="JAI"),
    path("JCA/", views.JCA_view, name="JCA"),
    path("JCSE/", views.JCSE_view, name="JCSE"),
    path("JDALST/", views.JDALST_view, name="JDALST"),
    path("companies/", views.companies_view, name="companies"),
    path("JDART/", views.JDART_view, name="JDART"),
    path("JDBA/", views.JDBA_view, name="JDBA"),
    path("JDS/", views.JDS_view, name="JDS"),
    path("JISA/", views.JISA_view, name="JISA"),
    path("JNSA/", views.JNSA_view, name="JNSA"),
    path("JSD/", views.JSD_view, name="JSD"),
    path("template1/", views.template1_view, name="template1"),
    path("template2/", views.template2_view, name="template2"),
    path("template3/", views.template3_view, name="template3"),
    path("formfinal/", views.formfinal_view, name="formfinal"),
    path("video/", views.video_view, name="video"),
    path("signup/", views.SignupPage, name="signup"),
    path("login/", views.LoginPage, name="login"),
    path("logout/", views.LogoutPage, name="logout"),
    path("profile/", views.profile, name="profile"),
    path("submit_form/", views.submit_form_view, name="submit_form"),
    path("view_entries/", views.view_contact_form_entries, name="view_entries"),
]
