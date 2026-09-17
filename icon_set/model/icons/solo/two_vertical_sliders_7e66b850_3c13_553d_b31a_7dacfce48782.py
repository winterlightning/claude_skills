"""Two Vertical Sliders — batch 52."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7e66b850-3c13-553d-b31a-7dacfce48782'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/settings vertical_7e66b850-3c13-553d-b31a-7dacfce48782.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'two-vertical-sliders'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    aliases = ()
    keywords = ('two', 'vertical', 'sliders')

    def build(self):
        # Plan: mirrored track positions and equal horizontal capsule knobs, staggered vertically.
        # SQUARE extremes6,6,42,42. Lucide sliders-vertical informs interrupted tracks.
        for n,x,y in [('left',14,17),('right',34,31)]:
            self.add_line(n+'-top-1',(x-4,y-4),(x,y-4));self.add_line(n+'-top-2',(x,y-4),(x+4,y-4))
            self.add_arc(n+'-r',(x+4,y-4),(x+4,y+4),radius_x=4)
            self.add_line(n+'-bottom-1',(x+4,y+4),(x,y+4));self.add_line(n+'-bottom-2',(x,y+4),(x-4,y+4))
            self.add_arc(n+'-l',(x-4,y+4),(x-4,y-4),radius_x=4)
            self.add_contour(n+'-knob',n+'-top-1',n+'-top-2',n+'-r',n+'-bottom-1',n+'-bottom-2',n+'-l',closed=True)
            for suffix,a,z in [('upper',(x,6),(x,y-4)),('lower',(x,y+4),(x,42))]:
                self.add_line(n+suffix,a,z);self.relate('connect',n+suffix,n+'-knob')


    def circle(self,n,x,y,r):
        pts=[(x+r,y),(x,y+r),(x-r,y),(x,y-r)]
        for j in range(4):self.add_arc(f'{n}-{j}',pts[j],pts[(j+1)%4],radius_x=r)
        self.add_contour(n,*[f'{n}-{j}' for j in range(4)],closed=True)

