from django.shortcuts import render
from django.views.generic import View


# Create your views here.


class HelloWord(View):

    def get(self, request):
        return render(request, 'HelloWorld.html')
