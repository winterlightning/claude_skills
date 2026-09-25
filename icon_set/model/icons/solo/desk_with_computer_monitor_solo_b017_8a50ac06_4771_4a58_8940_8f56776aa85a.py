"""Office desk with left monitor, right drawer pedestal and two detached document marks. Centerline6,6–42,42; monitor stand meets desk.
Lucide construction reference: monitor.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='8a50ac06-4771-4a58-8940-8f56776aa85a'
SOURCE_PATH='/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/office/desk document base work_8a50ac06-4771-4a58-8940-8f56776aa85a.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/office/desk document base work_8a50ac06-4771-4a58-8940-8f56776aa85a.svg'
EXPORTED_REFERENCE_PATH='work/brief-exports/20260918-all-todo-batches-15/batches/batch-017/references/desk document base work_8a50ac06-4771-4a58-8940-8f56776aa85a.svg'
AUTHOR='gpt-6'
class BatchIcon(Solo48):
    icon_id='desk-with-computer-monitor-solo-b017'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "office"
    aliases=()
    keywords=('desk', 'with', 'computer', 'monitor')
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

        self.add_polyline('monitor',(6,6),(24,6),(24,22),(15,22),(6,22),closed=True)
        self.add_line('stand',(15,22),(15,30));self.relate('connect','monitor','stand')
        self.add_polyline('desk',(6,42),(6,30),(15,30),(30,30),(42,30),(42,42),(30,42),(30,30));self.relate('connect','desk','stand')
        for y in (10,18):self.add_line('paper'+str(y),(33,y),(42,y))
