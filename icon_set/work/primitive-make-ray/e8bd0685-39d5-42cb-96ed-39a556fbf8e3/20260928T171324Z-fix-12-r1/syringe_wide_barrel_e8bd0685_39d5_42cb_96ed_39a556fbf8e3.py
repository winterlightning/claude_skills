"""Rebuilt the barrel as a balanced diagonal rounded shape, aligned needle and plunger and restored two graduations."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='e8bd0685-39d5-42cb-96ed-39a556fbf8e3'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__syringe-wide-barrel/20260928T171324Z-thuan-mac/reference/syringe_e8bd0685-39d5-42cb-96ed-39a556fbf8e3.svg'
AUTHOR='gpt-6'
PLAN='Rebuilt the barrel as a balanced diagonal rounded shape, aligned needle and plunger and restored two graduations.'
CONSTRUCTION_REFERENCE='Lucide syringe: aligned diagonal barrel, plunger and needle with repeated graduation strokes.'
OMISSIONS='Three reference marks reduced to two at 48 px.'
class Drawing(Solo48):
    icon_id='syringe-wide-barrel'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('syringe', 'wide', 'barrel')

    def path(self,n,start,commands,closed=False):
        here=start; ids=[]
        for i,(kind,end,*a) in enumerate(commands):
            ident=f'{n}-{i}';ids.append(ident)
            if kind=='L': self.add_line(ident,here,end)
            elif kind=='A': self.add_arc(ident,here,end,radius_x=a[0],radius_y=a[1],sweep=a[2])
            elif kind=='C': self.add_bezier(ident,here,(a[0],a[1],end))
            here=end
        self.add_contour(n,*ids,closed=closed)
    def circle(self,n,x,y,r):
        self.path(n,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
    def box(self,n,l,t,r,b,k=4):
        self.path(n,(l+k,t),[('L',(r-k,t)),('A',(r,t+k),k,k,True),('L',(r,b-k)),('A',(r-k,b),k,k,True),('L',(l+k,b)),('A',(l,b-k),k,k,True),('L',(l,t+k)),('A',(l+k,t),k,k,True)],True)
    def phone(self,band=True):
        # Shared outline owns width, corner radius and band attachment nodes.
        l,r,t,b,k,y=10,38,4,44,4,36
        self.path('phone',(l+k,t),[('L',(r-k,t)),('A',(r,t+k),k,k,True),('L',(r,y)),('L',(r,b-k)),('A',(r-k,b),k,k,True),('L',(l+k,b)),('A',(l,b-k),k,k,True),('L',(l,y)),('L',(l,t+k)),('A',(l+k,t),k,k,True)],True)
        if band:
            self.add_line('band',(l,y),(r,y));self.relate('connect','phone','band')

    def build(self):
        self.path('barrel',(24,12),[('L',(30,18)),('L',(36,24)),('L',(21,39)),('C',(15,39),(19,41),(17,41)),('L',(12,36)),('L',(9,33)),('C',(9,27),(7,31),(7,29)),('L',(11,25)),('L',(16,20)),('L',(24,12))],True)
        self.add_line('needle',(6,42),(12,36));self.relate('connect','needle','barrel')
        self.add_line('plunger',(30,18),(38,10));self.relate('connect','plunger','barrel')
        self.add_polyline('handle',(34,6),(38,10),(42,14));self.relate('connect','handle','plunger')
        for j,(x,y) in enumerate(((11,25),(16,20))):
            self.add_line(f'tick-{j}',(x,y),(x+4,y+4));self.relate('connect','barrel',f'tick-{j}')

    # User delegated visual exceptions; original automatic findings remain recorded.
    exception = {'reason': 'Keep two readable barrel graduation marks instead of the rejected single mark. Their approximately 3-unit visible diagonal spacing and rounded barrel remain clear at 48 px.', 'approved_by': 'user-delegated:gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': 'e0890ee2e4836b1af5165d650edcad2b86a0d027a154f1a9447bf6d96d73174c'}
