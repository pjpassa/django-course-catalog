from django.conf.urls import include, url, patterns
from django.conf.urls.static import static
from django.contrib import admin
from DjangoCourseCatalog import settings
from courses import views

urlpatterns = patterns([
    url(r'^admin/',
        include(admin.site.urls),
        name="admin"),
    url(r'^courses/add$',
        views.CourseAddChangeView.as_view(),
        name="add"),
    ]) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
