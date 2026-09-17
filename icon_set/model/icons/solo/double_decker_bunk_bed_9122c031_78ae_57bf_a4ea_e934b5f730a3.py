"""Double Decker Bunk Bed.

Plan: Two bed bands share upright posts; repeated pillow divisions and optional right ladder. Bounds (6,6)-(42,42).
Construction: Lucide bed and bed-double shared rail and post construction; source bunks.
Reduction: Single rail strokes replace mattress bands; pillows become vertical divisions.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '9122c031-78ae-57bf-a4ea-e934b5f730a3'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/hotels/hotel bunk bed_9122c031-78ae-57bf-a4ea-e934b5f730a3.svg'
AUTHOR = 'gpt-6'


class IconDoubleDeckerBunkBed(Solo48):
    icon_id = 'double-decker-bunk-bed'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'hotels'
    aliases = ()
    keywords = ('double', 'decker', 'bunk', 'bed')

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
        for x in [6,42]:
         path('post'+str(x),(x,6),[('L',(x,14)),('L',(x,30)),('L',(x,42))])
        for y in [14,30]:
         path('bed'+str(y),(6,y),[('L',(16,y)),('L',(32,y)),('L',(42,y))]);self.relate('connect','bed'+str(y),'post6');self.relate('connect','bed'+str(y),'post42')
         path('pillow'+str(y),(6,y-8),[('L',(12,y-8)),('A',(16,y-4),4,4,True),('L',(16,y))]);self.relate('connect','pillow'+str(y),'post6');self.relate('connect','pillow'+str(y),'bed'+str(y))
