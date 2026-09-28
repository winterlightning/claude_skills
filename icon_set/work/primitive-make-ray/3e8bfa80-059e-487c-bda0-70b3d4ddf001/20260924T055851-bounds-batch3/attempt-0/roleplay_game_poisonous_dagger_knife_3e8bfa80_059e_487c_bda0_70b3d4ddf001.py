"""roleplay game poisonous dagger knife.
Plan: Diagonal dagger with guard and rounded handle, droplet and open skull silhouette, matching source which has no eyes. No useful Lucide complete match. No poison symbol omitted.
Keyshape SQUARE: visible bounds (4, 4, 44, 44); centerlines inset 2 from these bounds.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='3e8bfa80-059e-487c-bda0-70b3d4ddf001'
SOURCE_PATH='pictographic-primitives/video-games/batch-09/roleplay game poisonous dagger knife_3e8bfa80-059e-487c-bda0-70b3d4ddf001.svg'
AUTHOR="gpt-6"

class Drawing(Solo48):
    icon_id='roleplay-game-poisonous-dagger-knife'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/general"
    aliases=()
    keywords=('roleplay', 'game', 'poisonous', 'dagger', 'knife')
    def build(self):
        # Diagonal tool, droplet above right, open skull below right.
        for j,(a,b) in enumerate(zip([(10,30),(28,6),(28,20)],[(28,6),(28,20),(18,38)]),1):self.add_line(f'blade-{j}',a,b)
        self.add_arc('handle',(18,38),(10,30),radius_x=6,sweep=True)
        self.add_contour('dagger','blade-1','blade-2','blade-3','handle',closed=True)
        self.add_polyline('guard',(6,24),(14,32),(22,40));self.relate('connect','guard','dagger')
        self.path('drop',(38,14),[('L',(42,22)),('A',(34,22),4,4,True),('L',(38,14))],True)
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
