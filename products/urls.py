from django.urls import path, include
from .views import list,single,sorted_list
from rest_framework import routers

# router=routers.SimpleRouter()
# router.register(r'jeans', product_jeans)
# urlpatterns = router.urls
urlpatterns = [
    path('<str:category>/', list),
    path('<str:category>/<str:sort_by>/', sorted_list),
    path('<str:category>/<int:id>/', single, name='products-detail'),
    # Other URL patterns...
]