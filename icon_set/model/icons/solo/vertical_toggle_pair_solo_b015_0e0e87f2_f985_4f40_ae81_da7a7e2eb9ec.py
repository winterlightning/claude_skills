"""Paired vertical controls. Narrow pill widths preclude a hollow knob with clearance, so left knob reduced to a round mark; right retains attached divider. Centerline6,6–42,42.
Lucide construction reference: toggle-left.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='0e0e87f2-f985-4f40-ae81-da7a7e2eb9ec'
SOURCE_PATH='/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/interface-essential/settings toggle vertical_0e0e87f2-f985-4f40-ae81-da7a7e2eb9ec.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/settings toggle vertical_0e0e87f2-f985-4f40-ae81-da7a7e2eb9ec.svg'
EXPORTED_REFERENCE_PATH='work/brief-exports/20260918-all-todo-batches-15/batches/batch-015/references/settings toggle vertical_0e0e87f2-f985-4f40-ae81-da7a7e2eb9ec.svg'
AUTHOR='gpt-6'
class BatchIcon(Solo48):
    icon_id='vertical-toggle-pair-solo-b015'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/controls"
    aliases=()
    keywords=('vertical', 'toggle', 'pair')
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

        self.add_polyline('left',(4,8),(20,8),(20,40),(4,40),closed=True)
        path('right',(32,8),[('L',(40,8)),('A',4,4,True,(44,12)),('L',(44,27)),('L',(44,36)),('A',4,4,True,(40,40)),('L',(32,40)),('A',4,4,True,(28,36)),('L',(28,27)),('L',(28,12)),('A',4,4,True,(32,8))],True)
        self.add_dot('knob',(12,30))
        self.add_line('divider',(28,27),(44,27));self.relate('connect','right','divider')
