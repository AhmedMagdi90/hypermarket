from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns  # import for i18n patterns

urlpatterns = [
    # URLs that don't depend on language (e.g., language switching)
    path('i18n/', include('django.conf.urls.i18n')),  # language set/change url
]

# Wrap your main app URLs and admin in i18n_patterns so they get language prefixes (/en/, /ar/)
urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    # Note: You already include 'accounts/' with django.contrib.auth.urls,
    # which includes login/logout/password management URLs with namespace 'auth'.
    # Since you have custom login/logout URLs in your core app, you might consider removing this line or move your custom auth URLs.
    path('accounts/', include('django.contrib.auth.urls')),  # optional, remove if using custom auth
    path('', include('core.urls')),
)
