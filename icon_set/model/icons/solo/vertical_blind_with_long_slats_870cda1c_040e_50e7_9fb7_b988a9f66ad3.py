"""Vertical Blind with Long Slats.

Plan: SQUARE centerlines (6,6)-(42,42); four equally spaced open-bottom slat edges attach to a rectangular structural headrail.
Construction references: Lucide blinds: regular slat spacing; source supplies the vertical orientation.
Reduction: Omitted the tiny upper stem; retained all four long slat edges.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '870cda1c-040e-50e7-9fb7-b988a9f66ad3'
SOURCE_PATH = 'pictographic-primitives/building/blinds vertical closed_870cda1c-040e-50e7-9fb7-b988a9f66ad3.svg'
SOURCE_ICON_IDS = ('870cda1c-040e-50e7-9fb7-b988a9f66ad3',)
SOURCE_PATHS = ('pictographic-primitives/building/blinds vertical closed_870cda1c-040e-50e7-9fb7-b988a9f66ad3.svg',)
AUTHOR = 'gpt-6'


class VerticalBlindWithLongSlats(Solo48):
    icon_id = 'vertical-blind-with-long-slats'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'building'
    categories = ('building', 'primitives')
    aliases = ()
    keywords = ('vertical', 'blind', 'with', 'long', 'slats')

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

        xs=[6+12*i for i in range(4)]
        self.add_polyline("rail",(6,6),(42,6),(42,14),(30,14),(18,14),(6,14),closed=True)
        for i,x in enumerate(xs):
            self.add_line(f"slat-{i}",(x,14),(x,42))
            self.relate("connect","rail",f"slat-{i}")
