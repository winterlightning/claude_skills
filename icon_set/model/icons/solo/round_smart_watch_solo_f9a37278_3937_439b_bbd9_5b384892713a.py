"""Round Smart Watch: standalone SOLO48 reconstruction.
Source render supplies essential parts and arrangement. Lucide construction
reference and ownership plan are recorded in build. Original artwork preserved.
"""
from ._base import Solo48
from ...keyshapes import Keyshape
from ._symmetry_curves import path, ellipse, box, contacts
SOURCE_ICON_ID = 'f9a37278-3937-439b-bbd9-5b384892713a'
SOURCE_PATH = 'pictographic-primitives/devices/smart watch circle_f9a37278-3937-439b-bbd9-5b384892713a.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'round-smart-watch-solo'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'devices'
    categories = ('primitives', 'devices')
    aliases = ('Round Smart Watch',)
    keywords = ('round', 'smart', 'watch')
    def build(self):
        # Face and paired tapering straps share exact symmetric attachment nodes.
        # VRECT_M leaves strap length; Lucide watch supplies face/strap ownership.
        # A slightly flattened face reserves visible clearance within each strap.
        path(self,'face',(10,24),
            ('C',(10,21),(12,18),(14,16)),
            ('C',(19,12),(29,12),(34,16)),
            ('C',(36,18),(38,21),(38,24)),
            ('C',(38,27),(36,30),(34,32)),
            ('C',(29,36),(19,36),(14,32)),
            ('C',(12,30),(10,27),(10,24)),closed=True)
        for label,a,b,end in [('top',16,4,16),('bottom',32,44,32)]:
            self.add_polyline(label,(14,a),(18,b),(30,b),(34,end))
            self.relate('connect','face',label)
