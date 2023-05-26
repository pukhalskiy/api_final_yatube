from django.urls import path, include
from rest_framework import routers

from api.views import PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet


router = routers.DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'groups', GroupViewSet, basename='groups')
router.register('follow', FollowViewSet, basename='follow')
router.register(r'^posts/(?P<post_id>\d+)/comments',
                CommentViewSet, basename='comment')


urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls.jwt')),
]
