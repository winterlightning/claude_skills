'weights: independent smooth-curve repair.\n\nConstruction: Two matched rounded weight plates joined by a centered bar.\nKeyshape: HRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/dumbbell.svg and atomic-debug/dumbbell.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'e19c45b5-82c3-4520-898b-27160ddd0cc8'
SOURCE_PATH = 'pictographic-primitives/sports/weights_e19c45b5-82c3-4520-898b-27160ddd0cc8.svg'
AUTHOR = 'gpt-6'


class Weights(Solo48):
    icon_id = 'weights'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'sports'
    categories = ('sports', 'primitives')
    aliases = ()
    keywords = ('weights', 'sports')
    keyshape = Keyshape.HRECT_L

    def build(self):
        box(self,'left',8,8,18,40,3,ys=(24,))
        box(self,'right',30,8,40,40,3,ys=(24,))
        line(self,'bar-left',(4,24),(8,24));line(self,'bar-middle',(18,24),(30,24));line(self,'bar-right',(40,24),(44,24))
        contacts(self)
