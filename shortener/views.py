from django.shortcuts import redirect, render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny
from .serializers import ShortURLSerializer
from .models import ShortURL


class CreateShortURLView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        user = request.user
        original_url = request.data.get('original_url')

        serializer = ShortURLSerializer(data = request.data,context = {'request':request})

        if serializer.is_valid():
            short_url = serializer.save()
            return Response({
                "short_url":short_url.short_code,
                "original_url":short_url.original_url,
                "message":"Short URL created successfully"
                })
        return Response(serializer.errors,status = 400)

class RedirectView(APIView):
    permission_classes = [AllowAny]

    def get(self,request,short_code):
        short_obj = ShortURL.objects.filter(short_code=short_code).first()
        if not short_obj:
            return Response({
                "error":"Short URL does not exist"
            }, status=404)
        short_obj.click_count += 1
        short_obj.save()
        return redirect(short_obj.original_url)
        
        
