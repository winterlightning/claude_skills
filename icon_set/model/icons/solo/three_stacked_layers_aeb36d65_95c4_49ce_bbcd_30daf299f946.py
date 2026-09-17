"""Three Stacked Layers — batch 51."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'aeb36d65-95c4-49ce-bbcd-30daf299f946'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/keyboard command_aeb36d65-95c4-49ce-bbcd-30daf299f946.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-stacked-layers'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    aliases = ()
    keywords = ('three', 'stacked', 'layers')

    def build(self):
        # Plan: complete top diamond plus two repeated lower front edges.
        # SQUARE extremes6,6,42,42. Lucide layers informs occluded lower outlines.
        self.add_polyline('top',(24,6),(42,14),(24,22),(6,14),closed=True)
        for i,y in enumerate((24,34)):self.add_polyline(f'lower-{i}',(6,y),(24,y+8),(42,y))


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

