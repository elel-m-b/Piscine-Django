import re

from django.test import TestCase

from .views import _build_rows, ROW_COUNT


class Ex03GradientLogicTests(TestCase):
    """Unit tests on the color-generation logic itself (view, not template)."""

    def test_build_rows_returns_fifty_rows(self):
        rows = _build_rows()
        self.assertEqual(len(rows), 50)
        self.assertEqual(ROW_COUNT, 50)

    def test_every_row_has_the_four_columns(self):
        rows = _build_rows()
        for row in rows:
            self.assertEqual(set(row.keys()), {'black', 'red', 'blue', 'green'})

    def test_all_colors_are_valid_hex_codes(self):
        rows = _build_rows()
        hex_pattern = re.compile(r'^#[0-9a-f]{6}$')
        for row in rows:
            for color in row.values():
                self.assertRegex(color, hex_pattern)

    def test_each_column_has_fifty_distinct_shades(self):
        rows = _build_rows()
        for column in ('black', 'red', 'blue', 'green'):
            shades = [row[column] for row in rows]
            self.assertEqual(len(set(shades)), 50, f'{column} column has duplicate shades')


class Ex03PageTests(TestCase):
    """Exercise 03: Fifty Shades of Bic — the rendered page."""

    def test_ex03_returns_200(self):
        response = self.client.get('/ex03')
        self.assertEqual(response.status_code, 200)

    def test_unknown_url_returns_404(self):
        response = self.client.get('/ex03foo')
        self.assertEqual(response.status_code, 404)

    def test_page_has_51_table_rows(self):
        response = self.client.get('/ex03')
        content = response.content.decode()
        self.assertEqual(content.count('<tr>'), 51)  # 1 header + 50 data rows

    def test_template_only_uses_four_td_and_th_pairs(self):
        # Enforces the subject's tag-count limit directly on the .html source,
        # not the rendered (looped) output.
        from pathlib import Path
        source = Path(__file__).parent.joinpath('templates/ex03/index.html').read_text()
        self.assertEqual(source.count('<td'), 4)
        self.assertEqual(source.count('<th'), 4)

    def test_no_color_is_hardcoded_in_the_template(self):
        from pathlib import Path
        source = Path(__file__).parent.joinpath('templates/ex03/index.html').read_text()
        for forbidden in ('#000000', '#ff0000', '#0000ff', '#00ff00', 'red;', 'blue;', 'green;'):
            self.assertNotIn(forbidden, source)

    def test_column_headers_present(self):
        response = self.client.get('/ex03')
        for column in ('Black', 'Red', 'Blue', 'Green'):
            self.assertContains(response, f'<th>{column}</th>')
