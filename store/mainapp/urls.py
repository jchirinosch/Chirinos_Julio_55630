from django.urls import path, include
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
        path('', home, name='home' ),
        path('guitarras/', guitarras, name='guitarras' ),
        path('guitarrasForm/', guitarrasform, name='guitarrasForm' ),
        path('update_guitarras/<id_guitarra>/', updateGuitarras, name='update_guitarras' ), 
        path('delete_guitarras/<id_guitarra>/', deleteGuitarras, name='delete_guitarras' ),
        path('create_guitarras/', createGuitarras, name='create_guitarras' ),
        path('buscarGuitarras/', buscarGuitarras, name = 'buscarGuitarras'),
        path('buscar1/', buscar1, name = 'buscar1'),


        path('bajos/', bajos, name='bajos' ),
        path('bajosForm/', bajosform, name='bajosForm' ),
        path('update_bajos/<id_bajo>/', updateBajos, name='update_bajos' ), 
        path('delete_bajos/<id_bajo>/', deleteBajos, name='delete_bajos' ),
        path('create_bajos/', createBajos, name='create_bajos' ),
        path('buscarBajos/', buscarBajos, name = 'buscarBajos'),
        path('buscar3/', buscar3, name = 'buscar3'),


        path('percusion/', percusion, name='percusion' ),
        path('percusionForm/', percusionform, name='percusionForm' ),
        path('update_percusion/<id_percusion>/', updatePercusion, name='update_percusion' ), 
        path('delete_percusion/<id_percusion>/', deletePercusion, name='delete_percusion' ),
        path('create_percusion/', createPercusion, name='create_percusion' ),
        path('buscarPercusion/', buscarPercusion, name = 'buscarPercusion'),
        path('buscar4/', buscar4, name = 'buscar4'),


        path('sucursales/', sucursales, name='sucursales' ),  
        path('buscarSucursal/', buscarSucursal, name = 'buscarSucursal'),
        path('buscar2/', buscar2, name = 'buscar2'),
        path('update_sucursal/<id_sucursal>/', updateSucursal, name='update_sucursal' ), 
        path('delete_sucursal/<id_sucursal>/', deleteSucursal, name='delete_sucursal' ),
        path('create_sucursal/', createSucursal, name='create_sucursal' ),

        path('login/', login_request, name='login' ),
        path('logout/', LogoutView.as_view(template_name='mainapp/logout.html'), name='logout' ),
        path('registro/', register, name='registro' ),
        path('aboutme/', aboutMe, name="aboutme" ),
        path('editar_perfil/', editarPerfil, name="editar_perfil" ),
        path('agregar_avatar/', agregarAvatar, name="agregar_avatar" ),
]