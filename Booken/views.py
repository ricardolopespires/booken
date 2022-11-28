from django.views.generic import View, TemplateView, ListView ,DeleteView
from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib import messages







class Template_Index_View(View):


    def get(self, request):
        return render (request, 'initial/index.html')




def about(request):
    return render(request, 'initial/about.html')
