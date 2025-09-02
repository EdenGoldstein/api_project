
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import status, generics 
from .serializers import BookSerializer, AuthorSerializer
from .models import Book, Author
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token



#using APIVIEW(class-based view)
class AuthorListCreate(APIView):
    
    serializer_class = AuthorSerializer
    authentication_classes= [BasicAuthentication]
    permission_classes= [IsAuthenticatedOrReadOnly]
    
    def get(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)
    
    
    def post(self, request):
        print(request.data)
        
        serializer = AuthorSerializer(data=request.data)
        # Validate the data
        if serializer.is_valid():
            # Save the new author
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else: 
        # return validation errors
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class AuthorDetail(APIView):

    #Retrieve a single author by its id
    def get(self, request, pk=None):
        authors = Author.objects.all()
        author = get_object_or_404(authors, pk=pk)
        serializer = AuthorSerializer(author)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @permission_classes(IsAdminUser)    
    def delete(self, request, pk):
        try:
            author = Author.objects.get(pk=pk)
        except:
            return Response({"error": "author does not exist"}, status=status.HTTP_404_NOT_FOUND) 
        return Response(status=status.HTTP_204_NO_CONTENT)   
                    
        
        
class BookViewSet(ModelViewSet):

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    authentication_classes= [TokenAuthentication]
    permission_classes= [IsAuthenticated]
    
    # authentication_classes= [TokenAuthentication]
    # permission_classes= [IsAuthenticatedOrReadOnly]
    
    
    #gets all the books
    def list(self, request):
        serializer = BookSerializer(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    #Retrieve a single book by its id
    def retrieve(self, request, pk=None):
        book = get_object_or_404(self.queryset, pk=pk)
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request, *args, **kwargs):
        
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
    def perform_create(self, serializer):
        serializer.save()
    
    # @permission_classes(IsAdminUser)    
    def delete(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
        except:
            return Response({"error": "author does not exist"}, status=status.HTTP_404_NOT_FOUND)
            
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 