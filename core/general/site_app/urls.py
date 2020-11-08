from django.urls import path
from .views import collection_list, collection_detail, CollectionAPIView, CollectionDetails

urlpatterns = [
    path('', CollectionAPIView.as_view()),
    path('<int:id>/', CollectionDetails.as_view()),
]