"""Two people form a folded balance, with an upper bent body above a lower supporting pose.

Kept both heads, the folded upper silhouette and lower U-shaped support. Dense overlapping outlines were reduced.
Source fixes the two-person arrangement; Lucide person-standing informs separated heads and coherent limbs.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '672c58c9-cf49-5d74-ba11-e6398667c047'
SOURCE_PATH = 'pictographic-primitives/sports/acro yoga pose_672c58c9-cf49-5d74-ba11-e6398667c047.svg'
AUTHOR = 'gpt-6'

class AcroYogaFoldedBalance(Solo48):
    icon_id = 'acro-yoga-folded-balance'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/sports"
    aliases = ()
    keywords = ('acro', 'yoga', 'folded', 'balance')

    def circle(self, name, x, y, radius):
        self.add_arc(name+'-top',(x-radius,y),(x+radius,y),radius_x=radius)
        self.add_arc(name+'-bottom',(x+radius,y),(x-radius,y),radius_x=radius)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

    def skeleton(self, branches):
        # Declare only actual shared endpoints in the physical figure.
        segments=[]
        for name,points in branches:
            for index,(a,b) in enumerate(zip(points,points[1:])):
                key=f'{name}-{index}'
                self.add_line(key,a,b);segments.append((key,a,b))
            if len(points)>2:self.add_contour(name,*[f'{name}-{i}' for i in range(len(points)-1)])
        for index,(a,p,q) in enumerate(segments):
            for b,r,s in segments[index+1:]:
                if p in (r,s) or q in (r,s):self.relate('connect',a,b)

    def oval(self,name,x,y,rx,ry):
        self.add_arc(name+'-top',(x-rx,y),(x+rx,y),radius_x=rx,radius_y=ry)
        self.add_arc(name+'-bottom',(x+rx,y),(x-rx,y),radius_x=rx,radius_y=ry)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

    def build(self):
        # Two people form a folded balance, with an upper bent body above a lower supporting pose.
        self.circle('lower-head',9,39,3)
        self.circle('upper-head',39,24,3)
        self.add_polyline('folded-body',(6,16),(26,6),(26,18),(12,22))
        self.add_polyline('supporting-body',(26,18),(24,34),(24,42),(42,42),(42,36))
        self.relate('connect','supporting-body-1','folded-body-2')
        self.relate('connect','supporting-body-1','folded-body-3')
