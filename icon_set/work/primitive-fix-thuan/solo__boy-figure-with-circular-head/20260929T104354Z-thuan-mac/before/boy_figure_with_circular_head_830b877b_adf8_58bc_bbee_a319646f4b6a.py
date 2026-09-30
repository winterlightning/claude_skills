"""Boy Figure with Circular Head.

Plan: VRECT centerlines (8,4)-(40,44); radius8 circular detached head above an elliptical shoulder dome, short sleeves and a tapered flat-bottom body. Head bottom20 to body top28 is exactly8 centerline /4 visible units.
Construction references: Shared human_ref/user.svg and full_body_ref.png for circular head and rounded anatomy; supplied source for compact garment silhouette.
Reduction: Retained the source as a compact outlined figure without introducing separate stick limbs.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '830b877b-adf8-58bc-bbee-a319646f4b6a'
SOURCE_PATH = 'pictographic-primitives/avatars/boy full body_830b877b-adf8-58bc-bbee-a319646f4b6a.svg'
SOURCE_ICON_IDS = ('830b877b-adf8-58bc-bbee-a319646f4b6a',)
SOURCE_PATHS = ('pictographic-primitives/avatars/boy full body_830b877b-adf8-58bc-bbee-a319646f4b6a.svg',)
AUTHOR = 'gpt-6'


class BoyFigureWithCircularHead(Solo48):
    icon_id = 'boy-figure-with-circular-head'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'avatars'
    categories = ('avatars', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('boy', 'figure', 'with', 'circular', 'head')
    HUMAN_REFERENCE = "icon_set/references/human_ref/full_body_ref.png"
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

        circle("head",24,12,8)
        path("body",(24,28),[("A",(40,36),16,8,True),("L",(34,36)),("L",(32,44)),("L",(16,44)),("L",(14,36)),("L",(8,36)),("A",(24,28),16,8,True)],True)
