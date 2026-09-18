"""Fingerprint with nested open arches and uneven descending ridge ends. Three clear ridge levels replace tiny lower branches. Centerline8,4–40,44.
Lucide construction reference: No useful exact Lucide match.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='05e357f1-918a-47c6-833b-e84768b61f3b'
SOURCE_PATH='/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/fingerprint_05e357f1-918a-47c6-833b-e84768b61f3b.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/other/fingerprint_05e357f1-918a-47c6-833b-e84768b61f3b.svg'
EXPORTED_REFERENCE_PATH='work/brief-exports/20260918-all-todo-batches-15/batches/batch-018/references/fingerprint_05e357f1-918a-47c6-833b-e84768b61f3b.svg'
AUTHOR='gpt-6'
class BatchIcon(Solo48):
    icon_id='fingerprint-with-branching-ridges-solo-b018'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/everyday"
    aliases=()
    keywords=('fingerprint', 'with', 'branching', 'ridges')
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

        path('outer',(8,25),[('L',(8,20)),('A',16,16,True,(24,4)),('A',16,16,True,(40,20)),('L',(40,26))])
        path('middle',(10,39),[('B',(17,34),(17,29),(17,20)),('A',7,7,True,(24,13)),('A',7,7,True,(31,20)),('B',(31,31),(33,35),(38,38))])
        path('inner',(21,44),[('B',(23,42),(24,39),(24,36))])
