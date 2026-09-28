"""House above Two-Step Cellar.

Plan: SQUARE centerlines (6,6)-(42,42); a gabled house stands above a deliberate stepped underground contour with a flat cellar floor. Shared floor and wall nodes keep the section coherent.
Construction references: Lucide house: simple gable and structural walls; source controls the below-ground staircase and annex.
Reduction: Omitted the small square window to prioritize the roof, ground and cellar steps.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '00da3e9c-162a-4c09-86bf-5ba70f170953'
SOURCE_PATH = 'pictographic-primitives/building/cellar_00da3e9c-162a-4c09-86bf-5ba70f170953.svg'
SOURCE_ICON_IDS = ('00da3e9c-162a-4c09-86bf-5ba70f170953',)
SOURCE_PATHS = ('pictographic-primitives/building/cellar_00da3e9c-162a-4c09-86bf-5ba70f170953.svg',)
AUTHOR = 'gpt-6'


class HouseAboveTwoStepCellar(Solo48):
    icon_id = 'house-above-two-step-cellar'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'building'
    categories = ('building', 'primitives')
    aliases = ()
    keywords = ('house', 'above', 'two-step', 'cellar')

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

        self.add_polyline("roof",(14,16),(26,6),(38,16))
        self.add_polyline("house",(14,16),(14,26),(38,26),(38,16))
        self.relate("connect","roof","house")

        self.add_polyline("ground",(38,26),(42,26),(42,42),(22,42),(22,34),(6,34),(6,26))
        self.relate("connect","house","ground")
