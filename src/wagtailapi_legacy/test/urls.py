from django.urls import include, path
from wagtail import urls as wagtail_urls
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail.images import urls as wagtailimages_urls

from wagtailapi_legacy.v2.documents.views import DocumentsAPIViewSet
from wagtailapi_legacy.v2.images.views import ImagesAPIViewSet
from wagtailapi_legacy.v2.redirects.views import RedirectsAPIViewSet
from wagtailapi_legacy.v2.router import WagtailAPIRouter
from wagtailapi_legacy.v2.views import PagesAPIViewSet


class Test10411APIViewSet(PagesAPIViewSet):
    meta_fields = []


api_router = WagtailAPIRouter("wagtailapi_v2")
api_router.register_endpoint("pages", PagesAPIViewSet)
api_router.register_endpoint("images", ImagesAPIViewSet)
api_router.register_endpoint("documents", DocumentsAPIViewSet)
api_router.register_endpoint("redirects", RedirectsAPIViewSet)
api_router.register_endpoint("issue_10411", Test10411APIViewSet)


urlpatterns = [
    path("admin/", include(wagtailadmin_urls)),
    path("documents/", include(wagtaildocs_urls)),
    path("images/", include(wagtailimages_urls)),
    path("api/main/", api_router.urls),
    path("", include(wagtail_urls)),
]
