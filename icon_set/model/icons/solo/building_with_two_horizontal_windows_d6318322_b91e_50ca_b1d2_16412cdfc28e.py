"""Building with Two Horizontal Windows.

Plan: SQUARE centerlines (6,6)-(42,42); rounded upper roof, projecting band and ground, paired horizontal windows and a centered door. Window pitch8.
Construction references: Lucide building: coherent façade and sparse repeated window bars.
Reduction: Shortened the door and used one stroke for it to preserve both long windows.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = 'd6318322-b91e-50ca-b1d2-16412cdfc28e'
SOURCE_PATH = 'pictographic-primitives/building/building_d6318322-b91e-50ca-b1d2-16412cdfc28e.svg'
SOURCE_ICON_IDS = ('d6318322-b91e-50ca-b1d2-16412cdfc28e',)
SOURCE_PATHS = ('pictographic-primitives/building/building_d6318322-b91e-50ca-b1d2-16412cdfc28e.svg',)
AUTHOR = 'gpt-6'


class BuildingWithTwoHorizontalWindows(Solo48):
    icon_id = 'building-with-two-horizontal-windows'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'building'
    aliases = ()
    keywords = ('building', 'with', 'two', 'horizontal', 'windows')

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

        path("building",(10,42),[("L",(10,14)),("L",(10,10)),("A",(14,6),4,4,True),("L",(34,6)),("A",(38,10),4,4,True),("L",(38,14)),("L",(38,42))])
        self.add_polyline("roof-band",(6,14),(10,14),(38,14),(42,14))
        self.add_polyline("ground",(6,42),(10,42),(24,42),(38,42),(42,42))
        for k in ("roof-band","ground"):self.relate("connect",k,"building")
        for i,y in enumerate((22,30)):self.add_line(f"window-{i}",(19,y),(29,y))
        self.add_line("door",(24,38),(24,42))
        self.relate("connect","door","ground")
