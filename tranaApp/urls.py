from django.urls import path
from .views import (
    signup,
    login_view,
    logout_view,
    usersDashboard,
    medicinesDashboard,
    reportsDashboard,
    reportCondition,
    orderMedicine,
    notify,
    resolve,
    page404,
    landing,
    getreport,
    getmedicine,
    reset_password,
    verify,
    details,
    pending,
    approved,
    statistics,

    motivation,
    about,
    services,
    faq,
    contact,
<<<<<<< HEAD
    team,
=======
    doctor,
    consult,
>>>>>>> 3b08ac32c33d8b3efb849ac3c58e178cf57a48b9
)

urlpatterns = [
    # path("", home, name="home"),
    path("signup/", signup, name="signup"),
    path("login/", login_view, name="login"),
    path("reset/", reset_password, name="reset"),
    path("logout/", logout_view, name="logout"),
    path("", landing, name="landing"),
    path("users/", usersDashboard, name="users"),
    path("reports/", reportsDashboard, name="reports"),
    path("medicines/", medicinesDashboard, name="medicines"),
    path("condition/", reportCondition, name="condition"),
    path("medicine/", orderMedicine, name="medicine"),
    path("notify/<str:id>", notify, name="notify"),
    path("resolve/<str:id>", resolve, name="resolve"),
    path("404/", page404, name="404"),
    path("getreport/", getreport, name="getreport"),
    path("getmedicine/", getmedicine, name="getmedicine"),
    path("verify/<str:uId>/<str:accepted>", verify, name="verify"),
    path("details/",details,name="details"),
    path('consult/',consult,name="consult"),
    path('doctor/',doctor,name="doctor"),
    path('pending/', pending, name="pending"),
    path('approved/',approved, name="approved"),
    path('statistics/',statistics,name="statistics"),

    # Static pages
    path("motivation/",motivation,name="motivation"),
    path("about/",about,name="about"),
    path("services/",services,name="services"),
    path("FAQ/",faq,name="faq"),
    path("contact/",contact,name="contact"),
    path("team/",team,name="team"),
]
