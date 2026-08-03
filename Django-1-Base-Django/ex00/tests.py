from django.test import TestCase


class Ex00PageTests(TestCase):
    """Exercise 00: First Static Page."""

    def test_ex00_no_slash_returns_200(self):
        response = self.client.get('/ex00')
        self.assertEqual(response.status_code, 200)

    def test_ex00_with_slash_returns_200(self):
        response = self.client.get('/ex00/')
        self.assertEqual(response.status_code, 200)

    def test_unknown_url_returns_404(self):
        response = self.client.get('/ex00foo')
        self.assertEqual(response.status_code, 404)

    def test_page_title(self):
        response = self.client.get('/ex00')
        self.assertContains(response, '<title>Ex00: Markdown Cheatsheet</title>', html=False)

    def test_page_is_a_full_html_document(self):
        response = self.client.get('/ex00')
        content = response.content.decode()
        self.assertTrue(content.strip().startswith('<!DOCTYPE html>'))
        self.assertIn('<html', content)
        self.assertIn('<head>', content)
        self.assertIn('<body>', content)

    def test_page_mentions_markdown_topics(self):
        response = self.client.get('/ex00')
        content = response.content.decode()
        for keyword in ('Heading', 'bold', 'italic', 'Blockquote', 'Table'):
            self.assertIn(keyword, content)
