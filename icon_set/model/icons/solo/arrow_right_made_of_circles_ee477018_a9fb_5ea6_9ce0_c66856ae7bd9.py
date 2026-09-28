"""Arrow Right Made of Circles.

Plan: Six equal circular marks with a 12-unit shaft pitch and mirrored wings. VRECT centerlines (8,4)-(40,44), or HRECT (4,8)-(44,40). Radius 2 circles read as round dots at stroke 4.
Construction references: Supplied circle-arrow reference; no useful exact Lucide match.
Reduction: Increased stroke contrast and regularized circle sizes; preserved all six marks.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = 'ee477018-a9fb-5ea6-9ce0-c66856ae7bd9'
SOURCE_PATH = 'pictographic-primitives/arrows/arrow thick dot right_ee477018-a9fb-5ea6-9ce0-c66856ae7bd9.svg'
SOURCE_ICON_IDS = ('ee477018-a9fb-5ea6-9ce0-c66856ae7bd9',)
SOURCE_PATHS = ('pictographic-primitives/arrows/arrow thick dot right_ee477018-a9fb-5ea6-9ce0-c66856ae7bd9.svg',)
AUTHOR = 'gpt-6'


class ArrowRightMadeOfCircles(Solo48):
    icon_id = 'arrow-right-made-of-circles'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'arrows'
    categories = ('arrows', 'primitives')
    aliases = ()
    keywords = ('arrow', 'right', 'made', 'of', 'circles')

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

        radius=2
        centers=[(24,6),(24,18),(24,30),(24,42),(10,18),(38,18)]
        centers=[(48-y,x) for x,y in centers]
        for i,(x,y) in enumerate(centers): circle(f"mark-{i}",x,y,radius)
