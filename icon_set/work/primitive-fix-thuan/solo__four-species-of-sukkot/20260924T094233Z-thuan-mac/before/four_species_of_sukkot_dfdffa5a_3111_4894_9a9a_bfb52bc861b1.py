"""Four Species of Sukkot.

Plan: Upright lulav and branching sprig share binding, citron on right. Bounds (6,6)-(42,42); deliberate botanical asymmetry.
Construction: Source bundle and citron; Lucide tree-pine informs simplified branching only.
Reduction: Removed citron interior mark and extra fine branches.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = 'dfdffa5a-3111-4894-9a9a-bfb52bc861b1'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/sukkot feast of tabernacles_dfdffa5a-3111-4894-9a9a-bfb52bc861b1.svg'
AUTHOR = 'gpt-6'


class FourSpeciesOfSukkot(Solo48):
    icon_id = 'four-species-of-sukkot'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "holidays"
    aliases = ()
    keywords = ('four', 'species', 'of', 'sukkot')

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
        self.add_polyline('binding',(6,32),(18,32),(18,42),(6,42),closed=True)
        self.add_polyline('lulav',(18,32),(18,24),(18,6))
        path('palm-leaf',(18,24),[('C',(28,6),(18,14),(22,8))])
        self.relate('connect','lulav','palm-leaf');self.relate('connect','binding','lulav')
        self.add_polyline('twig',(6,12),(6,22),(6,32))
        self.add_line('leaf',(6,22),(12,16))
        self.relate('connect','twig','leaf');self.relate('connect','twig','binding')
        path('citron',(34,23),[('C',(42,32),(40,23),(42,25)),('C',(34,42),(42,38),(39,42)),('C',(28,34),(28,42),(28,38)),('C',(34,23),(28,28),(29,25))],True)
        self.add_line('stem',(34,23),(40,17));self.relate('connect','stem','citron')
