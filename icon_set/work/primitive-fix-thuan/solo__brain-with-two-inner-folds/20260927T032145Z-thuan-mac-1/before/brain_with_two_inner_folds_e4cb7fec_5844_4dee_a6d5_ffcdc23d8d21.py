"""Brain with Two Inner Folds.

Plan: SQUARE centerlines (6,6)-(42,42); mirrored rounded hemispheres share top and bottom notch nodes. Sparse inward folds preserve clear internal channels.
Construction references: Lucide brain: paired lobe contours, shared central fissure and inward curved folds.
Reduction: Reduced the small perimeter wrinkles to broad lobes; preserved the named center treatment and two folds where specified.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = 'e4cb7fec-5844-4dee-a6d5-ffcdc23d8d21'
SOURCE_PATH = 'pictographic-primitives/artificial-intelligence/brain_e4cb7fec-5844-4dee-a6d5-ffcdc23d8d21.svg'
SOURCE_ICON_IDS = ('e4cb7fec-5844-4dee-a6d5-ffcdc23d8d21',)
SOURCE_PATHS = ('pictographic-primitives/artificial-intelligence/brain_e4cb7fec-5844-4dee-a6d5-ffcdc23d8d21.svg',)
AUTHOR = 'gpt-6'


class BrainWithTwoInnerFolds(Solo48):
    icon_id = 'brain-with-two-inner-folds'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'artificial-intelligence'
    categories = ('artificial-intelligence', 'primitives')
    aliases = ()
    keywords = ('brain', 'with', 'two', 'inner', 'folds')

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

        for side in (-1,1):
            p=lambda x,y:(24+side*x,y)
            path(f"hemisphere-{side}",p(0,10),[("C",p(8,6),p(2,6),p(4,6)),("C",p(16,14),p(14,6),p(16,10)),("C",p(18,24),p(18,16),p(18,20)),("C",p(16,34),p(18,28),p(18,32)),("C",p(8,42),p(16,38),p(14,42)),("C",p(0,38),p(4,42),p(2,42))])
        self.relate("connect","hemisphere--1","hemisphere-1")
        self.add_line("fissure",(24,10),(24,38))
        for side in (-1,1):self.relate("connect","fissure",f"hemisphere-{side}")

        path("left-fold",(8,14),[("C",(15,21),(8,19),(11,21))])
        self.relate("connect","left-fold","hemisphere--1")
        path("right-fold",(33,21),[("C",(33,27),(34,21),(34,25))])
