'keyboard-asterisk-interface-essential: independent smooth-curve repair.\n\nConstruction: Outlined medical cross with equal arm widths and rounded outside corners; re-entrant corners preserve the cross.\nKeyshape: SQUARE; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/plus.svg and atomic-debug/plus.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '4aff3aef-75a6-5746-bf7d-ae18d5b3397e'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__keyboard-asterisk-interface-essential/20260927T070927Z-thuan-mac-1/reference/keyboard asterisk_4aff3aef-75a6-5746-bf7d-ae18d5b3397e.svg'
AUTHOR = 'gpt-6'


class KeyboardAsteriskInterfaceEssential(Solo48):
    icon_id = 'keyboard-asterisk-interface-essential'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('keyboard', 'asterisk', 'interface-essential')
    keyshape = Keyshape.SQUARE

    def build(self):
        # Even four-unit rounds restore the reference's pill-ended plus outline.
        path(self,'cross',(22,6),('L',(26,6)),('A',4,4,True,(30,10)),
             ('L',(30,18)),('L',(38,18)),('A',4,4,True,(42,22)),
             ('L',(42,26)),('A',4,4,True,(38,30)),('L',(30,30)),
             ('L',(30,38)),('A',4,4,True,(26,42)),('L',(22,42)),
             ('A',4,4,True,(18,38)),('L',(18,30)),('L',(10,30)),
             ('A',4,4,True,(6,26)),('L',(6,22)),
             ('A',4,4,True,(10,18)),('L',(18,18)),('L',(18,10)),
             ('A',4,4,True,(22,6)),closed=True)
        contacts(self)
