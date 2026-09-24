"""mail card bug: fresh spacing repair.
Plan: Bug body, two antenna strokes and side legs remain above the envelope fold.
Keyshape SQUARE: SQUARE gives the card enough width for its bug.
Omissions: Card/envelope side walls merged; bug divider, lower legs and envelope seam strokes omitted.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='0b79dbcd-029c-4c05-baad-34d720b23be7'
SOURCE_PATH='pictographic-primitives/other/mail card bug_0b79dbcd-029c-4c05-baad-34d720b23be7.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='mail-card-bug'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('mail', 'card', 'bug')

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
        # Card and envelope share the side walls; fold joins at explicit vertices.
        self.path('card-mail',(10,6),[('L',(38,6)),('A',(42,10),4),('L',(42,26)),('L',(42,38)),('A',(38,42),4),('L',(10,42)),('A',(6,38),4),('L',(6,26)),('L',(6,10)),('A',(10,6),4)],True)
        self.add_polyline('fold',(6,26),(18,34),(30,34),(42,26));self.relate('connect','fold','card-mail')
        # Four-legged beetle: the body exposes each actual attachment node.
        pts=[(24,17),(28,21),(24,25),(20,21)]
        for i in range(4): self.add_arc(f'bug-{i}',pts[i],pts[(i+1)%4],radius_x=4)
        self.add_contour('bug',*(f'bug-{i}' for i in range(4)),closed=True)
        for i,(a,b) in enumerate([((24,17),(21,15)),((24,17),(27,15)),((20,21),(15,21)),((28,21),(33,21))]):
            self.add_line(f'leg-{i}',a,b);self.relate('connect',f'leg-{i}','bug')

