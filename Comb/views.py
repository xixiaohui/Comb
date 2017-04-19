from django.shortcuts import render


from django.http import HttpResponse

# Create your views here.


"""
	主页面
"""
def index(request):
	# return HttpResponse("Hello,Comb!")
	context={}
	
	return render(request,'Comb/index.html',context)