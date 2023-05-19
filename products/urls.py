from django.urls import path, include
from .views import product_jeans
from rest_framework import routers

router=routers.SimpleRouter()
router.register(r'jeans', product_jeans)
urlpatterns = router.urls