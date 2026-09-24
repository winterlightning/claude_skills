"""heart user: fresh spacing repair.
Plan: Mirrored heart gains vertical room. Shared human user.svg vocabulary; head bottom21 and shoulder crest29 give exactly 4 ink units.
Keyshape VRECT_L: extrema derived from the profile's standard envelope.
Omissions: Small bust and broad lower heart; notch made shallower.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='e7e97355-bccb-465c-ae55-5037fd70d291'
SOURCE_PATH='pictographic-primitives/other/heart user_e7e97355-bccb-465c-ae55-5037fd70d291.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='heart-user'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('heart', 'user')

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
        self.add_bezier('heart',(24,8),((21,4),(19,4),(16,4)),((11,4),(8,8),(8,14)),((8,33),(12,38),(24,44)),((36,38),(40,33),(40,14)),((40,8),(37,4),(32,4)),((29,4),(27,4),(24,8)))
        self.circle('head',24,19,2)
        # user.svg: head bottom21, shoulder crest29, exact centerline gap8.
        self.add_arc('shoulders',(20,31),(28,31),radius_x=4,radius_y=2)
