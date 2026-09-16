"""Sewing Needle with Looping Thread.

Plan: SQUARE centerlines (6,6)-(42,42); circular needle eye meets a long upright shaft, and flowing thread passes through the eye and loops around the shaft at an exact crossing node.
Construction references: Supplied threaded-needle reference; no useful exact Lucide needle match.
Reduction: Simplified the tapered needle body to one straight shaft with a distinct round eye; retained both loose thread ends.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '652a9d34-33e6-51e1-8190-d3c508fdfc2c'
SOURCE_PATH = 'pictographic-primitives/clothes/clothes design needle_652a9d34-33e6-51e1-8190-d3c508fdfc2c.svg'
SOURCE_ICON_IDS = ('652a9d34-33e6-51e1-8190-d3c508fdfc2c',)
SOURCE_PATHS = ('pictographic-primitives/clothes/clothes design needle_652a9d34-33e6-51e1-8190-d3c508fdfc2c.svg',)
AUTHOR = 'gpt-6'


class SewingNeedleWithLoopingThread(Solo48):
    icon_id = 'sewing-needle-with-looping-thread'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'clothes'
    aliases = ()
    keywords = ('sewing', 'needle', 'with', 'looping', 'thread')

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

        path("eye",(16,10),[("A",(20,6),4,4,True),("A",(24,10),4,4,True),("A",(20,14),4,4,True),("A",(16,10),4,4,True)],True)
        self.add_polyline("needle",(20,14),(20,30),(20,42))
        self.relate("connect","needle","eye")
        path("upper-thread",(24,10),[("C",(42,6),(30,14),(38,10))])
        self.relate("connect","upper-thread","eye")
        path("thread-loop",(16,10),[("C",(6,24),(8,12),(6,18)),("C",(20,30),(6,30),(12,30)),("C",(38,34),(30,30),(38,28)),("C",(34,42),(38,38),(36,40))])
        self.relate("connect","thread-loop","eye")
        self.relate("connect","thread-loop","needle")
