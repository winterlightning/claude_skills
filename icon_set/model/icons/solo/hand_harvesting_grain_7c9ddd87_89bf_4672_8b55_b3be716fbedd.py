"""Hand Harvesting Grain.

Plan: Diagonal harvesting hand above horizontal wheat sprig and one ground ledge. Bounds (6,6)-(42,42).
Construction: Human reference style, Lucide hand coherent curved digits; source downward pinch and low wheat.
Reduction: Reduced planting ledges to one; two grain branches remain.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '7c9ddd87-89bf-4672-8b55-b3be716fbedd'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/reishit katzir feast of firstfruits_7c9ddd87-89bf-4672-8b55-b3be716fbedd.svg'
AUTHOR = 'gpt-6'


class HandHarvestingGrain(Solo48):
    icon_id = 'hand-harvesting-grain'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "holidays"
    aliases = ()
    keywords = ('hand', 'harvesting', 'grain')

    def build(self) -> None:

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
        path('hand',(42,6),[('L',(34,6)),('C',(25,12),(30,6),(28,8)),('L',(18,22)),('A',(24,28),5,5,False),('L',(31,21)),('C',(42,14),(36,22),(40,18))])
        self.add_polyline('stalk',(6,28),(14,28),(24,28))
        self.add_line('grain-top',(14,28),(6,20));self.add_line('grain-bottom',(14,28),(6,36))
        self.relate('connect','stalk','grain-top');self.relate('connect','stalk','grain-bottom');self.relate('connect','grain-top','grain-bottom')
        self.relate('connect','stalk','hand')
        path('ground',(14,42),[('L',(42,42))])
