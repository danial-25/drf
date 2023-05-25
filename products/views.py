from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from django.http import Http404
from rest_framework import status,viewsets
from rest_framework import permissions
from rest_framework import generics
from .models import products
from django.core.serializers import serialize   
from .serializers import productsSerializer
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.decorators import api_view, renderer_classes,permission_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.reverse import reverse,reverse_lazy
# class product(viewsets.ModelViewSet):
#     queryset=products.objects.all()
#     serializer_class=productsSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]

#     def single(self, request,id=None):
#         p=get_object_or_404(self.queryset, pk=id)
#         serializer=productsSerializer(p)
#         return Response(serializer.data)


@api_view()
@permission_classes([IsAuthenticatedOrReadOnly])
def list(request, category):
    queryset=products.objects.all().filter(category=category)
    serializer = productsSerializer(queryset, many=True, context={'request': request})
    # api_root=reverse_lazy('products-detail', request=request)    
    return Response(serializer.data)
@api_view()
@permission_classes([IsAuthenticatedOrReadOnly])
def single(request, category,id):
    if(products.objects.filter(category=category).exists()):
        queryset=products.objects.get(id=id)
        serializer = productsSerializer(queryset, context={'request': request})
        return Response(serializer.data)
    raise Http404("Object not found")
# class product_jeans(viewsets.ModelViewSet):
#     queryset=products.objects.all().filter(category='jeans')
#     serializer_class=productsSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#     lookup_field='id'
#     def list(self, request):#still needs to be worked on
#         # scrape_and_create_objects()
#         queryset = products.objects.all()
#         serializer = productsSerializer(queryset, many=True, context={'request': request})
#         return Response(serializer.data)
    
#     def single(self, request,*args, **kwargs):
#         p=get_object_or_404(self.queryset)
#         serializer=productsSerializer(p)
#         return Response(serializer.data)










# from .models import Todo
# from .serializers import TodoSerializer

# class TodoListApiView(APIView):
#     # add permission to check if user is authenticated
#     permission_classes = [permissions.IsAuthenticated]

#     # 1. List all
#     def get(self, request, *args, **kwargs):
#         '''
#         List all the todo items for given requested user
#         '''
#         todos = Todo.objects.filter(user = request.user.id)
#         serializer = TodoSerializer(todos, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     # 2. Create
#     def post(self, request, *args, **kwargs):
#         '''
#         Create the Todo with given todo data
#         '''
#         data = {
#             'task': request.data.get('task'), 
#             'completed': request.data.get('completed'), 
#             'user': request.user.id
#         }
#         serializer = TodoSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)