from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RegisterSerializers
from .models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import check_password
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken, OutstandingToken


class RegisterView(APIView):
    def post(self,request):
        serializers = RegisterSerializers(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({'message':"User Successfully Created"})
        print(serializers.errors)
        return Response(serializers.errors, status = 400)

class LoginView(APIView):
    def post(self,request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        try:
            user = User.objects.get(username = username)
        except User.DoesNotExist:
            return Response({'error':"Username of Password might be incorrect"},status = 400)
        
        if not check_password(password,user.password):
            return Response({'error':'Username or Password might be incorrect'},status = 400)
        
        refresh = RefreshToken.for_user(user)

        response = Response({"message":"User successfully logged in."})
        response.set_cookie(key = 'refresh',value = str(refresh),httponly = True)
        response.set_cookie(key="access",value=str(refresh.access_token),httponly = True)

        return response

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self,request):
        try:
            tokens = OutstandingToken.objects.filter(user=request.user)

            for token in tokens:
                BlacklistedToken.objects.get_or_create(token = token)

            return Response({"message":"User successfully logged out"},status=200)
        except Exception as e:
            return Response({"error":str(e)},status = 400)

