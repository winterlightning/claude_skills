"""Agricultural Combine Harvester.
Plan: Left-facing combine with sloped cab, forward header and unequal circular wheels. Extrema (4,8)-(44,40).
Reference: Lucide tractor: unequal wheels and spare angular vehicle silhouette.
Reduction: Fine interior detail omitted to preserve negative space.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '44ee4e62-4052-5cd9-b8ce-7733bb2ccec0'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/farming/harvester storage_44ee4e62-4052-5cd9-b8ce-7733bb2ccec0.svg'
AUTHOR = 'gpt-6'

class Batch27Icon(Solo48):
    icon_id = 'combine-harvester-front-header'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/agriculture"
    aliases = ()
    keywords = ('agricultural', 'combine', 'harvester')

    def build(self):

        self.add_polyline('body',(12,21),(16,8),(28,8),(28,22),(44,22),(44,36))
        self.add_polyline('outlet',(28,8),(40,8),(44,12))
        self.relate('connect','body','outlet')
        self.add_polyline('header',(4,40),(4,34),(13,34))
        for n,x,y,r in (('front',19,34,6),('rear',40,36,4)):
            self.add_arc(n+'-a',(x+r,y),(x-r,y),radius_x=r)
            self.add_arc(n+'-b',(x-r,y),(x+r,y),radius_x=r)
            self.add_contour(n,n+'-a',n+'-b',closed=True)
        self.relate('connect','body','rear')
        self.relate('connect','header','front')
