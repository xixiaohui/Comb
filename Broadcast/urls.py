from django.conf.urls  import url


from . import views

urlpatterns = [

	url(r'^$',views.index,name='index'),

	url(r'^broadmaster/',views.broadmaster,name='broadmaster'),

	url(r'^commonpeople/',views.commonpeople,name='commonpeople')


]
