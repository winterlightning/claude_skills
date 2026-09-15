"""Vertical Blind with Teardrop Pull.

Plan: HRECT centerlines (4,8)-(44,40); a structural rail owns repeated vertical panel edges and a genuine teardrop pull at the left.
Construction references: Lucide blinds: sparse slat/cord construction; source controls panel count and teardrop.
Reduction: Squared the structural rail corners; retained the distinguishing pull and panel count.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '1f8784cc-093a-536f-bb6f-73431e3151d9'
SOURCE_PATH = 'pictographic-primitives/building/blinds vertical open_1f8784cc-093a-536f-bb6f-73431e3151d9.svg'
SOURCE_ICON_IDS = ('1f8784cc-093a-536f-bb6f-73431e3151d9',)
SOURCE_PATHS = ('pictographic-primitives/building/blinds vertical open_1f8784cc-093a-536f-bb6f-73431e3151d9.svg',)
AUTHOR = 'gpt-6'


class VerticalBlindWithTeardropPull(Solo48):
    icon_id = 'vertical-blind-with-teardrop-pull'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'building'
    aliases = ()
    keywords = ('vertical', 'blind', 'with', 'teardrop', 'pull')

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

        xs=[22, 33, 44]
        self.add_polyline("rail",(4,8),(44,8),(44,16),*[(x,16) for x in reversed(xs[:-1])],(8,16),(4,16),closed=True)
        self.add_line("cord",(8,16),(8,30))
        self.relate("connect","cord","rail")
        path("pull",(8,30),[("C",(12,36),(10,32),(12,34)),("A",(4,36),4,4,True),("C",(8,30),(4,34),(6,32))],True)
        self.relate("connect","cord","pull")
        for i,x in enumerate(xs):
            self.add_line(f"slat-{i}",(x,16),(x,40))
            self.relate("connect","rail",f"slat-{i}")
