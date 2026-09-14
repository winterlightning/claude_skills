"""Db Letters Underlined. Retains the identifying silhouette and visible features.

HRECT_L visible extremes (2, 6, 46, 42); centerlines (4, 8, 44, 40).
Supplied Db reference; monoline lettering rebuilt with tangent rounded bowls.
Repeated features share dimensions; deliberate asymmetry preserves the
letter order, handles and chart heights. Authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd98f0429-d034-4d6d-86d2-90889d17d1df'
SOURCE_PATH = 'pictographic-primitives/symbol/db (text u)_d98f0429-d034-4d6d-86d2-90889d17d1df.svg'
AUTHOR = 'gpt-6'


class DbLettersUnderlined(Solo48):
    icon_id = 'db-letters-underlined'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbols/standalone"
    aliases = ()
    keywords = ('db', 'letters', 'database', 'text', 'underline', 'typography', 'abbreviation')

    def build(self) -> None:
        self.add_arc('d-curve', (4, 8), (4, 30), radius_x=14, radius_y=11, sweep=True)
        self.add_line('d-back', (4, 30), (4, 8))
        self.add_contour('d', 'd-curve', 'd-back', closed=True)
        self.add_polyline('b-stem', (30, 8), (30, 24), (30, 30))
        self.add_arc('b-top', (30, 24), (44, 24), radius_x=7, radius_y=6, sweep=True)
        self.add_arc('b-bottom', (44, 24), (30, 24), radius_x=7, radius_y=6, sweep=True)
        self.add_contour('b-bowl', 'b-top', 'b-bottom', closed=True)
        self.relate("connect", 'b-stem', 'b-bowl')
        self.add_line('underline', (4, 40), (44, 40))
