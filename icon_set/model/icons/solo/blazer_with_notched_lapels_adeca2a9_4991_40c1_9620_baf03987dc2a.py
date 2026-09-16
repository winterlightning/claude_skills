"""Blazer with Notched Lapels.

Plan: SQUARE centerlines (6,6)-(42,42); mirrored long sleeves and notched lapels converge at one front fastening; one open outline preserves the jacket silhouette.
Construction references: Lucide shirt: symmetric shoulders, coherent outer garment contour; supplied blazer owns the lapel/notch pattern.
Reduction: Omitted buttons, pockets and duplicate inner lapel edges; shortened sleeve seams to keep the lapels clear.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = 'adeca2a9-4991-40c1-9620-baf03987dc2a'
SOURCE_PATH = 'pictographic-primitives/clothes/blazer_adeca2a9-4991-40c1-9620-baf03987dc2a.svg'
SOURCE_ICON_IDS = ('adeca2a9-4991-40c1-9620-baf03987dc2a',)
SOURCE_PATHS = ('pictographic-primitives/clothes/blazer_adeca2a9-4991-40c1-9620-baf03987dc2a.svg',)
AUTHOR = 'gpt-6'


class BlazerWithNotchedLapels(Solo48):
    icon_id = 'blazer-with-notched-lapels'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'clothes'
    aliases = ()
    keywords = ('blazer', 'with', 'notched', 'lapels')

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

        axis=24
        self.add_polyline("jacket",(18,6),(8,10),(6,42),(16,42),(24,38),(32,42),(42,42),(40,10),(30,6))
        for side in (-1,1):
            point=lambda x,y:(axis+side*x,y)
            k=f"lapel-{side}"
            self.add_polyline(k,point(6,6),point(8,14),point(4,18),point(8,22),(axis,32))
            self.relate("connect","jacket",k)
            self.add_line(f"sleeve-{side}",point(8,34),point(8,42))
            self.relate("connect","jacket",f"sleeve-{side}")
        self.relate("connect","lapel--1","lapel-1")
        self.add_line("front-fastening",(axis,32),(axis,38))
        self.relate("connect","front-fastening","jacket")
        for side in (-1,1): self.relate("connect","front-fastening",f"lapel-{side}")
