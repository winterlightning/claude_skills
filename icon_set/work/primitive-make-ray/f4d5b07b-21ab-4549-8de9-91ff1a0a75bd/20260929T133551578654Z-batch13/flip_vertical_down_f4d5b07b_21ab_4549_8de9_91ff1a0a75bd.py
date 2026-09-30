"""Restore the rounded upper panel and horizontal fold axis around a curved down arrow.
Symbol plan: SQUARE on SOLO48; named shapes and source arrangement.
Before review: The source panel has been omitted, leaving only a down arrow and two dots.
Construction reference: Lucide square: coherent contours and tangent quarter-circle corners.
Omissions: 
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='f4d5b07b-21ab-4549-8de9-91ff1a0a75bd'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__flip-vertical-down/20260929T132621Z-thuan-mac/reference/flip vertical down_f4d5b07b-21ab-4549-8de9-91ff1a0a75bd.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='flip-vertical-down'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='primitives-generate'
    aliases=()
    keywords=('flip', 'vertical', 'down')
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
        path('panel',(6,24),[('L',(6,10)),('A',(10,6),4,4,True),('L',(38,6)),('A',(42,10),4,4,True),('L',(42,24))])
        line('axis-left',(6,24),(12,24));join('axis-left','panel')
        line('axis-right',(34,24),(42,24));join('axis-right','panel')
        path('arrow',(25,16),[('B',(24,42),(18,25),(20,33))])
        poly('head',(15,35),(24,42),(31,33));join('head','arrow')
