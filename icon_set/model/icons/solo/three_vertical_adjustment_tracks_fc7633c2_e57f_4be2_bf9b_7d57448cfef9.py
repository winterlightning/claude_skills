"""Three Vertical Adjustment Tracks — batch 51."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'fc7633c2-e57f-4be2-bf9b-7d57448cfef9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/slider vertical alternative_fc7633c2-e57f-4be2-bf9b-7d57448cfef9.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-vertical-adjustment-tracks'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    categories = ("interface-essential", "primitives")
    aliases = ()
    keywords = ('three', 'vertical', 'adjustment', 'tracks')

    def build(self):
        # Plan: three equally spaced upright tracks with staggered horizontal controls.
        # SQUARE extremes6,6,42,42. Lucide sliders-vertical informs gap placement.
        for i,(x,y) in enumerate(((10,16),(24,32),(38,16))):
            self.add_polyline(f'mark-{i}',(x-4,y),(x,y),(x+4,y))
            if i==0:
                self.add_polyline('left-track',(x,6),(x,y),(x,42));self.relate('connect','left-track',f'mark-{i}')
            elif i==1:
                self.add_line('middle-top',(x,6),(x,y-8));self.add_line('middle-bottom',(x,y),(x,42));self.relate('connect','middle-bottom',f'mark-{i}')
            else:
                self.add_line('right-top',(x,6),(x,y));self.add_line('right-bottom',(x,y+8),(x,42));self.relate('connect','right-top',f'mark-{i}')


    def circle(self,n,x,y,r,attachments=()):
        from math import atan2
        pts=list(dict.fromkeys([(x+r,y),(x,y+r),(x-r,y),(x,y-r)]+list(attachments)))
        pts.sort(key=lambda p:atan2(p[1]-y,p[0]-x))
        for j in range(len(pts)):self.add_arc(f'{n}-{j}',pts[j],pts[(j+1)%len(pts)],radius_x=r)
        self.add_contour(n,*[f'{n}-{j}' for j in range(len(pts))],closed=True)

    def box(self,n,x,y,w,h,attachments=()):
        corners=[(x,y),(x+w,y),(x+w,y+h),(x,y+h)];nodes=[]
        for a,z in zip(corners,corners[1:]+corners[:1]):
            dx,dy=z[0]-a[0],z[1]-a[1]
            inside=[p for p in attachments if (p[0]-a[0])*dy==(p[1]-a[1])*dx and 0<(p[0]-a[0])*dx+(p[1]-a[1])*dy<dx*dx+dy*dy]
            inside.sort(key=lambda p:(p[0]-a[0])*dx+(p[1]-a[1])*dy);nodes.extend([a]+inside)
        self.add_polyline(n,*nodes,closed=True)

