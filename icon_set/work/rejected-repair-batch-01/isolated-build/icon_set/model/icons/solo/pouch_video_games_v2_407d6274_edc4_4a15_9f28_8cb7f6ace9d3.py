'pouch-video-games: independent smooth-curve repair.\n\nConstruction: Drawstring pouch with a broad rounded bowl and a simple tied mouth.\nKeyshape: VRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/shopping-bag.svg and atomic-debug/shopping-bag.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '407d6274-edc4-4a15-9f28-8cb7f6ace9d3'
SOURCE_PATH = 'pictographic-primitives/video-games/pouch_407d6274-edc4-4a15-9f28-8cb7f6ace9d3.svg'
AUTHOR = 'gpt-6'


class PouchVideoGamesVariant2(Solo48):
    icon_id = 'pouch-video-games-v2'
    variant_of = 'pouch-video-games'
    variant_label = 'Smooth curves and symmetry'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video-games'
    aliases = ()
    keywords = ('pouch', 'video-games')
    keyshape = Keyshape.VRECT_L

    def build(self):
        path(self,'bag',(18,14),('C',(14,20),(8,30),(8,35)),('C',(8,41),(15,44),(24,44)),('C',(33,44),(40,41),(40,35)),('C',(40,30),(34,20),(30,14)))
        path(self,'mouth',(18,14),('L',(15,8)),('C',(13,4),(18,4),(24,4)),('C',(30,4),(35,4),(33,8)),('L',(30,14)),('L',(18,14)),closed=True)
        contacts(self)
