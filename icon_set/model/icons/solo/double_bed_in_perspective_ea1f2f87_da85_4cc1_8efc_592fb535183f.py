"""Double Bed in Perspective.

Plan: Mirrored headboard and divided pillows above widening foot. Bounds (6,6)-(42,42).
Construction: Lucide bed-double front frame; source trapezoidal mattress perspective.
Reduction: Single pillow divider; blanket boundary retained, no doubled edges.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = 'ea1f2f87-da85-4cc1-8efc-592fb535183f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/hotels/hotel double bed 1_ea1f2f87-da85-4cc1-8efc-592fb535183f.svg'
AUTHOR = 'gpt-6'


class IconDoubleBedInPerspective(Solo48):
    icon_id = 'double-bed-in-perspective'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'hotels'
    categories = ('hotels', 'primitives')
    aliases = ()
    keywords = ('double', 'bed', 'in', 'perspective')

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
        path('headboard',(10,20),[('L',(10,10)),('A',(14,6),4,4,True),('L',(24,6)),('L',(34,6)),('A',(38,10),4,4,True),('L',(38,20))])
        path('bed',(10,20),[('L',(24,20)),('L',(38,20)),('L',(42,34)),('L',(6,34)),('L',(10,20))],True);self.relate('connect','headboard','bed')
        self.add_line('pillows',(24,6),(24,20));self.relate('connect','pillows','headboard');self.relate('connect','pillows','bed')
        for x in [6,42]:self.add_line('leg'+str(x),(x,34),(x,42));self.relate('connect','leg'+str(x),'bed')
