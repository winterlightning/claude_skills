"""Rejected molecule has a flattened angular upper lobe. Restore three rounded lobes and clean internal Y-shaped boundaries.
Symbol plan: shared dimensions and symmetry for paired parts; coherent contours and explicit real junctions.
Construction reference: network; bean.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='d7786532-dbd2-54e1-87e0-f66a8363d821'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__molecule-d7786532/20260928T173014Z-thuan-mac/reference/molecule_d7786532-dbd2-54e1-87e0-f66a8363d821.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    exception = {'reason': 'Preserve three rounded molecular lobes and clean internal Y boundaries. All spacing checks pass. Natural lobed silhouette has a 44px-wide ink envelope instead of the 40px square keyshape, remaining at least 2px inside the canvas. User explicitly delegated exception decisions for UI/UX quality; reviewed at 48px in light and dark.', 'approved_by': 'user-delegated-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '6a2fa995a5ab0450ec8b83cfc2e297d76b2dcf234d2b9d3b4e512dce0ebdecc7'}
    icon_id='molecule-d7786532'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('molecule',)
    def build(self):
        path=self.path;circle=self.circle;box=self.box;line=self.add_line;poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        path('lobes',(12,22),[('A',(24,4),13,True),('A',(36,22),13,True),('C',(44,34),(42,24),(44,28)),('C',(24,40),(44,46),(32,46)),('C',(4,34),(16,46),(4,46)),('C',(12,22),(4,28),(6,24))],True)
        poly('y',(12,22),(24,30),(36,22));line('center',(24,30),(24,40));join('y','lobes');join('center','lobes');join('center','y')


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

