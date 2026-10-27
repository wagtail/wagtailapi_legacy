from django.urls import include, path
from django.views.i18n import JavaScriptCatalog
from wagtail import hooks
from wagtail.admin.site_summary import SummaryItem


class WagtailapiLegacySummaryItem(SummaryItem):
    order = 50
    template_name = "wagtailapi_legacy/admin/wagtailapi_legacy_summary.html"


@hooks.register("construct_homepage_summary_items")
def register_wagtailapi_legacy_summary_item(request, summary_items):
    summary_items.append(WagtailapiLegacySummaryItem(request))


@hooks.register("register_admin_urls")
def register_admin_urls():
    urls = [
        path(
            "jsi18n/",
            JavaScriptCatalog.as_view(packages=["wagtailapi_legacy"]),
            name="javascript_catalog",
        ),
        # Add other package-scoped URLs here so they are access-restricted to the admin.
    ]

    return [
        path(
            "wagtailapi_legacy/",
            include(
                (urls, "wagtailapi_legacy"),
                namespace="wagtailapi_legacy",
            ),
        )
    ]
