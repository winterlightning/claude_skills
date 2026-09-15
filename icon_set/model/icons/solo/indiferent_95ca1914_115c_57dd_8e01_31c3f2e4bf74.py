'indiferent: independent smooth-curve repair.\n\nConstruction: Neutral face with equal eyes and a level mouth; complete circle replaces the lumpy outline.\nKeyshape: CIRCLE; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/circle.svg and atomic-debug/circle.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '95ca1914-115c-57dd-8e01-31c3f2e4bf74'
SOURCE_PATH = 'pictographic-primitives/smileys/indiferent_95ca1914-115c-57dd-8e01-31c3f2e4bf74.svg'
AUTHOR = 'gpt-6'


class Indiferent(Solo48):
    icon_id = 'indiferent'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('indiferent', 'smileys')
    keyshape = Keyshape.CIRCLE

    def build(self):
        ellipse(self,'face',24,24,20)
        line(self,'eye-left',(15,18),(19,18));line(self,'eye-right',(29,18),(33,18))
        line(self,'mouth',(16,30),(32,30))
        contacts(self)
