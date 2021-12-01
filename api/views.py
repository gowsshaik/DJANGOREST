from warnings import catch_warnings
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, response
from rest_framework.parsers import JSONParser
from rest_framework.utils import json
from .models import Details
from .serializer import DetailSer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
import requests
import urllib
import json
from rest_framework import mixins, generics


class DetGen(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView, mixins.UpdateModelMixin, mixins.RetrieveModelMixin,mixins.DestroyModelMixin):
    serializer_class = DetailSer
    queryset = Details.objects.all()
    lookup_field='id'
    def get(self, request,id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id=None):
        return self.update(request,id)
    def delete(self,request,id):
        return self.destroy(request,id)

# class DetView(APIView):
#     def get(self,request):
#         det=Details.objects.all()
#         ser=DetailSer(det,many=True)
#         return Response(ser.data)
#     def post(self,request):
#         ser=DetailSer(data=request.data)
#         if ser.is_valid():
#             ser.save()
#             return Response(ser.data,status=status.HTTP_201_CREATED)
#         return Response(statu=status.HTTP_400_BAD_REQUEST)

# class detUpd(APIView):
#     def getdata(self,id):
#         try:
#             return Details.objects.get(id=id)
#         except Details.DoesNotExist:
#             return Response(status=status.HTTP_204_NO_CONTENT)
#     def get(self,request,id):
#         data=self.getdata(id)
#         ser=DetailSer(data)
#         return Response(ser.data)
#     def put(self,request,id):
#         da=self.getdata(id)
#         ser=DetailSer(da,data=request.data)
#         if ser.is_valid():
#             ser.save()
#             return Response(ser.data,status=status.HTTP_200_OK)
#         return Response(status=status.HTTP_304_NOT_MODIFIED)
#     def delete(self,request,id):
#         data=self.getdata(id)
#         data.delete()
#         return Response(status=status.HTTP_302_FOUND)


# Create your views here.
# @api_view(['GET','POST'])
# def createdet(request):
#     if request.method=='GET':
#         det=Details.objects.all()
#         ser=DetailSer(det,many=True)
#         return Response(ser.data)
#     elif request.method=='POST':
#         ser=DetailSer(data=request.data)
#         if ser.is_valid():
#             ser.save()
#             return Response(ser.data,status=status.HTTP_201_CREATED)
#         else:
#             return Response(status=status.HTTP_400_BAD_REQUEST)
# def exp(request):
#     return render(request,'exp.html')
# def display(request):
#     if request.method=='POST':
#         createdet(request)
#         r=requests.get("http://127.0.0.1:8000/create/?format=json")
#         k=r.json()
#         return render(request,'disp.html',{'l':k})
#     elif request.method=='GET':
#         r=requests.get("http://127.0.0.1:8000/create/?format=json")
#         k=r.json()
#         return render(request,'disp.html',{'l':k})
# @api_view(['GET','PUT','DELETE'])
# def updatedyn(request,pk):
#     try:
#         det=Details.objects.get(pk=pk)
#     except Details.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     if request.method=='GET':
#         ser=DetailSer(det)
#         return Response(ser.data)
#     elif request.method=='PUT':
#         ser=DetailSer(det,data=request.data)
#         if ser.is_valid():
#             ser.save()
#             return Response(ser.data)
#         else:
#             return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)
#     elif request.method=='DELETE':
#         det.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
