"""A four-spoke shutoff handwheel; dense gear teeth and two spokes omitted to open the wheel."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3f19c420-5af0-403b-b4fa-30f604efb1ed'
SOURCE_PATH = 'pictographic-primitives/tools/emergency valve_3f19c420-5af0-403b-b4fa-30f604efb1ed.svg'
AUTHOR = 'gpt-6'

class EmergencyValveWheel(Solo48):
    icon_id = 'emergency-valve-wheel'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/tools"
    aliases = ()
    keywords = ('valve', 'handwheel', 'emergency', 'shutoff', 'wheel', 'gear', 'pipe', 'industrial')

    def build(self) -> None:

        def circle(n, x, y, r):
            self.add_arc(n+'-a', (x-r,y), (x+r,y), radius_x=r)
            self.add_arc(n+'-b', (x+r,y), (x-r,y), radius_x=r)
            self.add_contour(n,n+'-a',n+'-b',closed=True)

        pts=[(24,4),(44,24),(24,44),(4,24)]
        for i in range(4):
            self.add_arc('rim'+str(i),pts[i],pts[(i+1)%4],radius_x=20)
        self.add_contour('rim',*[f'rim{i}' for i in range(4)],closed=True)
        circle('hub',24,24,3)
        for i,(p,q) in enumerate(zip(pts,[(24,21),(27,24),(24,27),(21,24)])):
            self.add_line('spoke'+str(i),p,q)
            self.relate('connect','spoke'+str(i),'rim')
            self.relate('connect','spoke'+str(i),'hub')
