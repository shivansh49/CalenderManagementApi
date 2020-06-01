from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from  django.http import HttpResponse,JsonResponse
from  rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework.authentication import SessionAuthentication,BasicAuthentication
from  rest_framework.views import APIView
from  rest_framework import filters,viewsets
from rest_framework.response import Response
from django.db.models import Model
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from   .models import usrs,Event
from .serializers import usrsSerializer,EventSerializer
class usr_requestapi(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request):
        art = usrs.objects.all()
        s = usrsSerializer(art, many=True)
        return Response(s.data)
    def post(self,request):
        s = EventSerializer(data=request.data)
        ab = usrsSerializer(data=request.data)
        if s.is_valid() and ab.is_valid():
            s.save()
            ab.save()
            return Response(s.data, status=status.HTTP_201_CREATED)
        return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)
class user_detailsapi(APIView):
    authentication_classes = [SessionAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get_object(self,Email):
        try:
            return Event.objects.filter(Email=Email)
        except Event.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    def get(self,request,Email):
        q = self.get_object(Email)
        p = EventSerializer(q,many=True)
        return Response(p.data)
class user_detailsschedule(APIView):
    authentication_classes = [SessionAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get_object(self,id):
        try:
            return Event.objects.get(id=id)
        except Event.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    def get(self,request,id):
        q = self.get_object(id)
        print(100)
        print(q)
        p = EventSerializer(q)
        return Response(p.data)
    def put(self,request,id):
        w = Event.objects.get(id=id)
        a = EventSerializer(w,data=request.data)
        if a.is_valid():
            a.save()
            return Response(a.data)
        return Response(a.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id):
        q = self.get_object(id)
        q.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
@api_view(['GET','POST'])
def usr_request(request):
    if request.method=="GET":
        art = usrs.objects.all()
        s = usrsSerializer(art,many=True)
        return Response(s.data)
    elif request.method=="POST":
        s = usrsSerializer(data=request.data)
        if s.is_valid():
            s.save()
            return Response(s.data,status=status.HTTP_201_CREATED)
        return Response(s.errors,status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET','PUT','DELETE'])
def user_details(request,pk):
    try:
        q = usrs.objects.get(pk=pk)
    except usrs.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    if request.method=="GET":
        p = usrsSerializer(q)
        return Response(p.data)
    elif request.method=="PUT":
        a = usrsSerializer(data=request.data)
        if a.is_valid():
            a.save()
            return Response(a.data,status=status.HTTP_201_CREATED)
        return JsonResponse(a.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method=="DELETE":
        q.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


