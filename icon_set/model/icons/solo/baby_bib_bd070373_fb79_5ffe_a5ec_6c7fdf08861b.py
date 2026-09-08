from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bd070373-fb79-5ffe-a5ec-6c7fdf08861b'
SOURCE_PATH = 'pictographic-primitives/babies/baby care bib_bd070373-fb79-5ffe-a5ec-6c7fdf08861b.svg'
AUTHOR = 'gpt-6'

class BabyBib(Solo48):
    icon_id = 'baby-bib'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/baby-care"
    aliases = ()
    keywords = ('bib', 'baby', 'feeding', 'infant', 'mealtime', 'childcare', 'bear', 'apron')

    # Designed to centerline extremes (2, 2)–(46, 46).
    def build(self) -> None:
        self.add_arc('bib-1', (16, 2), (2, 24), radius_x=14, radius_y=22, sweep=False)
        self.add_arc('bib-2', (2, 24), (24, 46), radius_x=22, radius_y=22, sweep=False)
        self.add_arc('bib-3', (24, 46), (46, 24), radius_x=22, radius_y=22, sweep=False)
        self.add_arc('bib-4', (46, 24), (32, 2), radius_x=14, radius_y=22, sweep=False)
        self.add_arc('bib-5', (32, 2), (35, 12), radius_x=6, radius_y=7, sweep=True)
        self.add_arc('bib-6', (35, 12), (13, 12), radius_x=11, radius_y=9, sweep=True)
        self.add_arc('bib-7', (13, 12), (16, 2), radius_x=6, radius_y=7, sweep=True)
        self.add_contour('bib', 'bib-1', 'bib-2', 'bib-3', 'bib-4', 'bib-5', 'bib-6', 'bib-7', closed=True)
