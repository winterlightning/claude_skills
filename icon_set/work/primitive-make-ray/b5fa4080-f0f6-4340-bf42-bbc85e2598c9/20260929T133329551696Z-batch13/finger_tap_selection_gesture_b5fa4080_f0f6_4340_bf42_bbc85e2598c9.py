"""Extend the rounded fingertip and restore a semicircular touch halo below the direction chevron.
Symbol plan: VRECT_L on SOLO48; named shapes and source arrangement.
Before review: Outer tap halo is a shallow brow and the fingertip is too short.
Construction reference: No useful exact Lucide match; source fingertip and concentric halo construction.
Omissions: 
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='b5fa4080-f0f6-4340-bf42-bbc85e2598c9'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__finger-tap-selection-gesture/20260929T132621Z-thuan-mac/reference/finger tap_b5fa4080-f0f6-4340-bf42-bbc85e2598c9.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='finger-tap-selection-gesture'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='primitives-generate'
    aliases=()
    keywords=('finger', 'tap')
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
        poly('chevron',(16,4),(24,12),(32,4))
        path('halo',(8,36),[('L',(8,34)),('A',(40,34),16,14,True),('L',(40,36))])
        path('finger',(20,44),[('L',(20,33)),('A',(28,33),4,4,True),('L',(28,44))])
