import colorsys

from django.shortcuts import render

ROW_COUNT = 50

# Hue of each column on the 0..1 scale used by colorsys (red=0, green=1/3,
# blue=2/3). "Black" has no hue: its shades are simply a black -> white
# grayscale gradient (saturation = 0).
COLUMN_SPECS = [
    ('Black', None),
    ('Red', 0.0),
    ('Blue', 2 / 3),
    ('Green', 1 / 3),
]


def _shade(hue, lightness):
    """Return a '#rrggbb' hex color for the given hue/lightness.

    hue=None produces a pure grayscale color (used for the Black column).
    """
    if hue is None:
        r, g, b = colorsys.hls_to_rgb(0.0, lightness, 0.0)
    else:
        r, g, b = colorsys.hls_to_rgb(hue, lightness, 1.0)
    return '#%02x%02x%02x' % (round(r * 255), round(g * 255), round(b * 255))


def _build_rows():
    """Generate the 50-row color gradient, computed here in the view
    (never hard-coded in the template)."""
    rows = []
    for i in range(ROW_COUNT):
        # Spread lightness across the open interval (0, 1) so every row is
        # different and we never repeat pure black or pure white.
        lightness = (i + 1) / (ROW_COUNT + 1)
        rows.append({
            'black': _shade(None, lightness),
            'red': _shade(0.0, lightness),
            'blue': _shade(2 / 3, lightness),
            'green': _shade(1 / 3, lightness),
        })
    return rows


def index(request):
    context = {
        'page_title': 'Ex03: Fifty Shades of Bic',
        'columns': [name for name, _ in COLUMN_SPECS],
        'rows': _build_rows(),
    }
    return render(request, 'ex03/index.html', context)
