"""Cellar Stair beneath Arch.

Plan: VRECT centerlines (8,4)-(40,44); concentric radius16/radius8 doorway arches over two equal8-unit stair risers and a broad threshold.
Construction references: Supplied arched stairwell reference; Lucide house informs shared structural nodes.
Reduction: Reduced the staircase to two clear rises, preserving the nested arch and threshold.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '17afd34b-46b4-4fa1-ad76-6bf7386ace3a'
SOURCE_PATH = 'pictographic-primitives/building/cellar stair_17afd34b-46b4-4fa1-ad76-6bf7386ace3a.svg'
SOURCE_ICON_IDS = ('17afd34b-46b4-4fa1-ad76-6bf7386ace3a',)
SOURCE_PATHS = ('pictographic-primitives/building/cellar stair_17afd34b-46b4-4fa1-ad76-6bf7386ace3a.svg',)
AUTHOR = 'gpt-6'


class CellarStairBeneathArch(Solo48):
    icon_id = 'cellar-stair-beneath-arch'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'building'
    categories = ('building', 'primitives')
    aliases = ()
    keywords = ('cellar', 'stair', 'beneath', 'arch')

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

        path("outer-arch",(8,44),[("L",(8,20)),("A",(40,20),16,16,True),("L",(40,44))])
        path("inner-arch",(16,44),[("L",(16,36)),("L",(16,20)),("A",(32,20),8,8,True),("L",(32,28)),("L",(32,36)),("L",(32,44))])
        self.add_polyline("threshold",(8,44),(16,44),(24,44),(32,44),(40,44))
        for k in ("outer-arch","inner-arch"):self.relate("connect",k,"threshold")
        self.add_polyline("steps",(16,36),(24,36),(24,28),(32,28))
        self.relate("connect","steps","inner-arch")
        self.add_line("tread",(24,36),(32,36))
        self.relate("connect","tread","steps")
        self.relate("connect","tread","inner-arch")
