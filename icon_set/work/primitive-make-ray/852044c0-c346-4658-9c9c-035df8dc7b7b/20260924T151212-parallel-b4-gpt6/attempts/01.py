"""stablization operation female: fresh spacing repair.
Plan: Separate scissors loops and preserve the partial female symbol to the upper right, with a real common cross junction.
Keyshape SQUARE: extrema derived from the profile's standard envelope.
Omissions: Blade seam omitted; scissors have a single open blade outline.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='852044c0-c346-4658-9c9c-035df8dc7b7b'
SOURCE_PATH='pictographic-primitives/_uncategorized_36/stablization operation female_852044c0-c346-4658-9c9c-035df8dc7b7b.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='stablization-operation-female'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('stablization', 'operation', 'female')

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
        self.circle('left-loop',10,38,4)
        self.circle('right-loop',26,38,4)
        self.add_polyline('blades',[(14,38),(14,26),(16,6),(22,30),(22,38)])
        self.relate('connect','blades','left-loop');self.relate('connect','blades','right-loop')
        self.add_arc('female-arc',(28,14),(36,28),radius_x=9)
        self.add_line('female-shaft',(28,14),(38,10))
        self.add_line('female-end',(38,10),(42,6))
        self.add_polyline('female-cross',[(34,6),(38,10),(42,14)])
        for a,b in [('female-arc','female-shaft'),('female-shaft','female-end'),('female-shaft','female-cross'),('female-end','female-cross')]:self.relate('connect',a,b)
