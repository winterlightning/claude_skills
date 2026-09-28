"""footwear-sock: reviewed and repaired in place on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9b273457-d5cd-507b-9092-a6e989db84d5'
SOURCE_PATH = 'pictographic-primitives/clothes/footwear sock_9b273457-d5cd-507b-9092-a6e989db84d5.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-repaired'

class FootwearSock(Solo48):
    icon_id = 'footwear-sock'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'clothes'
    categories = ('primitives', 'clothes')
    aliases = ()
    keywords = ('footwear', 'sock', 'clothes')

    def build(self):
        # VRECT_L (8,4)-(40,44); keep ankle, heel and toe; remove tiny conversion segments.
        # Construction reference: No useful local sock match; smooth tangent cubic construction
        self.add_polyline('cuff',(11,13),(11,4),(26,4),(26,16))
        self.add_bezier('ankle',(26,16),((26,22),(29,26),(32,32)))
        self.add_bezier('toe',(32,32),((34,36),(40,35),(40,39)),((40,42),(38,44),(34,44)))
        self.add_line('sole-tip',(34,44),(31,44))
        self.add_bezier('sole',(31,44),((23,44),(23,35),(16,31)),((12,29),(8,29),(8,24)),((8,20),(11,17),(11,13)))
        self.add_contour('outline','cuff-1','cuff-2','cuff-3','ankle','toe','sole-tip','sole',closed=True)
        self.contours.pop(0)
