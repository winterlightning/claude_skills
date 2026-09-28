"""Fresh SOLO48 revision of clam-shell from the claimed reference.

The original and rejected drawing were compared before this construction.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._symmetry_curves import path, ellipse, box, line, poly, contacts
from icon_set.model.icons.solo._payments_batch02 import small_dollar

SOURCE_ICON_ID = 'a23c6ef9-fd90-57c7-ae12-5006686062cd'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__clam-shell/20260927T071330Z-thuan-mac-1/reference/shell_a23c6ef9-fd90-57c7-ae12-5006686062cd.svg'
AUTHOR = "gpt-6"

class ClamShell(Solo48):
    icon_id = 'clam-shell'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    categories = ('animals', 'primitives')
    aliases = ()
    keywords = ('shell', 'clam', 'mussel', 'oyster', 'sea', 'beach', 'bivalve', 'marine')

    def build(self) -> None:

        # Side-facing fan shell, with the narrow tip at the right of the source.
        path(self,'shell',(42,24),('C',(34,13),(24,6),(18,8)),
             ('C',(10,10),(8,18),(6,24)),('C',(8,30),(10,38),(18,40)),
             ('C',(24,42),(34,35),(42,24)),closed=True)
        line(self,'center-rib',(6,24),(30,24))
        line(self,'upper-rib',(11,16),(30,24))
        line(self,'lower-rib',(11,32),(30,24))
        contacts(self)
