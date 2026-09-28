"""Open piercing ring around detached centered captive bead. Outer radius20 centered24,24; bead radius4 at24,40.
Lucide construction reference: No useful exact Lucide match.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='d636ad65-cbbd-4a17-b0a1-2f5b484460f7'
SOURCE_PATH='/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/circle top circle_d636ad65-cbbd-4a17-b0a1-2f5b484460f7.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/other/circle top circle_d636ad65-cbbd-4a17-b0a1-2f5b484460f7.svg'
EXPORTED_REFERENCE_PATH='work/brief-exports/20260918-all-todo-batches-15/batches/batch-018/references/circle top circle_d636ad65-cbbd-4a17-b0a1-2f5b484460f7.svg'
AUTHOR='gpt-6'
class BatchIcon(Solo48):
    icon_id='captive-bead-piercing-ring-solo-b018'
    keyshape=Keyshape.CIRCLE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    categories = ("container", "other", "primitives-generate")
    aliases=()
    keywords=('captive', 'bead', 'piercing', 'ring')
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

        self.add_arc('ring',(8,36),(40,36),radius_x=20,large_arc=True,sweep=True)
        circle('bead',24,40,4)
