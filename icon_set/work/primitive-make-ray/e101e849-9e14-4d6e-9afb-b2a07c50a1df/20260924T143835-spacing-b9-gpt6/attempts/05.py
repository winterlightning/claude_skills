"""mobile phone circle add: fresh spacing repair.
Plan: Change to wider keyshape; explicit wall primitives certify circle/frame spacing. Keep plus at a visible two-unit spoke length.
Keyshape SQUARE: extrema derived from the profile's standard envelope.
Omissions: Phone widened and lower separator omitted; circle and readable plus retained.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='e101e849-9e14-4d6e-9afb-b2a07c50a1df'
SOURCE_PATH='pictographic-primitives/other/mobile phone circle add_e101e849-9e14-4d6e-9afb-b2a07c50a1df.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='mobile-phone-circle-add'
    keyshape=Keyshape.SQUARE
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
        pts=[(10,6),(38,6),(42,10),(42,38),(38,42),(10,42),(6,38),(6,10)]
        for i,a in enumerate(pts):
            b=pts[(i+1)%8]
            if i%2:self.add_arc(f'phone-{i}',a,b,radius_x=4)
            else:self.add_line(f'phone-{i}',a,b)
        for i in range(8):self.relate('connect',f'phone-{i}',f'phone-{(i+1)%8}')
        self.circle('add-circle',24,24,10)
        self.cross('plus',24,24,2)
