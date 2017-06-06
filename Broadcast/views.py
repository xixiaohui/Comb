from django.shortcuts import render

# Create your views here.


"""
	主页面
"""
def index(request):
	# return HttpResponse("Hello,Comb!")
	# authors = Author.objects.all()

	context={
	# "authors":authors,
	}
	
	return render(request,'Broadcast/index.html',context)


def broadmaster(request):


	context={}

	return render(request,'Broadcast/broadmaster.html',context)


def commonpeople(request):

	context={}

	return render(request,'Broadcast/commonpeople.html',context)