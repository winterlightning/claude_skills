"""team vs team mode.
Plan: Two equal detached busts over a gamepad. human-reference.md/user.svg/full_body_ref.png: circular heads radius3, lower head centerline12, shoulders20 gives exact 8 centerline/4 ink head-body gap. Shared mirrored shoulder arcs. Simplify controller grips to open lower silhouette; omit small internal V control to remove undersized triangular hole.
Keyshape SQUARE: visible bounds (4, 4, 44, 44); centerlines inset 2 from these bounds.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='5bac2074-ad7e-4c93-acd8-d73142b163b6'
SOURCE_PATH='pictographic-primitives/video-games/batch-11/team vs team mode_5bac2074-ad7e-4c93-acd8-d73142b163b6.svg'
AUTHOR="gpt-6"

class Drawing(Solo48):
    icon_id='team-vs-team-mode'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "video-games"
    categories = ("primitives", "video-games")
    aliases=()
    keywords=('team', 'vs', 'team', 'mode')
    def build(self):
        for i,x in enumerate((11,37)):
            self.circle(f'head-{i}',x,9,3)
            self.path(f'body-{i}',(x-5,25),[('A',(x,20),5,5,True),('A',(x+5,25),5,5,True)])
        self.add_polyline('controller',(20,42),(12,42),(16,34),(32,34),(36,42),(28,42))

    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)
    def path(self,n,start,ops,closed=False):
        at=start; members=[]
        for i,op in enumerate(ops):
            eid=f'{n}-{i}';kind,end,*args=op
            if end==at:continue
            if kind=='L':self.add_line(eid,at,end)
            elif kind=='A':self.add_arc(eid,at,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
            at=end;members.append(eid)
        self.add_contour(n,*members,closed=closed)
