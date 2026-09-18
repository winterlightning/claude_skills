"""House with short isolated facade stroke and broad overhanging roof. No inferred full doorway. Centerline4,8–44,40.
Construction reference: house.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='40ae9091-ac10-4c02-88bc-c04028f85e36'
SOURCE_PATH='/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/interface-essential/house_40ae9091-ac10-4c02-88bc-c04028f85e36.svg'
SAVED_REFERENCE_PATH='/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/house_40ae9091-ac10-4c02-88bc-c04028f85e36.svg'
EXPORTED_REFERENCE_PATH='work/brief-exports/20260918-all-todo-batches-15/batches/batch-015/references/house_40ae9091-ac10-4c02-88bc-c04028f85e36.svg'
AUTHOR='gpt-6'
class BatchIcon(Solo48):
    icon_id='house-with-interior-door-stroke-solo-b015-r02'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/controls"
    aliases=()
    keywords=('house', 'with', 'interior', 'door', 'stroke')
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

        self.add_polyline('roof',(4,24),(8,21),(24,8),(40,21),(44,24))
        self.add_polyline('walls',(8,21),(8,40),(40,40),(40,21));self.relate('connect','roof','walls')
        self.add_line('mark',(24,23),(24,31))
