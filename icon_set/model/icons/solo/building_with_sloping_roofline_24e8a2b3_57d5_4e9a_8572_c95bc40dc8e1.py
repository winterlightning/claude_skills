"""Building with Sloping Roofline.

Plan: SQUARE centerlines (6,6)-(42,42); descending roof plane and vertical façade divider share an exact roof intersection. Asymmetry preserves the architectural perspective.
Construction references: Lucide building-2: structural partitions sharing exact wall nodes; source supplies the sloping roof.
Reduction: None.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '24e8a2b3-57d5-4e9a-8572-c95bc40dc8e1'
SOURCE_PATH = 'pictographic-primitives/building/building_24e8a2b3-57d5-4e9a-8572-c95bc40dc8e1.svg'
SOURCE_ICON_IDS = ('24e8a2b3-57d5-4e9a-8572-c95bc40dc8e1',)
SOURCE_PATHS = ('pictographic-primitives/building/building_24e8a2b3-57d5-4e9a-8572-c95bc40dc8e1.svg',)
AUTHOR = 'gpt-6'


class BuildingWithSlopingRoofline(Solo48):
    icon_id = 'building-with-sloping-roofline'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'building'
    categories = ('building', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('building', 'with', 'sloping', 'roofline')

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

        self.add_polyline("building",(6,6),(24,14),(42,22),(42,30),(42,42),(24,42),(6,42),closed=True)
        self.add_polyline("divider",(24,6),(24,14),(24,42))
        self.relate("connect","divider","building")
        self.add_line("window",(34,30),(42,30))
        self.relate("connect","window","building")
