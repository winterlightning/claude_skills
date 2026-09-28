"""A cloud outline holds an inner swirl: a curved line loops from the lower left up and around into a hooked arrow near the centre.

Plan: Cloud lobes and an inward curl form a continuous contour.
Keyshape: HRECT_L; exact SOLO48 envelope from the contract.
Construction reference: cloud: rounded lobes flowing into flat floor.
Simplification: Redundant inner return and short arrowhead stroke omitted to open the curl.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'db353c0d-658e-461b-b173-300e908af122'
SOURCE_PATH = 'pictographic-primitives/logos/google cloud logo_db353c0d-658e-461b-b173-300e908af122.svg'
AUTHOR = 'gpt-6'


class GoogleCloudLogo(Solo48):
    icon_id = 'google-cloud-logo'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    categories = ("logos", "primitives")
    aliases = ()
    keywords = ('google-cloud', 'google', 'cloud', 'logo', 'brand', 'hosting', 'platform')

    def build(self):
        self.add_bezier('crest',(14,20),((14,12),(20,8),(26,8)),((34,8),(38,14),(38,20)))
        self.add_bezier('right',(38,20),((42,21),(44,24),(44,29)),((44,35),(39,40),(33,40)))
        self.add_line('floor',(33,40),(14,40))
        self.add_arc('left',(14,40),(14,20),radius_x=10)
        self.add_bezier('curl',(14,20),((21,20),(25,23),(27,27)))
        self.add_line('hook-1',(27,27),(23,31))
        self.add_contour('outline','crest','right','floor','left',closed=True)
        self.add_contour('swirl','curl','hook-1')
        self.relate('connect','outline','swirl')
