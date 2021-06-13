#from django.shortcuts import render
from rest_framework import viewsets
#from django.db.models import Q
#from rest_framework import generics
#from rest_framework.response import Response


from .serializers import UserSerializer
from .models import User
'''
from .serializers import loginSerializer
from .models import login
'''
from .serializers import tweetSerializer
from .models import tweet

from .pagination import APIPagination

from .forms import UserForm
from django.views.generic.edit import FormView


    '''
    def showformdata(request):
        if request.method == 'POST':
        fm = UserForm(request.POST)
        if fm.is_valid():
       '''     


class UserViewSet(viewsets.ModelViewSet):
    #def list(self, request):
    serializer_class = UserSerializer
    queryset = User.objects.all().order_by('name')
    form_class = UserForm

    def form_valid(self, form):
        form.clean()
        return super().form_valid(form)

     
class tweetViewSet(viewsets.ModelViewSet):
    queryset = tweet.objects.all().order_by('posted_at')
    serializer_class = tweetSerializer    
    pagination_class = APIPagination

'''
# Create your views here.
class ListCreateTweetView(generics.ListCreateAPIView):
    queryset = tweet.objects.all()
    serializer_class = tweetSerializer

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        override_view_attributes(self)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user, type=0)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        queryset = queryset.filter(Q(name=request.user))

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
        '''