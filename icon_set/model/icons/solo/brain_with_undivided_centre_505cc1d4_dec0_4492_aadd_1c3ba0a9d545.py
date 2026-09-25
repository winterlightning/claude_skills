"""Brain with Undivided Centre.

Plan: HRECT centerlines (4,8)-(44,40); mirrored rounded hemispheres share top and bottom notch nodes. Sparse inward folds preserve clear internal channels.
Construction references: Lucide brain: paired lobe contours, shared central fissure and inward curved folds.
Reduction: Reduced the small perimeter wrinkles to broad lobes; preserved the named center treatment and two folds where specified.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '505cc1d4-dec0-4492-aadd-1c3ba0a9d545'
SOURCE_PATH = 'pictographic-primitives/artificial-intelligence/brain 1_505cc1d4-dec0-4492-aadd-1c3ba0a9d545.svg'
SOURCE_ICON_IDS = ('505cc1d4-dec0-4492-aadd-1c3ba0a9d545',)
SOURCE_PATHS = ('pictographic-primitives/artificial-intelligence/brain 1_505cc1d4-dec0-4492-aadd-1c3ba0a9d545.svg',)
AUTHOR = 'gpt-6'


class BrainWithUndividedCentre(Solo48):
    icon_id = 'brain-with-undivided-centre'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'artificial-intelligence'
    categories = ('artificial-intelligence', 'primitives')
    aliases = ()
    keywords = ('brain', 'with', 'undivided', 'centre')

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

        # One mirrored sequence of broad, smooth lobes per hemisphere.
        for side in (-1,1):
            p=lambda x,y:(24+side*x,y)
            k=f"hemisphere-{side}"
            path(k,p(0,12),[("C",p(8,8),p(2,8),p(4,8)),("C",p(14,17),p(14,8),p(16,12)),("A",p(14,31),6,7,side>0),("C",p(8,40),p(16,36),p(14,40)),("C",p(0,36),p(4,40),p(2,40))])
        self.relate("connect","hemisphere--1","hemisphere-1")
