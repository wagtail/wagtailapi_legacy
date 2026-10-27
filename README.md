# wagtailapi_legacy

Legacy versions of the Wagtail API that are no longer maintained in Wagtail core.

This package contains the Wagtail v2 API, previously `wagtail.api.v2`. The v2 API is deprecated in favor of the [v3 API](https://docs.wagtail.org/en/latest/advanced_topics/api/v3/index.html): it raises deprecation warnings from Wagtail 8.2, and will be removed from Wagtail in 9.0 at the earliest. This package lets projects keep using the v2 API while they migrate. See the [v3 API migration guide](https://docs.wagtail.org/en/latest/advanced_topics/api/v3/migration.html) for details.

The v1 API, removed in Wagtail 2.0, is available in the 1.x releases of this package, from the [`stable/v1`](https://github.com/wagtail/wagtailapi_legacy/tree/stable/v1) branch.

> [!NOTE]
> While the intention of this package is to keep old versions of the API working on the latest version of Wagtail, the Wagtail core team are not committed to carrying out much of this work. If it doesn't work with the version of Wagtail you are using, pull requests are welcome.

## Links

- [Configuration guide](https://github.com/wagtail/wagtailapi_legacy/blob/main/docs/configuration.md)
- [Usage guide](https://github.com/wagtail/wagtailapi_legacy/blob/main/docs/usage.md)
- [Changelog](https://github.com/wagtail/wagtailapi_legacy/blob/main/CHANGELOG.md)
- [Contributing](https://github.com/wagtail/wagtailapi_legacy/blob/main/CONTRIBUTING.md)
- [Security](https://github.com/wagtail/wagtailapi_legacy/security)

## Supported versions

This package supports Wagtail 8.1 and up, and all [compatible versions of Python and Django](https://docs.wagtail.org/en/stable/releases/upgrading.html#compatible-django-python-versions).

## Installation

Pick the command for your preferred package installer:

```bash
uv add wagtailapi-legacy
poetry add wagtailapi-legacy
pip install wagtailapi-legacy
```

## Migrating from `wagtail.api.v2`

Replace `wagtail.api.v2` with `wagtailapi_legacy.v2` in `INSTALLED_APPS`, then update your imports:

| Wagtail                                             | wagtailapi_legacy                                        |
| --------------------------------------------------- | -------------------------------------------------------- |
| `wagtail.api.v2`                                    | `wagtailapi_legacy.v2`                                   |
| `wagtail.images.api.v2.views`                       | `wagtailapi_legacy.v2.images.views`                      |
| `wagtail.images.api.v2.serializers`                 | `wagtailapi_legacy.v2.images.serializers`                |
| `wagtail.images.api.fields.ImageRenditionField`     | `wagtailapi_legacy.v2.images.fields.ImageRenditionField` |
| `wagtail.documents.api.v2.views`                    | `wagtailapi_legacy.v2.documents.views`                   |
| `wagtail.documents.api.v2.serializers`              | `wagtailapi_legacy.v2.documents.serializers`             |
| `wagtail.contrib.redirects.api.RedirectsAPIViewSet` | `wagtailapi_legacy.v2.redirects.views.RedirectsAPIViewSet` |

`APIField` and `api_fields` are shared with the v3 API, so keep importing `APIField` from `wagtail.api`. The `WAGTAILAPI_*` settings work as before.
