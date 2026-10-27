from wagtailapi_legacy.v2.documents.views import DocumentsAPIViewSet
from wagtailapi_legacy.v2.images.views import ImagesAPIViewSet
from wagtailapi_legacy.v2.redirects.views import RedirectsAPIViewSet
from wagtailapi_legacy.v2.router import WagtailAPIRouter
from wagtailapi_legacy.v2.views import PagesAPIViewSet


api_router = WagtailAPIRouter("wagtailapi")
api_router.register_endpoint("pages", PagesAPIViewSet)
api_router.register_endpoint("images", ImagesAPIViewSet)
api_router.register_endpoint("documents", DocumentsAPIViewSet)
api_router.register_endpoint("redirects", RedirectsAPIViewSet)
