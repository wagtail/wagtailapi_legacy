"""
Django settings for the test suite.

Reuses Wagtail's own test settings, as the tests rely on the models and
fixtures of Wagtail's test apps (``wagtail.test.*``).
"""

import os

import dj_database_url

from wagtail.test.settings import *  # noqa: F403


PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(os.path.dirname(PROJECT_DIR))

INSTALLED_APPS = [app for app in INSTALLED_APPS if app != "wagtail.api.v2"]  # noqa: F405
INSTALLED_APPS += ["wagtailapi_legacy.v2"]

ROOT_URLCONF = "wagtailapi_legacy.test.urls"

DATABASES = {
    "default": dj_database_url.config(default="sqlite:///test_wagtailapi_legacy.db"),
}

STATIC_ROOT = os.path.join(BASE_DIR, "test-static")
MEDIA_ROOT = os.path.join(BASE_DIR, "test-media")
