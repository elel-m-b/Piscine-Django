import tempfile
from pathlib import Path
from unittest import mock

from django.test import TestCase

from . import views


class Ex02FormTests(TestCase):
    """Exercise 02: First Form.

    Each test points ex02.views.LOGS_FILE at a fresh temporary file so the
    tests never touch the real ex02/logs.txt used by the running app.
    """

    def setUp(self):
        self.tmp_dir = tempfile.TemporaryDirectory()
        self.tmp_log = Path(self.tmp_dir.name) / 'logs.txt'
        self.patcher = mock.patch.object(views, 'LOGS_FILE', self.tmp_log)
        self.patcher.start()

    def tearDown(self):
        self.patcher.stop()
        self.tmp_dir.cleanup()

    def test_get_returns_200(self):
        response = self.client.get('/ex02')
        self.assertEqual(response.status_code, 200)

    def test_form_is_rendered_not_hardcoded(self):
        response = self.client.get('/ex02')
        content = response.content.decode()
        self.assertIn('<form', content)
        self.assertIn('csrfmiddlewaretoken', content)
        self.assertIn('user_input', content)

    def test_history_starts_empty(self):
        response = self.client.get('/ex02')
        self.assertContains(response, 'No submissions yet.')

    def test_submitting_creates_the_log_file(self):
        self.assertFalse(self.tmp_log.exists())
        self.client.post('/ex02', {'user_input': 'hello world'})
        self.assertTrue(self.tmp_log.exists())

    def test_submission_appears_in_history(self):
        self.client.post('/ex02', {'user_input': 'hello world'})
        response = self.client.get('/ex02')
        self.assertContains(response, 'hello world')

    def test_post_redirects_get_pattern(self):
        response = self.client.post('/ex02', {'user_input': 'redirect check'})
        self.assertEqual(response.status_code, 302)

    def test_history_survives_across_requests(self):
        """Simulates a 'server restart' by reading the file fresh again."""
        self.client.post('/ex02', {'user_input': 'first entry'})
        self.client.post('/ex02', {'user_input': 'second entry'})
        response = self.client.get('/ex02')
        content = response.content.decode()
        self.assertIn('first entry', content)
        self.assertIn('second entry', content)

    def test_empty_submission_is_rejected(self):
        response = self.client.post('/ex02', {'user_input': ''})
        self.assertContains(response, 'This field is required')
        self.assertFalse(self.tmp_log.exists())
