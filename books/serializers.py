from rest_framework import serializers
from .models import Book, Author
from datetime import date, datetime


class AuthorSerializer(serializers.Serializer):
    
    author_id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    date_of_birth = serializers.CharField()
    nationality = serializers.CharField()

    def validate_date_of_birth(self, value):
        #check that Author's date of birth is before 2015-1-1 (field validator)
        max_date = date(2015, 1, 1)
        format_string = "%Y-%m-%d"
        date_value = datetime.strptime(value, format_string).date()
        
        if date_value > max_date:
         raise serializers.ValidationError({"date_of_birth":"author's date of birth must be before January 1, 2015"})
        return value
        
    def create(self, validated_data: dict): 
        
        format_string = "%Y-%m-%d"
        date_value = datetime.strptime(validated_data['date_of_birth'], format_string).date()
        
        instance = Author.objects.create(name=validated_data["name"], date_of_birth=date_value, nationality=validated_data["nationality"])
        return instance
    
      

class BookSerializer(serializers.ModelSerializer):     
    class Meta:
        model=Book
        fields = ['id', 'title', 'description', 'pages', 'rating', 'genre', 'author', 'publised_date']
        
    def validate(self, data):
        if data['genre']  == 'ROM' and data['pages'] < 50:
            raise serializers.ValidationError({
                "pages": "Romances must have at least 50 pages"
            })
        return data
    


# To Do:
# Decide which endpoints will be public vs protected.(with Permissions)

# Basic Authentication for initial testing.
# Token Authentication for real-world API usage.- to add 
# Secure sensitive endpoints so only authenticated users can access them. -only admin?
# . Authorization & Role-Based Access
# Use DRF’s permissions system to restrict certain actions (e.g., only Admin can delete, Regular User can only read/write their own objects).
# Protect routes accordingly.


# about users:

# https://codesignal.com/learn/courses/user-authentication-and-permissions-in-drf/lessons/implementing-sign-in-and-sign-up-in-django-api
# # users?:
#     password = serializers.CharField(write_only=True) 
#     confirm_password = serializers.CharField(write_only=True)

#     class Meta:
#         model = User
#         fields = ['username', 'password']

#     def validate(self, data):  
#         if data['password'] != data['confirm_password']: 
#             raise serializers.ValidationError( "Passwords do not match.")

#         return data