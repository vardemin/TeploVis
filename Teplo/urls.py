from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Teplo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    ('^$', 'Main.views.home'),
    url(r'^goods/heaters[/]$', 'Main.views.heater'),
    url(r'^cart[/]$', 'Main.views.show_cart'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
