"""toturialApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from pages import views
from post.views import dynamic_lookup_view, post_delete_view, post_listItem_view

app_name = 'posts'
urlpatterns = [
    path('', post_listItem_view, name="post-lists"),
    # path('forms', post_create_view),

    # dynmaic routing. it renders a new page everytime the id of items in the database changes.
    path('dynamic/<int:my_id>/', dynamic_lookup_view, name="dynamic"),
    path('dyna/<int:my_id>/delete/', post_delete_view, name="post-delete"),


]
