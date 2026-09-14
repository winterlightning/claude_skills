"""7 Days Stacked Label. Keeps 7 above DAY; drops the plural S to preserve readable lettering.

HRECT_L visible extremes (2, 6, 46, 42), centerlines (4, 8, 44, 40).
Lucide type: coherent monoline letter strokes.
Geometry authored directly on SOLO48. Letter order and directional numerals
retain intentional asymmetry; repeated letters share construction parameters.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e220de6b-3280-456c-b80e-dc2702654cac'
SOURCE_PATH = 'pictographic-primitives/symbol/7day (text)_e220de6b-3280-456c-b80e-dc2702654cac.svg'
AUTHOR = 'gpt-6'


class SevenDaysStackedLabel(Solo48):
    icon_id = 'seven-days-stacked-label'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'symbols/labels'
    aliases = ()
    keywords = ('7-days', 'days', 'seven', 'week', 'duration', 'trial', 'label', 'text')

    def build(self) -> None:
        self.add_polyline('seven', (18, 8), (30, 8), (20, 20))
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
