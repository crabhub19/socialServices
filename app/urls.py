from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="index"),
    path('signup',views.signup,name="signup"),
    path('worker/<str:name>',views.worker,name="worker"),
    path('profile',views.profile,name="profile"),
    path('userlogin',views.userlogin,name="userlogin"),
    path('userlogout',views.userlogout,name="userlogout"),
    path('profile',views.profile,name="profile"),
    path('delete_account/<str:username>', views.delete_account, name='delete_account'),
    path('active_account/<str:username>', views.active_account, name='active_account'),
    path('deactive_account/<str:username>', views.deactive_account, name='deactive_account'),
    path('update_contract_user',views.update_contract_user,name="update_contract_user"),
    path('update_userImage_user',views.update_userImage_user,name="update_userImage_user"),
    path('change_password',views.change_password,name="change_password"),

    # path('student/<str:dept>',views.student,name="student"),

]