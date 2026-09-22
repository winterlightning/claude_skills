"""Empty Vertical Battery: standalone SOLO48 reconstruction.
Source render supplies essential parts and arrangement. Lucide construction
reference and ownership plan are recorded in build. Original artwork preserved.
"""
from ._base import Solo48
from ...keyshapes import Keyshape
from ._symmetry_curves import path, ellipse, box, contacts
SOURCE_ICON_ID = '10b617a1-d67b-49a8-9559-604c636a0780'
SOURCE_PATH = 'pictographic-primitives/electronics/single cell battery_10b617a1-d67b-49a8-9559-604c636a0780.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'empty-vertical-battery-solo'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'electronics'
    aliases = ('Empty Vertical Battery',)
    keywords = ('empty', 'vertical', 'battery')
    def build(self):
        # Centered terminal attaches at split top-wall nodes; body is one rounded box.
        # VRECT_M preserves upright cell proportions. Lucide battery informs box flow.
        box(self,'body',10,14,38,44,3,xs=(18,30))
        path(self,'terminal',(18,14),('L',(18,7)),('A',3,3,True,(21,4)),
             ('L',(27,4)),('A',3,3,True,(30,7)),('L',(30,14)))
        self.relate('connect','body','terminal')
