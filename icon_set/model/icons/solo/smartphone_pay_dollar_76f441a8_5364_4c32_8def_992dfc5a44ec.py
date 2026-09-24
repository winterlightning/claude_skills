"""smartphone pay dollar: fresh parallel-spacing repair.
Plan: Overlapping phone and banknote retain the dollar mark, with a shared lower seam.
Keyshape SQUARE: Square envelope accommodates the overlapping upright phone and landscape bill.
Omissions: Decorative banknote corner arcs omitted; note enlarged and shares its bottom edge with the phone footer.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='76f441a8-5364-4c32-8def-992dfc5a44ec'
SOURCE_PATH='pictographic-primitives/_uncategorized_34/smartphone pay dollar_76f441a8-5364-4c32-8def-992dfc5a44ec.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='smartphone-pay-dollar'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('smartphone', 'pay', 'dollar')

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
        self.add_polyline('banknote',(16,6),(42,6),(42,34),(26,34),(16,34),closed=True)
        self.path('phone',(16,6),[('L',(10,6)),('A',(6,10),4,False),('L',(6,34)),('L',(6,38)),('A',(10,42),4,False),('L',(22,42)),('A',(26,38),4,False),('L',(26,34))])
        self.relate('connect','phone','banknote')
        self.add_line('footer',(6,34),(16,34));self.relate('connect','footer','phone');self.relate('connect','footer','banknote')
        self.path('dollar',(32,16),[('L',(29,16)),('A',(29,20),2,False),('A',(29,24),2),('L',(26,24))])
        self.add_line('tick-top',(29,15),(29,16));self.relate('connect','tick-top','dollar')
        self.add_line('tick-bottom',(29,24),(29,25));self.relate('connect','tick-bottom','dollar')
