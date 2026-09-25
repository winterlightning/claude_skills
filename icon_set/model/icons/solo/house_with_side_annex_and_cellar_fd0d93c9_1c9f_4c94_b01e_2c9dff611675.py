"""House with Side Annex and Cellar.

Plan: SQUARE centerlines (6,6)-(42,42); a gabled house stands above a deliberate stepped underground contour with a flat cellar floor. Shared floor and wall nodes keep the section coherent.
Construction references: Lucide house: simple gable and structural walls; source controls the below-ground staircase and annex.
Reduction: Omitted the small square window to prioritize the roof, ground and cellar steps.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = 'fd0d93c9-1c9f-4c94-b01e-2c9dff611675'
SOURCE_PATH = 'pictographic-primitives/building/cellar_fd0d93c9-1c9f-4c94-b01e-2c9dff611675.svg'
SOURCE_ICON_IDS = ('fd0d93c9-1c9f-4c94-b01e-2c9dff611675',)
SOURCE_PATHS = ('pictographic-primitives/building/cellar_fd0d93c9-1c9f-4c94-b01e-2c9dff611675.svg',)
AUTHOR = 'gpt-6'


class HouseWithSideAnnexAndCellar(Solo48):
    icon_id = 'house-with-side-annex-and-cellar'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'building'
    categories = ('building', 'primitives')
    aliases = ()
    keywords = ('house', 'with', 'side', 'annex', 'and', 'cellar')

    def build(self) -> None:
        def path(name, start, commands, closed=False):
            members=[]
            here=start
            for i,command in enumerate(commands):
                k=f"{name}-{i}"
                kind,end,*args=command
                if kind=="L": self.add_line(k,here,end)
                elif kind=="A": self.add_arc(k,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=="C": self.add_bezier(k,here,(args[0],args[1],end))
                members.append(k);here=end
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x,y-r),[("A",(x,y+r),r,r,True),("A",(x,y-r),r,r,True)],True)

        self.add_polyline("house",(6,24),(6,14),(18,6),(30,14),(30,26))
        self.add_polyline("annex",(30,14),(42,18),(42,26),(30,26),(22,26))
        self.relate("connect","annex","house")
        self.add_polyline("cellar",(6,24),(14,24),(14,32),(22,32),(22,42),(42,42),(42,26))
        self.relate("connect","cellar","house")
        self.relate("connect","cellar","annex")
