"""Electric Desk Fan.

Plan: Circular guard with radial blades, centered pedestal and base. Bounds (8,4)-(40,44).
Construction: Lucide fan radial symmetry; supplied desk stand and guard.
Reduction: Six radial guard divisions share the center; the narrow hub ring is omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '367831cd-f6c5-48ca-959c-5fa137f4001c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/hotels/ventilator_367831cd-f6c5-48ca-959c-5fa137f4001c.svg'
AUTHOR = 'gpt-6'


class IconElectricDeskFan(Solo48):
    icon_id = 'electric-desk-fan'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'hotels'
    aliases = ()
    keywords = ('electric', 'desk', 'fan')

    def build(self):

        def path(name, start, commands, closed=False):
            here=start
            members=[]
            for i, (kind,end,*args) in enumerate(commands):
                k=f"{name}-{i}"
                if kind == "L": self.add_line(k,here,end)
                elif kind == "A": self.add_arc(k,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind == "C": self.add_bezier(k,here,(args[0],args[1],end))
                members.append(k)
                here=end
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[("A",(x+r,y),r,r,True),("A",(x-r,y),r,r,True)],True)
        path('guard',(24,4),[('C',(38,12),(30,4),(35,7)),('C',(40,20),(39,14),(40,17)),('C',(38,28),(40,23),(39,26)),('C',(24,36),(35,33),(30,36)),('C',(10,28),(18,36),(13,33)),('C',(8,20),(9,26),(8,23)),('C',(10,12),(8,17),(9,14)),('C',(24,4),(13,7),(18,4))],True)
        points=[(24,4),(38,12),(38,28),(24,36),(10,28),(10,12)]
        for j,p in enumerate(points):self.add_line('blade'+str(j),(24,20),p);self.relate('connect','blade'+str(j),'guard')
        for a in range(6):
         for b in range(a+1,6):self.relate('connect','blade'+str(a),'blade'+str(b))
        self.add_line('stand',(24,36),(24,44));self.relate('connect','stand','guard')
        path('foot',(14,44),[('L',(24,44)),('L',(34,44))]);self.relate('connect','stand','foot')
