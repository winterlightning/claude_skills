"""Horizontal closed fist with left wrist opening, folded thumb and stacked right knuckles. Three finger divisions retain curled-hand identity with open spacing. Centerline4,8–44,40. Human reference simple rounded anatomy.
Lucide construction reference: hand-fist; human_ref/user.svg.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='f9cc745f-989b-5241-9fd0-090475a8c137'
SOURCE_PATH='/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/hand fist bump_f9cc745f-989b-5241-9fd0-090475a8c137.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/other/hand fist bump_f9cc745f-989b-5241-9fd0-090475a8c137.svg'
EXPORTED_REFERENCE_PATH='work/brief-exports/20260918-all-todo-batches-15/batches/batch-018/references/hand fist bump_f9cc745f-989b-5241-9fd0-090475a8c137.svg'
AUTHOR='gpt-6'
class BatchIcon(Solo48):
    icon_id='clenched-fist-solo-b018'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    aliases=()
    keywords=('clenched', 'fist')
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

        path('outline',(4,15),[('L',(10,15)),('B',(16,15),(16,8),(24,8)),('L',(36,8)),('A',8,8,True,(44,16)),('L',(44,32)),('A',8,8,True,(36,40)),('L',(24,40)),('B',(17,40),(15,34),(10,34)),('L',(4,34))])
        path('thumb',(36,8),[('L',(36,18)),('A',8,8,True,(28,26)),('L',(20,26))]);self.relate('connect','outline','thumb')
        self.add_line('finger',(36,32),(44,32));self.relate('connect','outline','finger')
