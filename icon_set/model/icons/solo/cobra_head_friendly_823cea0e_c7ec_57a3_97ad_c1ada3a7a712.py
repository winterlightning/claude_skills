"""Fresh SOLO48 revision of cobra-head-friendly from the claimed reference.

The original and rejected drawing were compared before this construction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from icon_set.model.icons.solo._symmetry_curves import path, ellipse, box, line, poly, contacts
from icon_set.model.icons.solo._payments_batch02 import small_dollar

SOURCE_ICON_ID = '823cea0e-c7ec-57a3-97ad-c1ada3a7a712'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__cobra-head-friendly/20260927T071330Z-thuan-mac-1/reference/cobra-head-friendly_823cea0e-c7ec-57a3-97ad-c1ada3a7a712.svg'
AUTHOR = 'gpt-6'

class CobraHeadFriendly(Solo48):
    icon_id = 'cobra-head-friendly-solo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    categories = ('animals',)
    aliases = ('cobra-head',)
    keywords = ('cobra', 'snake', 'reptile', 'hood', 'head', 'friendly')

    def build(self) -> None:

        path(self,'hood',(24,4),('C',(36,4),(40,10),(40,20)),
             ('C',(40,28),(32,30),(30,34)),('L',(30,44)),
             ('L',(18,44)),('L',(18,34)),
             ('C',(16,30),(8,28),(8,20)),
             ('C',(8,10),(12,4),(24,4)),closed=True)
        self.add_dot('eye-left',(19,16));self.add_dot('eye-right',(29,16))
        poly(self,'mouth',(21,24),(24,28),(27,24))
        contacts(self)
