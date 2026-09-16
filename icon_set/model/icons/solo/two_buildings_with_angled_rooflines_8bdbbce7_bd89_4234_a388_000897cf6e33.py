"""Two Buildings with Angled Rooflines.

Plan: SQUARE centerlines (6,6)-(42,42); low left roof slopes into a shared partition; taller right roof ascends diagonally to its high right corner. Two attached windows and a short roof mast preserve the source.
Construction references: Lucide building-2: adjoining structural volumes and shared wall intersections.
Reduction: Shortened the left window; retained both sloping roof planes and the roof-mounted mast.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '8bdbbce7-bd89-4234-a388-000897cf6e33'
SOURCE_PATH = 'pictographic-primitives/building/buildings_8bdbbce7-bd89-4234-a388-000897cf6e33.svg'
SOURCE_ICON_IDS = ('8bdbbce7-bd89-4234-a388-000897cf6e33',)
SOURCE_PATHS = ('pictographic-primitives/building/buildings_8bdbbce7-bd89-4234-a388-000897cf6e33.svg',)
AUTHOR = 'gpt-6'


class TwoBuildingsWithAngledRooflines(Solo48):
    icon_id = 'two-buildings-with-angled-rooflines'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'building'
    aliases = ()
    keywords = ('two', 'buildings', 'with', 'angled', 'rooflines')

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

        self.add_polyline("buildings",(6,42),(6,34),(6,26),(14,26),(18,30),(18,18),(30,12),(42,6),(42,26),(42,42),(30,42),(18,42),closed=True)
        self.add_line("partition",(18,30),(18,42))
        self.relate("connect","partition","buildings")
        self.add_line("mast",(30,6),(30,12))
        self.relate("connect","mast","buildings")
        self.add_line("left-window",(6,34),(10,34))
        self.add_line("right-window",(30,26),(42,26))
        for k in ("left-window","right-window"):self.relate("connect",k,"buildings")
