from django.http import HttpResponse
import requests
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

class BaseProxyView(APIView):
    permission_classes = [IsAuthenticated]

    def proxy(self, method, url, request, *args, **kwargs):
        response = requests.request(method, url, json=request.data, headers=request.headers)
        content_type = response.headers.get('Content-Type', 'application/json')
        return HttpResponse(response.content, status=response.status_code, content_type=content_type)
