"""Building with Six Narrow Windows.

Plan: VRECT centerlines (8,4)-(40,44); trapezoid roof above a three-column, two-row series of exactly six short windows and a centered door. Shared pitches8 horizontally and10 vertically.
Construction references: Lucide building: regular repeated window series inside one coherent structural façade.
Reduction: Shortened window and doorway marks to preserve all six windows with legal clearance.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '5e8f5a5b-e11d-504a-a164-59272de1b158'
SOURCE_PATH = 'pictographic-primitives/building/building_5e8f5a5b-e11d-504a-a164-59272de1b158.svg'
SOURCE_ICON_IDS = ('5e8f5a5b-e11d-504a-a164-59272de1b158',)
SOURCE_PATHS = ('pictographic-primitives/building/building_5e8f5a5b-e11d-504a-a164-59272de1b158.svg',)
AUTHOR = 'gpt-6'


class BuildingWithSixNarrowWindows(Solo48):
    icon_id = 'building-with-six-narrow-windows'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'building'
    aliases = ()
    keywords = ('building', 'with', 'six', 'narrow', 'windows')

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

        self.add_polyline("roof",(8,12),(12,4),(36,4),(40,12),(8,12))
        self.add_polyline("building",(8,12),(8,44),(24,44),(40,44),(40,12))
        self.relate("connect","roof","building")
        for row,y in enumerate((20,30)):
            for col,x in enumerate((16,24,32)):
                self.add_line(f"window-{row}-{col}",(x,y),(x,y+2))
        self.add_line("door",(24,40),(24,44))
        self.relate("connect","door","building")
