"""technology hand chip: fresh parallel-spacing repair.
Plan: Open hand with two broad finger groups and thumb sits beside a processor with four pins.
Keyshape HRECT_L: Horizontal envelope separates the upright hand from the small processor.
Omissions: Four fingers reduced to two broad finger groups; palm crease omitted; one chip pin per side.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='40415ff8-ab5e-4613-9886-33d055540f90'
SOURCE_PATH='pictographic-primitives/_uncategorized_37/technology hand chip_40415ff8-ab5e-4613-9886-33d055540f90.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='technology-hand-chip'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases=()
    keywords=('technology', 'hand', 'chip')

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
        self.path('hand-left',(4,40),[('L',(4,12)),('A',(8,8),4),('A',(12,12),4),('L',(12,22))])
        self.path('hand-right',(12,12),[('A',(16,8),4),('A',(20,12),4),('L',(20,24)),('A',(24,28),4),('L',(24,30)),('A',(20,36),8),('L',(20,40))])
        self.relate('connect','hand-left','hand-right')
        self.add_polyline('chip',(34,30),(38,30),(42,30),(42,34),(42,38),(38,38),(34,38),(34,34),closed=True)
        for n,a,b in [('top',(38,28),(38,30)),('right',(42,34),(44,34)),('bottom',(38,38),(38,40)),('left',(32,34),(34,34))]:
            self.add_line('pin-'+n,a,b);self.relate('connect','chip','pin-'+n)
