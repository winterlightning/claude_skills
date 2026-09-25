"""Globe framework with central meridian, equator and splayed stand. Extra curved meridians/latitudes omitted to keep four clear panels. Centerline8,4–40,44.
Construction reference: globe.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='04ec5404-f235-5ca7-ac4c-23f5bc014d24'
SOURCE_PATH='/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/kids/playground globe_04ec5404-f235-5ca7-ac4c-23f5bc014d24.svg'
SAVED_REFERENCE_PATH='/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/kids/playground globe_04ec5404-f235-5ca7-ac4c-23f5bc014d24.svg'
EXPORTED_REFERENCE_PATH='work/brief-exports/20260918-all-todo-batches-15/batches/batch-016/references/playground globe_04ec5404-f235-5ca7-ac4c-23f5bc014d24.svg'
AUTHOR='gpt-6'
class BatchIcon(Solo48):
    icon_id='globe-framework-on-legs-solo-b016-r02'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "kids"
    aliases=()
    keywords=('globe', 'framework', 'on', 'legs')
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

        circle('globe',24,20,16)
        self.add_polyline('equator',(8,20),(24,20),(40,20));self.add_polyline('meridian',(24,4),(24,20),(24,36))
        for n in ('equator','meridian'):self.relate('connect',n,'globe')
        self.relate('connect','equator','meridian')
        self.add_polyline('stand',(10,44),(24,36),(38,44));self.relate('connect','stand','globe');self.relate('connect','stand','meridian')
