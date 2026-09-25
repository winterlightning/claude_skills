"""file with shield plus: fresh spacing repair.
Plan: Clipped file top, shield rim, rounded shield base and centered medical plus remain visible.
Keyshape VRECT_L: VRECT_L accommodates the upright integrated file and shield.
Omissions: Lower page and shield walls merged into one real outline.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='d1c4154e-8c68-4782-9c5a-e5c81055a594'
SOURCE_PATH='pictographic-primitives/other/file with shield plus_d1c4154e-8c68-4782-9c5a-e5c81055a594.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='file-with-shield-plus'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    categories = ('other', 'primitives-generate')
    aliases=()
    keywords=('file', 'with', 'shield', 'plus')

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
        # One shared outer wall: clipped file top and shield-shaped lower document.
        self.path('page-shield',(12,4),[('L',(28,4)),('L',(40,16)),('L',(40,28)),('A',(24,44),16),('A',(8,28),16),('L',(8,16)),('L',(8,8)),('A',(12,4),4)],True)
        self.add_polyline('shield-rim',(8,16),(24,12),(40,16));self.relate('connect','shield-rim','page-shield')
        self.cross('plus',24,27,4)
