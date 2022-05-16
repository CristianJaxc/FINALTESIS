from django.urls import path
from .import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from .views import pagina_productos,product_list,product_detail

urlpatterns = [
    #!-------------------------- esterilizacion ----------------------------------------
    path('pagina_esterilizacion/',views.esterilizacion, name='pagina_esterilizacion'),
    path('pagina_productos/', views.pagina_productos, name='pagina_productos'),
    url('product_list', views.product_list, name='product_list'),
    url(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),


    #path('listado_productos/', views.product_list, name='listados_productos'),
    #path('Detalle_productos/<int:id>', views.product_detail, name='Detalle_productos'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



