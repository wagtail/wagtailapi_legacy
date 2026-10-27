from django.test import SimpleTestCase

from wagtailapi_legacy.v2.serializers import RichTextFieldSerializer


class TestRichTextFieldSerializer(SimpleTestCase):
    def test_accepts_text_field_kwargs(self):
        field = RichTextFieldSerializer(max_length=120)
        self.assertEqual(field.max_length, 120)
