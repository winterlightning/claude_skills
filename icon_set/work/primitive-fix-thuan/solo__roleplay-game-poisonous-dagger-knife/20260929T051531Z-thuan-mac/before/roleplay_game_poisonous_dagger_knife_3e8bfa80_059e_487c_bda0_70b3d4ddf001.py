"""roleplay game poisonous dagger knife.
Plan: Diagonal dagger with guard and rounded handle, droplet and open skull silhouette, matching source which has no eyes. No useful Lucide complete match. No poison symbol omitted.
Keyshape SQUARE: visible bounds (4, 4, 44, 44); centerlines inset 2 from these bounds.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='3e8bfa80-059e-487c-bda0-70b3d4ddf001'
SOURCE_PATH='pictographic-primitives/video-games/batch-09/roleplay game poisonous dagger knife_3e8bfa80-059e-487c-bda0-70b3d4ddf001.svg'
AUTHOR="gpt-6"

class Drawing(Solo48):
    icon_id='roleplay-game-poisonous-dagger-knife'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "video-games"
    categories = ("primitives", "video-games")
    aliases=()
    keywords=('roleplay', 'game', 'poisonous', 'dagger', 'knife')
    def build(self):
        # Diagonal tool, droplet above right, open skull below right.
        self.path('dagger',(6,36),[('L',(24,6)),('L',(24,22)),('L',(14,42)),('L',(12,42)),('A',(6,36),6,6,True)],True)
        self.add_line('guard',(6,24),(22,36));self.relate('connect','guard','dagger')
        self.path('drop',(38,10),[('L',(42,18)),('A',(34,18),4,4,True),('L',(38,10))],True)
        self.path('skull',(30,42),[('L',(30,38)),('A',(42,38),6,6,True),('L',(42,42))])

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
