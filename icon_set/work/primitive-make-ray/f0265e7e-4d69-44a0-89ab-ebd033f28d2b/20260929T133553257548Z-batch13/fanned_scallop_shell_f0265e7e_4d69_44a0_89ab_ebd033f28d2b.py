"""Restore three detached fanning ribs and a broad scalloped rim above the hinge.
Symbol plan: SQUARE on SOLO48; named shapes and source arrangement.
Before review: Single central division makes the shell look like a leaf or shield.
Construction reference: Lucide square: coherent contours and tangent quarter-circle corners.
Omissions: Fine outer ribs and hinge tabs omitted; three ribs retain the fan.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='f0265e7e-4d69-44a0-89ab-ebd033f28d2b'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__fanned-scallop-shell/20260929T132621Z-thuan-mac/reference/clam_f0265e7e-4d69-44a0-89ab-ebd033f28d2b.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='fanned-scallop-shell'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='primitives-generate'
    aliases=()
    keywords=('clam',)
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
        path('shell',(24,42),[('L',(9,30)),('A',(6,24),6,6,True),('A',(12,15),6,9,True),('A',(18,9),6,6,True),('A',(30,9),6,3,True),('A',(36,15),6,6,True),('A',(42,24),6,9,True),('A',(39,30),6,6,True),('L',(24,42))],True)
        line('rib-center',(24,16),(24,31))
        line('rib-left',(14,20),(16,24));line('rib-right',(34,20),(32,24))
