"""Two Modern Buildings with Rounded Roofs.

Plan: HRECT centerlines (4,8)-(44,40); low left and tall right blocks share one partition and baseline, with radius4 upper roof corners and one door/window per block.
Construction references: Lucide building-2: adjoining structural volumes and sparse attached window marks.
Reduction: Simplified each small outlined doorway to one rounded vertical stroke.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = 'c49793fa-8cd5-528a-8278-f97b65b7e6a6'
SOURCE_PATH = 'pictographic-primitives/building/building modern_c49793fa-8cd5-528a-8278-f97b65b7e6a6.svg'
SOURCE_ICON_IDS = ('c49793fa-8cd5-528a-8278-f97b65b7e6a6',)
SOURCE_PATHS = ('pictographic-primitives/building/building modern_c49793fa-8cd5-528a-8278-f97b65b7e6a6.svg',)
AUTHOR = 'gpt-6'


class TwoModernBuildingsWithRoundedRoofs(Solo48):
    icon_id = 'two-modern-buildings-with-rounded-roofs'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'building'
    aliases = ()
    keywords = ('two', 'modern', 'buildings', 'with', 'rounded', 'roofs')

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

        path("buildings",(4,40),[("L",(4,28)),("L",(4,24)),("A",(8,20),4,4,True),("L",(24,20)),("L",(24,12)),("A",(28,8),4,4,True),("L",(40,8)),("A",(44,12),4,4,True),("L",(44,18)),("L",(44,40)),("L",(34,40)),("L",(24,40)),("L",(16,40)),("L",(4,40))],True)
        self.add_line("partition",(24,20),(24,40))
        self.relate("connect","partition","buildings")
        for name,start,end in [("left-window",(4,28),(10,28)),("right-window",(44,18),(36,18)),("left-door",(16,40),(16,36)),("right-door",(34,40),(34,32))]:
            self.add_line(name,start,end)
            self.relate("connect",name,"buildings")
