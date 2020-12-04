from django.urls import path

from user import views


app_name = "user"

urlpatterns = [
  # 1: url_path, 2: view to direct to, 3: reverse name (url name)
  path("create/", views.CreateUserView.as_view(), name="create"),
  path("token/", views.CreateTokenView.as_view(), name="token")
]
