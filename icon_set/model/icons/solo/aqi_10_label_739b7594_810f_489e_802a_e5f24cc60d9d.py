"""10 AQI Label. Preserves the reference characters; reconstructs their stroke geometry.

Keyshape SQUARE: visible extremes (4, 4, 44, 44); centerline extremes (6, 6, 42, 42).
Lucide percent informs diagonal/counter separation; Lucide type informs
coherent monoline letter strokes. Digits and word order retain intentional
asymmetry. All coordinates are authored directly for the live SOLO48 keyshape.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '739b7594-810f-489e-802a-e5f24cc60d9d'
SOURCE_PATH = 'pictographic-primitives/symbol/10 AQI (text)_739b7594-810f-489e-802a-e5f24cc60d9d.svg'
AUTHOR = 'gpt-6'

class Aqi10Label(Solo48):
    icon_id = 'aqi-10-label'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbols/labels'
    aliases = ()
    keywords = ('aqi', 'air-quality', 'index', '10', 'label', 'pollution', 'weather', 'text')

    def build(self) -> None:
        self.add_polyline('one', (16, 9), (18, 6), (18, 18))
        self.add_arc('zero-top', (28, 10), (36, 10), radius_x=4, radius_y=4, sweep=True)
        self.add_line('zero-right', (36, 10), (36, 14))
        self.add_arc('zero-bottom', (36, 14), (28, 14), radius_x=4, radius_y=4, sweep=True)
        self.add_line('zero-left', (28, 14), (28, 10))
        self.add_contour('zero', 'zero-top', 'zero-right', 'zero-bottom', 'zero-left', closed=True)
        self.add_polyline('a-arch', (6, 42), (6, 35), (6, 27), (14, 27), (14, 35), (14, 42))
        self.add_line('a-bar', (6, 35), (14, 35))
        self.relate('connect', 'a-arch', 'a-bar')
        self.add_arc('q-top', (24, 31), (32, 31), radius_x=4, radius_y=4, sweep=True)
        self.add_line('q-right', (32, 31), (32, 35))
        self.add_arc('q-bottom', (32, 35), (24, 35), radius_x=4, radius_y=4, sweep=True)
        self.add_line('q-left', (24, 35), (24, 31))
        self.add_contour('q', 'q-top', 'q-right', 'q-bottom', 'q-left', closed=True)
        self.add_line('q-tail', (28, 39), (32, 42))
        self.relate('connect', 'q', 'q-tail')
        self.add_line('i', (42, 27), (42, 42))
