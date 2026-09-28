"""Building with Rooftop Pennant.

Plan: SQUARE centerlines (6,6)-(42,42); rectangular façade with paired windows, central doorway and a roof-mounted notched pennant. Flag placement creates intentional asymmetry.
Construction references: Lucide building and flag: sparse façade and a physical flag attached to a pole.
Reduction: Omitted the detached side ground extensions to reserve height for the flag.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '8278f1b6-79b0-5521-9f33-256d4ba28c0f'
SOURCE_PATH = 'pictographic-primitives/building/building flag_8278f1b6-79b0-5521-9f33-256d4ba28c0f.svg'
SOURCE_ICON_IDS = ('8278f1b6-79b0-5521-9f33-256d4ba28c0f',)
SOURCE_PATHS = ('pictographic-primitives/building/building flag_8278f1b6-79b0-5521-9f33-256d4ba28c0f.svg',)
AUTHOR = 'gpt-6'


class BuildingWithRooftopPennant(Solo48):
    icon_id = 'building-with-rooftop-pennant'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'building'
    categories = ('building', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('building', 'with', 'rooftop', 'pennant')

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

        self.add_polyline("building",(6,42),(6,22),(24,22),(42,22),(42,42),(24,42),closed=True)
        self.add_polyline("pole",(24,22),(24,14),(24,6))
        self.relate("connect","building","pole")
        self.add_polyline("pennant",(24,6),(38,6),(34,10),(38,14),(24,14))
        self.relate("connect","pole","pennant")
        for x in (16,32):self.add_line(f"window-{x}",(x,30),(x,32))
        self.add_line("door",(24,36),(24,42))
        self.relate("connect","door","building")
