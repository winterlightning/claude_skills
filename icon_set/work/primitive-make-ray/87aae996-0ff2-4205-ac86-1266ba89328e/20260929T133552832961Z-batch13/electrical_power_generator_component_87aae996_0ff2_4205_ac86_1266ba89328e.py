"""Reconnect the insulator and base, restoring paired lightning strokes.
Symbol plan: HRECT_L on SOLO48; named shapes and source arrangement.
Before review: The central machine is disconnected and both identifying lightning bolts are missing.
Construction reference: Lucide square: coherent contours and tangent quarter-circle corners.
Omissions: Bolt outlines reduced to zigzag sparks and central ribs reduced to two.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='87aae996-0ff2-4205-ac86-1266ba89328e'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__electrical-power-generator-component/20260929T132621Z-thuan-mac/reference/elecricity power_87aae996-0ff2-4205-ac86-1266ba89328e.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='electrical-power-generator-component'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='primitives-generate'
    aliases=()
    keywords=('elecricity', 'power')
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
        box('cap',18,8,30,16,4)
        line('column',(24,16),(24,32));join('column','cap')
        line('rib',(18,24),(30,24));join('rib','column')
        poly('base',(14,40),(14,32),(24,32),(34,32),(34,40),(14,40),closed=True);join('column','base')
        poly('left-bolt',(8,8),(4,19),(10,19),(6,29))
        poly('right-bolt',(42,8),(38,19),(44,19),(40,29))
