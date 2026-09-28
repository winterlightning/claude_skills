"""Fresh SOLO48 revision of closed-fist from the claimed reference.

The original and rejected drawing were compared before this construction.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._symmetry_curves import path, ellipse, box, line, poly, contacts
from icon_set.model.icons.solo._payments_batch02 import small_dollar

SOURCE_ICON_ID = '398a358b-6ba9-5507-b8f7-6dfcb7f136d1'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__closed-fist/20260927T071330Z-thuan-mac-1/reference/hand fist bump_398a358b-6ba9-5507-b8f7-6dfcb7f136d1.svg'
AUTHOR = 'gpt-6'

class ClosedFist(Solo48):
    icon_id = 'closed-fist'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'wayfinding'
    categories = ('wayfinding', 'primitives')
    aliases = ()
    keywords = ('fist', 'hand', 'knuckles', 'gesture', 'closed', 'thumb')

    def build(self) -> None:

        # Rounded fist with four stacked knuckles and a curled thumb.
        path(self,'fist',(44,16),('L',(38,16)),('A',12,8,False,(26,8)),
             ('L',(12,8)),('A',8,8,False,(4,16)),('L',(4,32)),
             ('A',8,8,False,(12,40)),('L',(26,40)),
             ('A',12,8,False,(38,32)),('L',(44,32)))
        path(self,'thumb',(26,8),('A',8,12,False,(18,20)),
             ('A',8,8,False,(26,28)),('L',(34,28)))
        for i,y in enumerate((18,26,34)):
            line(self,f'finger-{i}',(4,y),(12,y))
        contacts(self)
