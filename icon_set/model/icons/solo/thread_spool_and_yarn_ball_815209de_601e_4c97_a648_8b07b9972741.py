"""Thread Spool and Yarn Ball.

Plan: HRECT centerlines (4,8)-(44,40); spool with projecting rims touches a circular radius12 yarn ball at one exact side node. A sweeping winding and two projecting knitting needles identify the textile tools.
Construction references: Lucide spool: structural rims and upright wound core; source controls the ball and needles.
Reduction: Omitted the loose thread tail and extra winding lines; needle heads use round caps to keep the top open.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '815209de-601e-4c97-a648-8b07b9972741'
SOURCE_PATH = 'pictographic-primitives/clothes/clothes design needle yarn_815209de-601e-4c97-a648-8b07b9972741.svg'
SOURCE_ICON_IDS = ('815209de-601e-4c97-a648-8b07b9972741',)
SOURCE_PATHS = ('pictographic-primitives/clothes/clothes design needle yarn_815209de-601e-4c97-a648-8b07b9972741.svg',)
AUTHOR = 'gpt-6'


class ThreadSpoolAndYarnBall(Solo48):
    icon_id = 'thread-spool-and-yarn-ball'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'clothes'
    aliases = ()
    keywords = ('thread', 'spool', 'and', 'yarn', 'ball')

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

        self.add_polyline("spool-top",(4,16),(8,16),(20,16))
        self.add_polyline("spool-bottom",(4,40),(8,40),(20,40))
        self.add_line("spool-left",(8,16),(8,40))
        self.add_polyline("spool-right",(20,16),(20,28),(20,40))
        for wall in ("spool-left","spool-right"):
            for rim in ("spool-top","spool-bottom"):self.relate("connect",wall,rim)
        path("yarn",(20,28),[("A",(32,16),12,12,True),("A",(44,28),12,12,True),("A",(32,40),12,12,True),("A",(20,28),12,12,True)],True)
        self.relate("connect","yarn","spool-right")
        path("winding",(32,16),[("C",(32,40),(42,22),(22,34))])
        self.relate("connect","winding","yarn")
        for i,tip in enumerate(((28,8),(40,8))):
            self.add_line(f"needle-{i}",tip,(32,16))
            self.relate("connect",f"needle-{i}","yarn")
        self.relate("connect","needle-0","needle-1")
