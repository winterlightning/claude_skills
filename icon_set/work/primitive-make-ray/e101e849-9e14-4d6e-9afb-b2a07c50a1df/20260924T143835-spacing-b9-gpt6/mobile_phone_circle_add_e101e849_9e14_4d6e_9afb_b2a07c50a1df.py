"""mobile phone circle add: fresh spacing repair.
Plan: Upright phone, lower band and full circled plus remain readable. The dot-like compact-plus and square-phone alternatives were rejected.
Keyshape VRECT_L: VRECT_L preserves the phone proportions.
Omissions: Plus spokes extended to true cardinal circle junctions; all named symbols retained.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='e101e849-9e14-4d6e-9afb-b2a07c50a1df'
SOURCE_PATH='pictographic-primitives/other/mobile phone circle add_e101e849-9e14-4d6e-9afb-b2a07c50a1df.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='mobile-phone-circle-add'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('mobile', 'phone', 'circle', 'add')

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
        # Phone frame is split at its real corner and lower separator nodes.
        pts=[(12,4),(36,4),(40,8),(40,36),(40,40),(36,44),(12,44),(8,40),(8,36),(8,8)]
        arcs={1,4,6,9}
        for i,a in enumerate(pts):
            b=pts[(i+1)%len(pts)]
            if i in arcs:self.add_arc(f'phone-{i}',a,b,radius_x=4)
            else:self.add_line(f'phone-{i}',a,b)
        for i in range(len(pts)):self.relate('connect',f'phone-{i}',f'phone-{(i+1)%len(pts)}')
        self.add_line('separator',(8,36),(40,36))
        for i in (2,3,7,8):self.relate('connect','separator',f'phone-{i}')
        self.path('add-circle',(24,12),[('A',(32,20),8),('A',(24,28),8),('A',(16,20),8),('A',(24,12),8)],True)
        self.cross('plus',24,20,8)
        for i in range(4):self.relate('connect','add-circle',f'plus-{i}')
