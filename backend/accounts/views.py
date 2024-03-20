from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import permissions, status
from .serializers import UserSerializer
User = get_user_model()

class RegisterView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request):
        try: 
            data = request.data 

            name = data['name']
            email = data['email']
            password = data['password']
            re_password = data['re_password']
            is_seller = data['is_seller']

            if is_seller == 'True':
                is_seller = True 
            else: 
                is_seller = False 
            
            if password == re_password:
                if len(password) >= 8:
                    if not User.objects.filter(email=email).exists():
                        if not is_seller:
                            User.objects.create_user(email=email, name=name, password=password)
                            return Response(
                                {'success': 'User account created successfully'}
                            )
                        else: 
                            User.objects.create_seller(email=email, name=name, password=password)
                            return Response(
                                {'success': 'Seller account created successfully'}
                            )
                    else: 
                        return Response(
                            {'error': 'Email already exists'},
                            status=status.HTTP_400_BAD_REQUEST
                        )
                else: 
                    return Response(
                        {'error': 'Password must be at least 8 characters'},
                        status = status.HTTP_400_BAD_REQUEST
                    )
            else: 
                return Response(
                    {'error': 'Passwords do not match'},
                    status=status.HTTP_400_BAD_REQUEST
                )

        except Exception as e: 
            return Response(
                {'error': f"Something went wrong during creating account: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        

class RetrieveUserView(APIView):
    
    def get(self, request):
        try: 
            user = request.user
            user = UserSerializer(user)
            
            return Response(
                {'user': user.data},
                status=status.HTTP_200_OK
            )
        
        except Exception as e: 
            return Response(
                {'error': f'Something went wrong during Retrieving Account details: {str(e)}'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )