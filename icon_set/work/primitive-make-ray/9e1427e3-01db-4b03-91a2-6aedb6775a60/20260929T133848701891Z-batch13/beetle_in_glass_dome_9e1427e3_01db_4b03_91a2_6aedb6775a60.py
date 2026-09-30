"""Restore a tall beetle body with three pairs of legs inside the display dome.
Symbol plan: SQUARE on SOLO48; named shapes and source arrangement.
Before review: The squat wing case, detached-looking head and missing legs read as a person rather than a beetle.
Construction reference: Lucide bug: elongated body and three leg pairs; source dome retained.
Omissions: Wing seam and separate antennae omitted to preserve six legs.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='9e1427e3-01db-4b03-91a2-6aedb6775a60'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__beetle-in-glass-dome/20260929T132621Z-thuan-mac/reference/insectarium_9e1427e3-01db-4b03-91a2-6aedb6775a60.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='beetle-in-glass-dome'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='primitives-generate'
    aliases=()
    keywords=('insectarium',)
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
        path('dome',(6,42),[('L',(6,24)),('A',(42,24),18,18,True),('L',(42,42)),('L',(6,42))],True)
        path('body',(20,24),[('A',(28,24),4,7,True),('L',(28,30)),('A',(20,30),4,3,True),('L',(20,24))],True)
        for side in (-1,1):
            x=24+side*4
            for k,y,ox,oy in [('upper',24,8,19),('middle',27,9,27),('lower',30,9,33)]:
                line(f'leg-{side}-{k}',(x,y),(24+side*ox,oy));join(f'leg-{side}-{k}','body')
