"""Rejected cube is flattened into a layered hexagon. Restore three tall equal isometric faces with clean central Y junction.
Symbol plan: shared dimensions and symmetry for paired parts; coherent contours and explicit real junctions.
Construction reference: box.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='802601c0-689d-481d-86cd-d13aceeaf9a1'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__cube/20260928T173014Z-thuan-mac/reference/cube_802601c0-689d-481d-86cd-d13aceeaf9a1.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    exception = {'reason': 'Preserve the source tall isometric cube and three equal readable faces. Its ink extends 2px above and below the square keyshape, while remaining 2px inside the canvas. All spacing checks pass. User explicitly delegated exception decisions for UI/UX quality; reviewed at 48px in light and dark.', 'approved_by': 'user-delegated-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': 'aa7ff44a2b6697566be289c34f44884b3e1639bb1fb00f1f34536c3f0cab3ca7'}
    icon_id='cube'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('cube',)
    def build(self):
        path=self.path;circle=self.circle;box=self.box;line=self.add_line;poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        poly('outline',(24,4),(42,14),(42,34),(24,44),(6,34),(6,14),closed=True)
        poly('faces',(6,14),(24,24),(42,14));line('vertical',(24,24),(24,44))
        join('faces','outline');join('vertical','outline');join('vertical','faces')


    def path(self,n,start,commands,closed=False):
        ids=[]
        for i,c in enumerate(commands):
            ident=f'{n}-{i}';k,end,*a=c
            if k=='L':self.add_line(ident,start,end)
            elif k=='A':self.add_arc(ident,start,end,radius_x=a[0],sweep=a[1])
            elif k=='E':self.add_arc(ident,start,end,radius_x=a[0],radius_y=a[1],sweep=a[2])
            elif k=='C':self.add_bezier(ident,start,(a[0],a[1],end))
            ids.append(ident);start=end
        self.add_contour(n,*ids,closed=closed)
    def circle(self,n,x,y,r):
        self.path(n,(x,y-r),[('A',(x+r,y),r,True),('A',(x,y+r),r,True),('A',(x-r,y),r,True),('A',(x,y-r),r,True)],True)
    def box(self,n,l,t,r,b,q):
        self.path(n,(l+q,t),[('L',(r-q,t)),('A',(r,t+q),q,True),('L',(r,b-q)),('A',(r-q,b),q,True),('L',(l+q,b)),('A',(l,b-q),q,True),('L',(l,t+q)),('A',(l+q,t),q,True)],True)

