"""Use a circular sweep and larger clean downward arrowhead around the central ring.
Symbol plan: SQUARE on SOLO48; named shapes and source arrangement.
Before review: The refresh loop is an uneven narrow oval with a cramped arrowhead. No separate original is available.
Construction reference: Lucide refresh-ccw: coherent circular sweep with an attached open head.
Omissions: 
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='9f429b74-95d6-5824-a8ce-c00437cdaaeb'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__circular-refresh-arrow-upload-46ba7fc835accd08/20260929T132621Z-thuan-mac/reference/circular-refresh-arrow-upload-46ba7fc835accd08_9f429b74-95d6-5824-a8ce-c00437cdaaeb.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='circular-refresh-arrow-upload-46ba7fc835accd08'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='primitives-generate'
    aliases=()
    keywords=('circular-refresh-arrow-upload-46ba7fc835accd08',)
    def build(self):

        def path(n,start,steps,closed=False):
            p=start; members=[]
            for i,step in enumerate(steps):
                k,end,*a=step; name=f'{n}-{i}'
                if k=='L': self.add_line(name,p,end)
                elif k=='A': self.add_arc(name,p,end,radius_x=a[0],radius_y=a[1],sweep=a[2])
                elif k=='B': self.add_bezier(name,p,(a[0],a[1],end))
                members.append(name);p=end
            self.add_contour(n,*members,closed=closed)
        def circle(n,x,y,r):
            path(n,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
        def box(n,l,t,r,b,k=4):
            path(n,(l+k,t),[('L',(r-k,t)),('A',(r,t+k),k,k,True),('L',(r,b-k)),('A',(r-k,b),k,k,True),('L',(l+k,b)),('A',(l,b-k),k,k,True),('L',(l,t+k)),('A',(l+k,t),k,k,True)],True)
        def line(n,a,b): self.add_line(n,a,b)
        def poly(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
        def join(a,b): self.relate('connect',a,b)
        path('loop',(24,42),[('A',(42,24),18,18,False),('A',(24,6),18,18,False),('A',(6,24),18,18,False)])
        poly('head',(6,16),(6,24),(12,24));join('head','loop')
        circle('hub',24,24,4)
