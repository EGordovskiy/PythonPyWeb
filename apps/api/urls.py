from django.urls import path
from .views import AuthorAPIView, AuthorGenericAPIView, AuthorViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

app_name = 'api'

urlpatterns = [
    path('authors/', AuthorAPIView.as_view(), name='author-list'),
    path('authors_viewset/', AuthorViewSet.as_view({'get': 'list'}), name='author-viewset'),
    path('authors_viewset/<int:pk>', AuthorViewSet.as_view({'get': 'list'}), name='author-viewset-detail'),
    path('authors/<int:pk>/', AuthorAPIView.as_view(), name='author-detail'),
    path('authors_generic/', AuthorGenericAPIView.as_view(), name='author-generic-list'),
    path('authors_generic/<int:pk>/', AuthorGenericAPIView.as_view(), name='author-generic-detail'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

