"""1 Day Label. Preserves the reference characters; reconstructs their stroke geometry.

Keyshape HRECT_L: visible extremes (2, 6, 46, 42); centerline extremes (4, 8, 44, 40).
Lucide percent informs diagonal/counter separation; Lucide type informs
coherent monoline letter strokes. Digits and word order retain intentional
asymmetry. All coordinates are authored directly for the live SOLO48 keyshape.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f1dbc1f6-7ce5-41b6-98fd-726c2d1d0f09'
SOURCE_PATH = 'pictographic-primitives/symbol/1day (text)_f1dbc1f6-7ce5-41b6-98fd-726c2d1d0f09.svg'
AUTHOR = 'gpt-6'


class OneDayLabel(Solo48):
    icon_id = 'one-day-label'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbols/labels"
    aliases = ()
    keywords = ('1-day', 'day', 'one', 'duration', 'label', 'time', 'delivery', 'text')

    def build(self) -> None:
        self.add_polyline('one', (21, 11), (25, 8), (25, 20))
        self.add_line('d-top', (6, 29), (8, 29))
        self.add_arc('d-ne', (8, 29), (12, 33), radius_x=4, radius_y=4, sweep=True)
        self.add_line('d-right', (12, 33), (12, 36))
        self.add_arc('d-se', (12, 36), (8, 40), radius_x=4, radius_y=4, sweep=True)
        self.add_line('d-left-1', (8, 40), (6, 40))
        self.add_line('d-left-2', (6, 40), (6, 29))
        self.add_contour('d', 'd-top', 'd-ne', 'd-right', 'd-se', 'd-left-1', 'd-left-2', closed=True)
        self.add_polyline('a-arch', (22, 40), (22, 35), (22, 29), (30, 29), (30, 35), (30, 40))
        self.add_line('a-bar', (22, 35), (30, 35))
        self.relate("connect", 'a-arch', 'a-bar')
        self.add_polyline('y-arms', (40, 29), (42, 34), (42, 29))
        self.add_line('y-stem', (42, 34), (42, 40))
        self.relate("connect", 'y-arms', 'y-stem')
