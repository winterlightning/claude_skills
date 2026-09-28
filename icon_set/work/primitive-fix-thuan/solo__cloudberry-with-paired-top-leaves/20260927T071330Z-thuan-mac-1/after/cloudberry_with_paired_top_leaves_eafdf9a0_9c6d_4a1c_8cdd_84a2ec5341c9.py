"""Fresh SOLO48 revision of cloudberry-with-paired-top-leaves from the claimed reference.

The original and rejected drawing were compared before this construction.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._symmetry_curves import path, ellipse, box, line, poly, contacts
from icon_set.model.icons.solo._payments_batch02 import small_dollar

SOURCE_ICON_ID = 'eafdf9a0-9c6d-4a1c-8cdd-84a2ec5341c9'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__cloudberry-with-paired-top-leaves/20260927T071330Z-thuan-mac-1/reference/cloud berry_eafdf9a0-9c6d-4a1c-8cdd-84a2ec5341c9.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'cloudberry-with-paired-top-leaves'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('cloudberry', 'berry', 'fruit', 'leaf', 'cluster', 'stem', 'food')

    def build(self) -> None:

        path(self,'fruit',(24,18),('C',(17,15),(8,19),(8,26)),
             ('C',(8,31),(11,34),(16,34)),('C',(12,39),(17,44),(24,44)),
             ('C',(31,44),(36,39),(32,34)),('C',(37,34),(40,31),(40,26)),
             ('C',(40,19),(31,15),(24,18)),closed=True)
        poly(self,'leaf-left',(24,18),(12,4),(20,8))
        poly(self,'leaf-right',(24,18),(28,8),(36,4))
        self.add_dot('center',(24,29))
        contacts(self)
