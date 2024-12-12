from django.contrib import admin
from.models import *

# Register your models here.
class contactAdmin(admin.ModelAdmin):
  list_display=('Name','Email','Mobile','Message')
admin.site.register(contact,contactAdmin)

class categoryAdmin(admin.ModelAdmin):
    list_display=('id','cname','cpic','cdate')
admin.site.register(category,categoryAdmin)

class sliderAdmin(admin.ModelAdmin):
    list_display=('id','spic','sdate')
admin.site.register(slider,sliderAdmin)

class subcategoryAdmin(admin.ModelAdmin):
   list_display=('id','category_name','subcategory_name')
admin.site.register(subcategory,subcategoryAdmin)

class myproductAdmin(admin.ModelAdmin):
   list_display=('id', 'product_category','subcategory_name','price','discount_price',
                 'product_pic','total_discount','product_quantity','pdate')
admin.site.register(myproduct,myproductAdmin)

class registerAdmin(admin.ModelAdmin):
   list_display=('name','email','mobile','password','address','profile')
admin.site.register(register,registerAdmin)

class offpicAdmin(admin.ModelAdmin):
   list_display=('id','ofpic')
admin.site.register(offpic,offpicAdmin)

class cartAdmin(admin.ModelAdmin):
    list_display=('id','user_id','product_name','product_quantity','price','total_price','product_picture','pw','added_date')
admin.site.register(cart,cartAdmin)

class myorderAdmin(admin.ModelAdmin):
    list_display=('id','user_id','product_name','product_quantity','price','total_price','product_picture','pw','order_date','status')
admin.site.register(myorder,myorderAdmin)

