"""Farm Tractor with Plow.
Plan: Right-facing tractor and attached left plow; unequal wheel circles. Extrema (4,8)-(44,40).
Reference: Lucide tractor: unequal wheels, angular cab and spare silhouette.
Reduction: Wheel hub, narrow panel edges and blade double outline omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '927b50de-ee1f-5ffc-89fb-de7063de8ee0'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/farming/plow_927b50de-ee1f-5ffc-89fb-de7063de8ee0.svg'
AUTHOR = 'gpt-6'

class Batch28Icon(Solo48):
    icon_id = 'tractor-trailing-plow-blade'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/agriculture"
    aliases = ()
    keywords = ('farm', 'tractor', 'with', 'plow')

    def build(self):

        self.add_polyline('body',(16,18),(16,8),(26,8),(30,22),(44,22),(44,36))
        for n,x,y,r in (('rear',20,34,6),('front',40,36,4)):
            self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
            self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
            self.add_contour(n,n+'-a',n+'-b',closed=True)
        self.relate('connect','body','front')
        self.add_line('hitch',(14,34),(4,34))
        self.add_bezier('blade',(4,26),((4,30),(4,34),(4,34)),((4,38),(6,40),(6,40)))
        self.relate('connect','rear','hitch');self.relate('connect','hitch','blade')
