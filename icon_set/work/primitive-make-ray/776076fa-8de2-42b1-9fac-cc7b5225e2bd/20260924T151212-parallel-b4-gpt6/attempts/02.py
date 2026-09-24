"""ticket basketball game: fresh spacing repair.
Plan: Basketball behind a notched ticket; widened, smooth concave ends replace cramped semicircular cuts.
Keyshape SQUARE: extrema derived from the profile's standard envelope.
Omissions: Detached accent circle and ticket text rules omitted; basketball seams reduced to one broad curve.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='776076fa-8de2-42b1-9fac-cc7b5225e2bd'
SOURCE_PATH='pictographic-primitives/_uncategorized_37/ticket basketball game_776076fa-8de2-42b1-9fac-cc7b5225e2bd.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='ticket-basketball-game'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('ticket', 'basketball', 'game')

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
        self.path('ball',(14,24),[('A',(6,16),8),('A',(16,6),10),('A',(26,16),10),('A',(18,24),8)])
        self.add_polyline('ticket-top',(14,24),(18,24),(42,24))
        self.add_bezier('ticket-right',(42,24),((42,28),(38,28),(38,33)),((38,38),(42,38),(42,42)))
        self.add_line('ticket-bottom',(42,42),(14,42))
        self.add_bezier('ticket-left',(14,42),((14,38),(18,38),(18,33)),((18,28),(14,28),(14,24)))
        self.add_contour('ticket','ticket-top-1','ticket-top-2','ticket-right','ticket-bottom','ticket-left',closed=True)
        self.relate('connect','ball','ticket')
        self.add_bezier('seam',(6,16),((12,16),(20,12),(26,16)))
        self.relate('connect','ball','seam')
