"""transportation ticket boat transfer: fresh parallel-spacing repair.
Plan: Triangular sail, open hull and two curved transfer arrows remain readable with clear gaps.
Keyshape SQUARE: Square envelope leaves room below and beside the boat for the transfer arrows.
Omissions: Wave and closed hull top omitted; widened sail and open bowl-shaped hull preserve the boat silhouette.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='79b63fb3-53d2-42aa-af62-afdbc09d4964'
SOURCE_PATH='pictographic-primitives/_uncategorized_38/transportation ticket boat transfer_79b63fb3-53d2-42aa-af62-afdbc09d4964.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='transportation-ticket-boat-transfer'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('transportation', 'ticket', 'boat', 'transfer')

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
        self.add_polyline('mast',(22,6),(22,18),(22,30))
        self.add_polyline('sail',(22,6),(6,18),(22,18))
        self.relate('connect','mast','sail')
        self.add_bezier('hull-left',(6,26),((10,30),(16,30),(22,30)))
        self.add_bezier('hull-right',(22,30),((28,30),(30,28),(32,26)))
        self.add_contour('hull','hull-left','hull-right')
        self.relate('connect','mast','hull')
        self.add_bezier('transfer-top',(32,10),((38,10),(42,16),(42,22)))
        self.add_polyline('head-top',(36,18),(42,22),(42,14))
        self.relate('connect','transfer-top','head-top')
        self.add_bezier('transfer-bottom',(8,38),((14,42),(28,42),(40,38)))
        self.add_polyline('head-bottom',(36,34),(40,38),(36,42))
        self.relate('connect','transfer-bottom','head-bottom')
