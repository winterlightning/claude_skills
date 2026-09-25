"""Tracked Bulldozer Facing Left.

Plan: HRECT centerlines (4,8)-(44,40); stadium-shaped crawler track supports a raised cab and low hood; a real forward arm meets a smooth left-facing blade.
Construction references: Lucide tractor: coherent cab, hood and wheel hierarchy; source controls the continuous track and curved blade.
Reduction: Omitted track inset and small hood marking, preserving the directional blade and crawler silhouette.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = 'dd08ace3-026c-4c9e-9ee1-8880118f7d1d'
SOURCE_PATH = 'pictographic-primitives/construction/cleaner_dd08ace3-026c-4c9e-9ee1-8880118f7d1d.svg'
SOURCE_ICON_IDS = ('dd08ace3-026c-4c9e-9ee1-8880118f7d1d',)
SOURCE_PATHS = ('pictographic-primitives/construction/cleaner_dd08ace3-026c-4c9e-9ee1-8880118f7d1d.svg',)
AUTHOR = 'gpt-6'


class TrackedBulldozerFacingLeft(Solo48):
    icon_id = 'tracked-bulldozer-facing-left'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'construction'
    categories = ('construction', 'primitives')
    aliases = ()
    keywords = ('tracked', 'bulldozer', 'facing', 'left')

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

        path("track",(24,28),[("L",(38,28)),("A",(38,40),6,6,True),("L",(24,40)),("A",(24,28),6,6,True)],True)
        self.add_polyline("body",(24,28),(24,18),(28,18),(40,18),(38,28))
        self.relate("connect","body","track")
        path("cab",(28,18),[("L",(30,10)),("C",(32,8),(30,9),(31,8)),("L",(38,8)),("L",(40,18))])
        self.relate("connect","cab","body")
        path("blade",(4,16),[("C",(8,28),(7,20),(8,24)),("C",(4,40),(8,32),(7,36))])
        self.add_line("arm",(8,28),(24,28))
        self.relate("connect","blade","arm")
        self.relate("connect","arm","body")
