"""Three Buildings with Pointed Roofs.

Plan: HRECT centerlines (4,8)-(44,40); three adjoining roof profiles, tallest centered tower, short mast and one deliberate diagonal façade division.
Construction references: Lucide building-2: adjoining volumes and shared structural walls; source controls the three distinct roof shapes.
Reduction: Omitted the tiny left doorway to preserve the narrow façade opening.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = 'dfe068ca-5778-593f-aa0a-c638b540bc5f'
SOURCE_PATH = 'pictographic-primitives/building/building modern_dfe068ca-5778-593f-aa0a-c638b540bc5f.svg'
SOURCE_ICON_IDS = ('dfe068ca-5778-593f-aa0a-c638b540bc5f',)
SOURCE_PATHS = ('pictographic-primitives/building/building modern_dfe068ca-5778-593f-aa0a-c638b540bc5f.svg',)
AUTHOR = 'gpt-6'


class ThreeBuildingsWithPointedRoofs(Solo48):
    icon_id = 'three-buildings-with-pointed-roofs'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'building'
    aliases = ()
    keywords = ('three', 'buildings', 'with', 'pointed', 'roofs')

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

        self.add_polyline("central-tower",(16,40),(16,30),(16,24),(16,22),(24,12),(32,22),(32,32),(32,40),closed=True)
        self.add_line("mast",(24,8),(24,12))
        self.relate("connect","mast","central-tower")
        self.add_line("roof-base",(16,22),(32,22))
        self.relate("connect","roof-base","central-tower")
        self.add_polyline("left-building",(16,24),(4,30),(4,40),(16,40))
        self.add_polyline("right-building",(32,32),(38,26),(44,32),(44,40),(32,40))
        for k in ("left-building","right-building"):self.relate("connect",k,"central-tower")
        self.add_line("diagonal-facade",(16,30),(32,40))
        self.relate("connect","diagonal-facade","central-tower")
