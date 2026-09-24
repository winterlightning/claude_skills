"""south east: fresh spacing repair.
Plan: SE letters use eight-unit steps; compass needle lies on exact 3-4-5 boundary nodes. Circular dial above preserves reference arrangement.
Keyshape VRECT_L: extrema derived from the profile's standard envelope.
Omissions: Pointer simplified to a diagonal needle; three dial ticks omitted.
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

    def build(self):
        # 3-4-5 points split the dial exactly at the needle's two endpoints.
        self.add_arc('dial-a',(27,8),(21,16),radius_x=5)
        self.add_arc('dial-b',(21,16),(24,7),radius_x=5)
        self.add_arc('dial-c',(24,7),(27,8),radius_x=5)
        self.add_contour('dial','dial-a','dial-b','dial-c',closed=True)
        self.add_line('needle',(21,16),(27,8));self.relate('connect','needle','dial')
        self.add_line('north-tick',(24,4),(24,7));self.relate('connect','north-tick','dial')
        # Circle split at north cardinal for its real tick connection.
        self.path('s',(20,28),[('L',(12,28)),('A',(12,36),4,False),('A',(12,44),4),('L',(8,44))])
        self.add_polyline('e',(40,28),(30,28),(30,36),(30,44),(40,44))
        self.add_line('e-bar',(30,36),(38,36));self.relate('connect','e','e-bar')
