from django.urls import include, path
from rest_framework import routers

from api.views import (
    CommentViewSet,
    FollowViewSet,
    GroupViewSet,
    PostViewSet,
)

app_name = 'api'

router_v1 = routers.DefaultRouter()
router_v1.register('posts', PostViewSet, basename='post')
router_v1.register('groups', GroupViewSet, basename='group')
router_v1.register('follow', FollowViewSet, basename='follow')
router_v1.register(
    'posts/(?P<post_id>\\d+)/comments',
    CommentViewSet, basename='comment'
)


urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/', include('djoser.urls.jwt')),
]
