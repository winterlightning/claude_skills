"""Seated plush bear with round ears, broad blank face, soft arms and symmetric feet. Single silhouette avoids tiny overlapping seams; lower foot division retained. Centerline8,4–40,44.
Lucide construction reference: No useful exact Lucide match.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='5f26224c-ad5e-551c-9f1b-15837db228cb'
SOURCE_PATH='/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/kids/toys teddy bear_5f26224c-ad5e-551c-9f1b-15837db228cb.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/kids/toys teddy bear_5f26224c-ad5e-551c-9f1b-15837db228cb.svg'
EXPORTED_REFERENCE_PATH='work/brief-exports/20260918-all-todo-batches-15/batches/batch-016/references/toys teddy bear_5f26224c-ad5e-551c-9f1b-15837db228cb.svg'
AUTHOR='gpt-6'
class BatchIcon(Solo48):
    icon_id='teddy-bear-plush-toy-solo-b016'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/toys"
    aliases=()
    keywords=('teddy', 'bear', 'plush', 'toy')
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

        path('bear',(14,4),[('B',(18,4),(18,8),(20,8)),('B',(22,7),(26,7),(28,8)),('B',(30,8),(30,4),(34,4)),('B',(40,4),(40,12),(36,14)),('B',(36,18),(34,22),(31,24)),('B',(35,24),(40,25),(40,30)),('B',(40,34),(36,35),(35,36)),('B',(40,40),(38,44),(32,44)),('B',(28,44),(27,40),(24,40)),('B',(21,40),(20,44),(16,44)),('B',(10,44),(8,40),(13,36)),('B',(12,35),(8,34),(8,30)),('B',(8,25),(13,24),(17,24)),('B',(14,22),(12,18),(12,14)),('B',(8,12),(8,4),(14,4))],True)
