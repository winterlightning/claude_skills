'gold: independent smooth-curve repair.\n\nConstruction: Three stacked gold ingots with shared trapezoid proportions and a central joined base.\nKeyshape: HRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/boxes.svg and atomic-debug/boxes.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '60218d13-a329-4988-b2f7-354732a0478e'
SOURCE_PATH = 'pictographic-primitives/science/gold_60218d13-a329-4988-b2f7-354732a0478e.svg'
AUTHOR = 'gpt-6'


class Gold(Solo48):
    icon_id = 'gold'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'science'
    aliases = ()
    keywords = ('gold', 'science')
    keyshape = Keyshape.HRECT_L

    def build(self):
        poly(self,'top',(14,22),(18,8),(30,8),(34,22),closed=True)
        poly(self,'bottom-left',(4,40),(8,22),(14,22),(20,22),(24,40),closed=True)
        poly(self,'bottom-right',(24,40),(28,22),(34,22),(40,22),(44,40),closed=True)
        contacts(self)
