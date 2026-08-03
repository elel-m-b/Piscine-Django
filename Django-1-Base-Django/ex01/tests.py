from django.test import TestCase


class Ex01PageTests(TestCase):
    """Exercise 01: A Few More Pages."""

    urls_and_titles = {
        '/ex01/django': 'Ex01: Django, Web Framework.',
        '/ex01/display': 'Ex01: Display Process of a Static Page.',
        '/ex01/templates': 'Ex01: Template Engine.',
    }

    def test_all_pages_return_200(self):
        for url in self.urls_and_titles:
            with self.subTest(url=url):
                response = self.client.get(url)
                self.assertEqual(response.status_code, 200)

    def test_all_pages_work_with_trailing_slash_too(self):
        for url in self.urls_and_titles:
            with self.subTest(url=url):
                response = self.client.get(url + '/')
                self.assertEqual(response.status_code, 200)

    def test_page_titles_are_correct(self):
        for url, title in self.urls_and_titles.items():
            with self.subTest(url=url):
                response = self.client.get(url)
                self.assertContains(response, f'<title>{title}</title>')

    def test_unrelated_ex01_url_returns_404(self):
        response = self.client.get('/ex01/doesnotexist')
        self.assertEqual(response.status_code, 404)

    def test_nav_bar_present_on_every_page(self):
        for url in self.urls_and_titles:
            with self.subTest(url=url):
                response = self.client.get(url)
                content = response.content.decode()
                self.assertIn('/ex01/django', content)
                self.assertIn('/ex01/display', content)
                self.assertIn('/ex01/templates', content)

    def test_style1_used_on_django_and_display_pages(self):
        for url in ('/ex01/django', '/ex01/display'):
            with self.subTest(url=url):
                response = self.client.get(url)
                content = response.content.decode()
                self.assertIn('<link rel="stylesheet" href="/static/ex01/style1.css">', content)
                self.assertNotIn('<link rel="stylesheet" href="/static/ex01/style2.css">', content)

    def test_style2_used_only_on_template_engine_page(self):
        response = self.client.get('/ex01/templates')
        content = response.content.decode()
        self.assertIn('<link rel="stylesheet" href="/static/ex01/style2.css">', content)
        self.assertNotIn('<link rel="stylesheet" href="/static/ex01/style1.css">', content)

    def test_pages_are_full_html_documents(self):
        for url in self.urls_and_titles:
            with self.subTest(url=url):
                response = self.client.get(url)
                content = response.content.decode()
                self.assertTrue(content.strip().startswith('<!DOCTYPE html>'))
