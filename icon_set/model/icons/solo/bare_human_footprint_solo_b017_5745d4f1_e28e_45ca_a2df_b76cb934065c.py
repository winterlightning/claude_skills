"""Bare footprint with broad toe pad, large big toe and rounded heel. Tiny individual toe notches merged into gently scalloped upper edge. Centerline10,4–38,44. Human reference informs simple organic anatomy.
Lucide construction reference: human_ref/user.svg; no useful exact Lucide match.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='5745d4f1-e28e-45ca-a2df-b76cb934065c'
SOURCE_PATH='/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/foot_5745d4f1-e28e-45ca-a2df-b76cb934065c.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/other/foot_5745d4f1-e28e-45ca-a2df-b76cb934065c.svg'
EXPORTED_REFERENCE_PATH='work/brief-exports/20260918-all-todo-batches-15/batches/batch-017/references/foot_5745d4f1-e28e-45ca-a2df-b76cb934065c.svg'
AUTHOR='gpt-6'
class BatchIcon(Solo48):
    icon_id='bare-human-footprint-solo-b017'
    keyshape=Keyshape.VRECT_M
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    aliases=()
    keywords=('bare', 'human', 'footprint')
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

        path('foot',(10,12),[('B',(10,4),(12,4),(16,4)),('B',(20,4),(20,9),(20,10)),('B',(23,5),(27,7),(28,12)),('B',(34,8),(38,13),(38,18)),('B',(38,23),(32,26),(32,34)),('B',(32,41),(29,44),(24,44)),('B',(17,44),(15,39),(16,33)),('B',(18,27),(12,24),(12,20)),('L',(10,12))],True)
