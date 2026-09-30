"""Lengthen the F bars and use a small open hub with a clean diagonal needle.
Symbol plan: HRECT_L on SOLO48; named shapes and source arrangement.
Before review: The F labels have very short bars and the needle hub fills in.
Construction reference: Lucide gauge: smooth arc and diagonal indicator; source F labels preserved.
Omissions: Diagonal outer tick omitted to preserve space.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='18728730-c932-5c2a-bbae-5f3d79009993'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__gas-f/20260929T132822Z-thuan-mac/reference/gas f_18728730-c932-5c2a-bbae-5f3d79009993.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='gas-f'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='primitives-generate'
    aliases=()
    keywords=('gas', 'f')
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
        path('arch',(4,24),[('A',(24,8),20,16,True),('A',(44,24),20,16,True)])
        line('tick',(24,8),(24,12));join('tick','arch')
        for x in (4,44):line(f'end-{x}',(x,24),(x+(4 if x==4 else -4),24));join(f'end-{x}','arch')
        circle('hub',24,25,3);line('needle',(27,25),(32,18));join('needle','hub')
        for x in (6,34):
            poly(f'f-{x}',(x,40),(x,32),(x+8,32))
            line(f'fbar-{x}',(x,40),(x+6,40));join(f'fbar-{x}',f'f-{x}')
