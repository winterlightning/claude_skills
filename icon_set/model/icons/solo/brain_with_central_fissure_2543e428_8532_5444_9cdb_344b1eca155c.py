"""Brain with Central Fissure.

Plan: HRECT centerlines (4,8)-(44,40); mirrored rounded hemispheres share top and bottom notch nodes. Sparse inward folds preserve clear internal channels.
Construction references: Lucide brain: paired lobe contours, shared central fissure and inward curved folds.
Reduction: Reduced the small perimeter wrinkles to broad lobes; preserved the named center treatment and two folds where specified.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '2543e428-8532-5444-9cdb-344b1eca155c'
SOURCE_PATH = 'pictographic-primitives/artificial-intelligence/brain_2543e428-8532-5444-9cdb-344b1eca155c.svg'
SOURCE_ICON_IDS = ('2543e428-8532-5444-9cdb-344b1eca155c', '4cc51cde-8646-5c24-82c4-d7386922eb24')
SOURCE_PATHS = ('pictographic-primitives/artificial-intelligence/brain_2543e428-8532-5444-9cdb-344b1eca155c.svg', 'pictographic-primitives/artificial-intelligence/brain_4cc51cde-8646-5c24-82c4-d7386922eb24.svg')
AUTHOR = 'gpt-6'


class BrainWithCentralFissure(Solo48):
    icon_id = 'brain-with-central-fissure'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'artificial-intelligence'
    categories = ('artificial-intelligence', 'primitives')
    aliases = ()
    keywords = ('brain', 'with', 'central', 'fissure')

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

        self.add_line("fissure",(24,12),(24,36))
        for side in (-1,1): self.relate("connect","fissure",f"hemisphere-{side}")

        for side in (-1,1):
            p=lambda x,y:(24+side*x,y)
            path(f"fold-{side}",p(14,17),[("C",p(9,23),p(10,17),p(9,20))])
            self.relate("connect",f"fold-{side}",f"hemisphere-{side}")
