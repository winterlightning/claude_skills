"""Segmented spring arch built from concentric upper semicircles and vertical feet; top seam and two side seams share endpoints. Individual coils omitted as in source. Centerline4,8–44,40.
Lucide construction reference: No useful exact Lucide match.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='adb3af2d-d45b-443f-893f-729c0e49861d'
SOURCE_PATH='/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/kids/slinky physics spring toy_adb3af2d-d45b-443f-893f-729c0e49861d.svg'
SAVED_REFERENCE_PATH='/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/kids/slinky physics spring toy_adb3af2d-d45b-443f-893f-729c0e49861d.svg'
EXPORTED_REFERENCE_PATH='work/brief-exports/20260918-all-todo-batches-15/batches/batch-015/references/slinky physics spring toy_adb3af2d-d45b-443f-893f-729c0e49861d.svg'
AUTHOR='gpt-6'
class BatchIcon(Solo48):
    icon_id='arched-spring-toy-solo-b015'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/controls"
    aliases=()
    keywords=('arched', 'spring', 'toy')
    def build(self):

        def circle(n,x,y,r):
            pts=((x-r,y),(x,y-r),(x+r,y),(x,y+r));members=[]
            for i in range(4):
                m=n+str(i);self.add_arc(m,pts[i],pts[(i+1)%4],radius_x=r);members.append(m)
            self.add_contour(n,*members,closed=True)
        def path(n,start,commands,closed=False):
            p=start;members=[]
            for i,c in enumerate(commands):
                m=n+str(i);q=c[-1]
                if c[0]=='L':self.add_line(m,p,q)
                elif c[0]=='A':self.add_arc(m,p,q,radius_x=c[1],radius_y=c[2],sweep=c[3])
                elif c[0]=='B':self.add_bezier(m,p,(c[1],c[2],q))
                members.append(m);p=q
            self.add_contour(n,*members,closed=closed)

        path('arch',(4,40),[('L',(4,28)),('A',20,20,True,(24,8)),('A',20,20,True,(44,28)),('L',(44,40)),('L',(32,40)),('L',(32,28)),('A',8,8,False,(24,20)),('A',8,8,False,(16,28)),('L',(16,40)),('L',(4,40))],True)
        for n,a,b in [('top',(24,8),(24,20)),('left',(4,28),(16,28)),('right',(32,28),(44,28))]:
         self.add_line(n,a,b);self.relate('connect','arch',n)
