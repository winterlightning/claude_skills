"""mobile phone fingerprint: fresh spacing repair.
Plan: Returning ridge reads as a simplified fingerprint in an upright phone; smooth arch and inner stem retain ridge flow.
Keyshape VRECT_L: VRECT_L preserves the phone proportions.
Omissions: Fingerprint reduced to one continuous returning ridge; lower separator omitted.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='0ef09a66-6578-497b-817b-f821ad82e177'
SOURCE_PATH='pictographic-primitives/other/mobile phone fingerprint_0ef09a66-6578-497b-817b-f821ad82e177.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='mobile-phone-fingerprint'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('mobile', 'phone', 'fingerprint')

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
        # Rounded phone frame exposes its straight walls individually for exact clearance.
        pts=[(12,4),(36,4),(40,8),(40,40),(36,44),(12,44),(8,40),(8,8)]
        for i,a in enumerate(pts):
            b=pts[(i+1)%8]
            if i%2:self.add_arc(f'phone-{i}',a,b,radius_x=4)
            else:self.add_line(f'phone-{i}',a,b)
        for i in range(8):self.relate('connect',f'phone-{i}',f'phone-{(i+1)%8}')
        self.path('fingerprint',(16,30),[('L',(16,21)),('A',(32,21),8),('L',(32,28)),('A',(24,28),4),('L',(24,22))])
