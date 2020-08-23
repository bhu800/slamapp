from django.urls import path
from dashboard import views

from .views import *

#template tagging
app_name = 'myapp'

urlpatterns = [

    path('', HomePageView, name='home'),
    path('dashboard', dashboardPageView, name="dashboard"),
    path('base', basePageView, name="base"),
    path('user', userPageView, name="user"),
    path('showSlambooks_all', showSlambooksAll.as_view(), name="showSlambooks_all"),
    path('showSlambooks_my', showSlambooksMyListView.as_view(), name="showSlambooks_my"),
    path('showentry/<int:pk>', showSlambookMyDetailView.as_view(), name="showentry"),
    path('fillSlambook/<int:pk>', fillSlambook_PageView, name='fillSlambook'),
    # path('accounts/login/',HomePageView), #                                             <--- This is removed temporarily for development purpose!
    path('letter', letterPageView, name="letter"),
    path("hiddenAdmin", hiddenAdminPageView, name="hiddenAdmin"),
]