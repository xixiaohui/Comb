from django.shortcuts import render

from django.http import HttpResponse

from Comb.models import Author

# Create your views here.


"""
	主页面
"""
def index(request):
	# return HttpResponse("Hello,Comb!")
	authors = Author.objects.all()
	context={
		"authors":authors,
	}
	
	return render(request,'Comb/index.html',context)