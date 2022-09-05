from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_202_ACCEPTED, HTTP_204_NO_CONTENT
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ViewSet):
    def list(self, request):          # api/products/
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)              
        return Response(serializer.data)
    
    def create(self, request): # api/products/
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)

    def retrieve(self, request, pk = None): # api/products/{1} <str:id>
        product = Product.objects.get(id=pk)
        serializers = ProductSerializer(product)
        return Response(serializers.data)
 
    def update(self, request, pk = None): # api/products/{1} <str:id>
        product = Product.objects.get(id=pk) 
        serializers = ProductSerializer(instance=product, data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(serializers.data, status=HTTP_202_ACCEPTED)

    def delete(self, request, pk = None): # api/products/{1} <str:id>
        product = Product.objects.get(id=pk) 
        product.delete()
        return Response(status=HTTP_204_NO_CONTENT)