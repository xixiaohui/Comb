from django.contrib import admin

from Comb.models import Author,Book,Booklist,Publisher,ReasonForListing
# Register your models here.


class AuthorAdmin(admin.ModelAdmin):
	pass

class PublisherAdmin(admin.ModelAdmin):
	pass

class ReasonForListingAdmin(admin.ModelAdmin):
	pass

class BookAdmin(admin.ModelAdmin):
	pass

class BooklistAdmin(admin.ModelAdmin):
	pass


admin.site.register(Author,AuthorAdmin)
admin.site.register(Publisher,PublisherAdmin)
admin.site.register(ReasonForListing,ReasonForListingAdmin)
admin.site.register(Book,BookAdmin)
admin.site.register(Booklist,BooklistAdmin)

