'smile-upside-down: independent smooth-curve repair.\n\nConstruction: Upside-down smile with identical eyes and one true half-ellipse mouth.\nKeyshape: CIRCLE; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/circle.svg and atomic-debug/circle.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'ee72f06c-87a6-550e-be06-374ee3412ed3'
SOURCE_PATH = 'pictographic-primitives/smileys/smile upside down_ee72f06c-87a6-550e-be06-374ee3412ed3.svg'
AUTHOR = 'gpt-6'


class SmileUpsideDown(Solo48):
    icon_id = 'smile-upside-down'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    categories = ('smileys', 'primitives')
    aliases = ()
    keywords = ('smile', 'upside', 'down', 'smileys')
    keyshape = Keyshape.CIRCLE

    def build(self):
        ellipse(self,'face',24,24,20)
        path(self,'mouth',(13,20),('A',11,5,True,(35,20)))
        self.add_dot('eye-left',(18,31));self.add_dot('eye-right',(30,31))
        contacts(self)
