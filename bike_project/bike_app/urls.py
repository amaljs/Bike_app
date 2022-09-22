from django.urls import path


from bike_app import views
app_name='bike_app'
urlpatterns = [

    path('',views.index,name="index"),
    path('bike/<int:bike_num>/',views.details,name='details'),
    path('add_bike/',views.add_bike,name='add_bike'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name="delete")

]