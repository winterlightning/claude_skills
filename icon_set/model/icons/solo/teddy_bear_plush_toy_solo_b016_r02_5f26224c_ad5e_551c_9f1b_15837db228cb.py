"""Seated plush bear silhouette with rounded ears, soft arms and broad paired feet. Mirrored contour about24; facial and overlapping body seams omitted. Centerline6,6–42,42.
Construction reference: No useful exact Lucide match; supplied reference.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='5f26224c-ad5e-551c-9f1b-15837db228cb'
SOURCE_PATH='/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/kids/toys teddy bear_5f26224c-ad5e-551c-9f1b-15837db228cb.svg'
SAVED_REFERENCE_PATH='/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/kids/toys teddy bear_5f26224c-ad5e-551c-9f1b-15837db228cb.svg'
EXPORTED_REFERENCE_PATH='work/brief-exports/20260918-all-todo-batches-15/batches/batch-016/references/toys teddy bear_5f26224c-ad5e-551c-9f1b-15837db228cb.svg'
AUTHOR='gpt-6'
class BatchIcon(Solo48):
    icon_id='teddy-bear-plush-toy-solo-b016-r02'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "kids"
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

        path('bear',(13,6),[('B',(18,6),(18,10),(20,10)),('B',(22,9),(26,9),(28,10)),('B',(30,10),(30,6),(35,6)),('B',(41,6),(40,13),(36,15)),('B',(36,19),(34,22),(31,24)),('B',(36,24),(42,25),(42,29)),('B',(42,33),(37,34),(35,34)),('B',(40,37),(38,42),(32,42)),('B',(28,42),(27,38),(24,38)),('B',(21,38),(20,42),(16,42)),('B',(10,42),(8,37),(13,34)),('B',(11,34),(6,33),(6,29)),('B',(6,25),(12,24),(17,24)),('B',(14,22),(12,19),(12,15)),('B',(8,13),(7,6),(13,6))],True)
