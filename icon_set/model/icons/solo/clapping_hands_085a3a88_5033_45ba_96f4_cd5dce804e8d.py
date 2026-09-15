# Refinement: Widen the back palm between its outer edge and the front thumb.
# Repair: Replace the rear hand zigzag with one broad raised finger; use exact shared thumb and palm contacts between the clapping hands.
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
        from ._symmetry_curves import path, ellipse, line, poly, contacts

        path(self,'front',(15,33),('L',(15,23)),('A',4,4,True,(19,19)),('A',4,4,True,(23,23)),('L',(23,29)),('L',(34,13)),('A',5,5,True,(42,17)),('L',(34,32)),('A',10,10,True,(24,42)),('A',9,9,True,(15,33)),closed=True)
        poly(self,'rear-fingers',(6,25),(11,6),(26,6),(19,19))
        path(self,'rear-palm',(6,25),('A',12,12,False,(15,33)))
        contacts(self)
