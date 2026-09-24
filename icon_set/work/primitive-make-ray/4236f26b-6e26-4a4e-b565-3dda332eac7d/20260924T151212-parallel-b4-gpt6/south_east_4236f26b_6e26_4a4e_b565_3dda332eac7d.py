"""south east: fresh parallel-spacing repair.
Plan: SE lettering has open eight-unit bar spacing; a diagonal needle divides the small compass dial.
Keyshape VRECT_L: Portrait envelope stacks a compact dial over full-height lettering.
Omissions: Dial ticks omitted; narrow triangular needle replaced by a diagonal diameter to leave two open dial regions.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='4236f26b-6e26-4a4e-b565-3dda332eac7d'
SOURCE_PATH='pictographic-primitives/_uncategorized_35/south east_4236f26b-6e26-4a4e-b565-3dda332eac7d.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='south-east'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('south', 'east')

    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)
    def path(self,n,start,segments,closed=False):
        at=start; members=[]
        for i,s in enumerate(segments):
            eid=f'{n}-{i}'; kind,end,*args=s
            if end==at: continue
            if kind=='L': self.add_line(eid,at,end)
            else: self.add_arc(eid,at,end,radius_x=args[0],sweep=args[1] if len(args)>1 else True)
            at=end; members.append(eid)
        self.add_contour(n,*members,closed=closed)
    def cross(self,n,x,y,r):
        for i,(dx,dy) in enumerate([(-r,0),(r,0),(0,-r),(0,r)]):
            self.add_line(f'{n}-{i}',(x,y),(x+dx,y+dy))
        for i in range(4):
            for j in range(i): self.relate('connect',f'{n}-{i}',f'{n}-{j}')

    def page(self):
        self.path('page',(12,4),[('L',(28,4)),('L',(40,16)),('L',(40,40)),('A',(36,44),4),('L',(12,44)),('A',(8,40),4),('L',(8,8)),('A',(12,4),4)],True)
    def phone(self,band=True):
        self.path('phone',(12,4),[('L',(36,4)),('A',(40,8),4),('L',(40,36)),('L',(40,40)),('A',(36,44),4),('L',(12,44)),('A',(8,40),4),('L',(8,36)),('L',(8,8)),('A',(12,4),4)],True)
        if band:
            self.add_line('separator',(8,36),(40,36));self.relate('connect','phone','separator')
    def house(self):
        self.path('house',(6,18),[('L',(24,6)),('L',(42,18)),('L',(42,38)),('A',(38,42),4),('L',(10,42)),('A',(6,38),4),('L',(6,18))],True)

    def frame(self):
        self.path('frame',(10,6),[('L',(38,6)),('A',(42,10),4),('L',(42,38)),('A',(38,42),4),('L',(10,42)),('A',(6,38),4),('L',(6,10)),('A',(10,6),4)],True)

    def build(self):
        # Rounded dial split at opposite diagonal needle nodes; paired cubic quadrants.
        self.add_bezier('dial',(29,7),((33,11),(33,13),(29,17)),((25,21),(23,21),(19,17)),((15,13),(15,11),(19,7)),((23,3),(25,3),(29,7)))
        self.add_line('needle',(19,17),(29,7));self.relate('connect','needle','dial')
        self.path('s',(20,28),[('L',(12,28)),('A',(12,36),4,False),('A',(12,44),4),('L',(8,44))])
        self.add_polyline('e',(40,28),(30,28),(30,36),(30,44),(40,44))
        self.add_line('e-bar',(30,36),(38,36));self.relate('connect','e','e-bar')
