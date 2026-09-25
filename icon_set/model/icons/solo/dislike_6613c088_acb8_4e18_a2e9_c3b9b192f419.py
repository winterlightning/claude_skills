"""dislike: reviewed and repaired in place on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6613c088-acb8-4e18-a2e9-c3b9b192f419'
SOURCE_PATH = 'pictographic-primitives/rating/dislike_6613c088-acb8-4e18-a2e9-c3b9b192f419.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-repaired'

class Dislike(Solo48):
    icon_id = 'dislike'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'rating'
    categories = ('rating', 'primitives')
    aliases = ()
    keywords = ('dislike', 'rating')

    def build(self):
        # SQUARE (6,6)-(42,42); one continuous outline, no loose one-unit cuff joins.
        # Construction reference: Lucide thumbs-down: smooth knuckles and a clear thumb
        self.add_line('top',(6,6),(30,6))
        self.add_bezier('knuckles',(30,6),((35,6),(37,8),(38,12)),((40,16),(42,19),(42,22)),((42,25),(40,26),(37,26)))
        self.add_line('palm',(37,26),(26,26))
        self.add_bezier('thumb',(26,26),((27,29),(30,32),(30,35)),((30,38),(28,42),(26,42)),((24,42),(20,33),(17,30)))
        self.add_bezier('wrist',(17,30),((14,27),(10,26),(6,26)))
        self.add_line('cuff',(6,26),(6,6))
        self.add_contour('outline','top','knuckles','palm','thumb','wrist','cuff',closed=True)
