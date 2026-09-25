"""Eco bulb with integrated leaf filament reaching bottom. Broad rounded bulb, curved pointed leaf and simple base. Centerline8,4–40,44.
Lucide construction reference: lightbulb; sprout.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='2a85d964-aa75-5541-b5f6-debca7c0ccfe'
SOURCE_PATH='/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/lights/light bulb eco_2a85d964-aa75-5541-b5f6-debca7c0ccfe.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/lights/light bulb eco_2a85d964-aa75-5541-b5f6-debca7c0ccfe.svg'
EXPORTED_REFERENCE_PATH='work/brief-exports/20260918-all-todo-batches-15/batches/batch-016/references/light bulb eco_2a85d964-aa75-5541-b5f6-debca7c0ccfe.svg'
AUTHOR='gpt-6'
class BatchIcon(Solo48):
    icon_id='light-bulb-with-leaf-filament-solo-b016'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "lights"
    aliases=()
    keywords=('light', 'bulb', 'with', 'leaf', 'filament')
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

        path('bulb',(16,36),[('B',(16,30),(8,26),(8,20)),('A',16,16,True,(24,4)),('A',16,16,True,(40,20)),('B',(40,26),(32,30),(32,36)),('L',(32,40)),('A',4,4,True,(28,44)),('L',(20,44)),('A',4,4,True,(16,40)),('L',(16,36))],True)
        self.add_polyline('base',(16,36),(24,36),(32,36));self.relate('connect','bulb','base')
        path('leaf',(24,27),[('B',(18,25),(19,17),(28,15)),('B',(28,24),(28,28),(24,27))],True)
        self.add_line('stem',(24,27),(24,36));self.relate('connect','leaf','stem');self.relate('connect','base','stem')
