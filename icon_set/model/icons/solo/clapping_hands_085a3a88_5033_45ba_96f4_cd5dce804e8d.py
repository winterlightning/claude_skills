"""Two overlapping hands clap diagonally upward-right. SQUARE centerlines 6,6–42,42. Related Lucide hand-metal informs rounded fingers; omit small impact rays and merge fingers into readable palms."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '085a3a88-5033-45ba-96f4-cd5dce804e8d'
SOURCE_PATH = 'pictographic-primitives/social/reward claps hand_085a3a88-5033-45ba-96f4-cd5dce804e8d.svg'
AUTHOR = 'gpt-6'

class ClappingHands(Solo48):
    icon_id = 'clapping-hands'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/social"
    aliases = ()
    keywords = ('hand', 'clapping', 'applause', 'palm', 'gesture', 'celebration')

    def build(self):
        # Two overlapping, upward-right palms. The rear hand stays open where occluded.
        self.add_line('front-thumb-out',(15,33),(15,23))
        self.add_arc('front-thumb-tip',(15,23),(23,23),radius_x=4)
        self.add_line('front-thumb-in',(23,23),(23,29))
        self.add_line('front-fingers-left',(23,29),(34,13))
        self.add_arc('front-fingertips',(34,13),(42,17),radius_x=5)
        self.add_line('front-fingers-right',(42,17),(34,32))
        self.add_arc('front-palm-right',(34,32),(24,42),radius_x=10)
        self.add_arc('front-palm-left',(24,42),(15,33),radius_x=9)
        self.add_contour('front','front-thumb-out','front-thumb-tip','front-thumb-in','front-fingers-left','front-fingertips','front-fingers-right','front-palm-right','front-palm-left',closed=True)
        self.add_polyline('rear-fingers',(6,25),(18,6),(22,10),(19,18),(30,10))
        self.add_arc('rear-palm',(6,25),(15,33),radius_x=12,sweep=False)
        self.relate('connect','rear-fingers','rear-palm')
        self.relate('connect','rear-palm','front')
