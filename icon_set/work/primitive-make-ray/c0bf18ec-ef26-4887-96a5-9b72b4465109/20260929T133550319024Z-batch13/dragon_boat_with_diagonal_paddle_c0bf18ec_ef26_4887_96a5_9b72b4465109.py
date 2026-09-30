"""Restore a continuous diagonal paddle and a distinct dragon crest with a smooth hull.
Symbol plan: HRECT_L on SOLO48; named shapes and source arrangement.
Before review: The separated paddle strokes read as stray marks and the dragon lacks a crest.
Construction reference: Lucide square: coherent contours and tangent quarter-circle corners.
Omissions: Paddle grip and blade reduced to a single long shaft; fine face details omitted.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='c0bf18ec-ef26-4887-96a5-9b72b4465109'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__dragon-boat-with-diagonal-paddle/20260929T132621Z-thuan-mac/reference/dragon boat_c0bf18ec-ef26-4887-96a5-9b72b4465109.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='dragon-boat-with-diagonal-paddle'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='primitives-generate'
    aliases=()
    keywords=('dragon', 'boat')
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
        path('boat',(4,17),[('L',(4,9)),('L',(10,9)),('L',(13,8)),('L',(18,8)),('A',(24,18),6,10,True),('L',(20,27)),('L',(44,27)),('A',(34,40),10,13,True),('L',(14,40)),('A',(4,30),10,10,True),('B',(12,21),(4,26),(12,24)),('A',(8,17),4,4,False),('L',(4,17))],True)
        line('paddle',(36,8),(27,40));join('paddle','boat')
