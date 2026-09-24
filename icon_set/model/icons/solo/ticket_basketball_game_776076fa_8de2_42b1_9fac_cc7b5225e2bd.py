"""ticket basketball game: fresh parallel-spacing repair.
Plan: Widened basketball retains a curved seam and upper crossing meridian above a smoothly notched ticket.
Keyshape SQUARE: Square envelope makes room for the ball above the ticket.
Omissions: Detached accent circle and ticket text rules omitted; lower meridian hidden behind the ticket.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
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
        self.add_arc('ball-bl',(16,26),(6,16),radius_x=10)
        self.add_arc('ball-tl',(6,16),(18,6),radius_x=12,radius_y=10)
        self.add_arc('ball-tr',(18,6),(30,16),radius_x=12,radius_y=10)
        self.add_arc('ball-br',(30,16),(20,26),radius_x=10)
        self.add_contour('ball','ball-bl','ball-tl','ball-tr','ball-br')
        self.add_line('ticket-top-1',(14,26),(16,26))
        self.add_line('ticket-top-2',(16,26),(20,26))
        self.add_line('ticket-top-3',(20,26),(42,26))
        self.add_bezier('ticket-right',(42,26),((42,30),(38,30),(38,34)),((38,38),(42,38),(42,42)))
        self.add_line('ticket-bottom',(42,42),(14,42))
        self.add_bezier('ticket-left',(14,42),((14,38),(18,38),(18,34)),((18,30),(14,30),(14,26)))
        self.add_contour('ticket','ticket-top-1','ticket-top-2','ticket-top-3','ticket-right','ticket-bottom','ticket-left',closed=True)
        self.relate('connect','ball','ticket')
        self.add_bezier('seam-left',(6,16),((10,18),(14,18),(18,16)))
        self.add_bezier('seam-right',(18,16),((22,14),(26,14),(30,16)))
        self.add_contour('seam','seam-left','seam-right')
        self.add_line('seam-top',(18,6),(18,16))
        self.relate('connect','ball','seam');self.relate('connect','ball','seam-top');self.relate('connect','seam','seam-top')
