"""Tapping Finger — batch 50."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '0c99403f-bc4d-4901-ad1c-00f4f8aa7bd8'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/touch finger 1_0c99403f-bc4d-4901-ad1c-00f4f8aa7bd8.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'tapping-finger'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    categories = ("interface-essential", "primitives")
    aliases = ()
    keywords = ('tapping', 'finger')

    def build(self):
        # Plan: one raised finger, coherent folded hand and five tap rays.
        # VRECT_L extremes (8,4)-(40,44). Lucide pointer informs the silhouette.
        self.add_line('finger-left',(20,32),(20,20))
        self.add_arc('fingertip',(20,20),(28,20),radius_x=4)
        self.add_line('finger-right',(28,20),(28,28))
        self.add_line('fold-top',(28,28),(32,28))
        self.add_arc('knuckles',(32,28),(40,36),radius_x=8)
        self.add_line('palm',(40,36),(40,44))
        self.add_line('thumb-lower',(20,44),(10,34))
        self.add_bezier('thumb-tip',(10,34),((6,30),(12,24),(16,28)))
        self.add_line('thumb-upper',(16,28),(20,32))
        self.add_contour('hand','thumb-lower','thumb-tip','thumb-upper','finger-left','fingertip','finger-right','fold-top','knuckles','palm')
        for n,a,z in [('top',(24,4),(24,7)),('left',(8,16),(11,16)),('right',(37,16),(40,16)),('up-left',(12,6),(14,8)),('up-right',(34,8),(36,6))]:self.add_line('tap-'+n,a,z)


    def circle(self,n,x,y,r):
        pts=[(x+r,y),(x,y+r),(x-r,y),(x,y-r)]
        for j in range(4): self.add_arc(f'{n}-{j}',pts[j],pts[(j+1)%4],radius_x=r)
        self.add_contour(n,*[f'{n}-{j}' for j in range(4)],closed=True)

    def box(self,n,x,y,w,h,attachments=()):
        corners=[(x,y),(x+w,y),(x+w,y+h),(x,y+h)];nodes=[]
        for a,z in zip(corners,corners[1:]+corners[:1]):
            dx,dy=z[0]-a[0],z[1]-a[1]
            inside=[p for p in attachments if (p[0]-a[0])*dy==(p[1]-a[1])*dx and 0<(p[0]-a[0])*dx+(p[1]-a[1])*dy<dx*dx+dy*dy]
            inside.sort(key=lambda p:(p[0]-a[0])*dx+(p[1]-a[1])*dy);nodes.extend([a]+inside)
        self.add_polyline(n,*nodes,closed=True)

