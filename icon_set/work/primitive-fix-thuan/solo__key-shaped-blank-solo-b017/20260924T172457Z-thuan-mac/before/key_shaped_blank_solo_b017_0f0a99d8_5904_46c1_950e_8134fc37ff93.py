"""Toothless key blank with broad diagonal shaft and round bow. Tiny bow dot retained, no teeth invented. Centerline6,6–42,42.
Lucide construction reference: key-round.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='0f0a99d8-5904-46c1-950e-8134fc37ff93'
SOURCE_PATH='/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/key 2_0f0a99d8-5904-46c1-950e-8134fc37ff93.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/other/key 2_0f0a99d8-5904-46c1-950e-8134fc37ff93.svg'
EXPORTED_REFERENCE_PATH='work/brief-exports/20260918-all-todo-batches-15/batches/batch-017/references/key 2_0f0a99d8-5904-46c1-950e-8134fc37ff93.svg'
AUTHOR='gpt-6'
class BatchIcon(Solo48):
    icon_id='key-shaped-blank-solo-b017'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/everyday"
    aliases=()
    keywords=('key', 'shaped', 'blank')
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

        path('key',(28,25),[('L',(42,11)),('L',(42,6)),('L',(34,6)),('L',(20,20)),('B',(12,17),(6,23),(6,30)),('A',12,12,False,(18,42)),('B',(27,42),(33,32),(28,25))],True)
        self.add_dot('hole',(17,31))
