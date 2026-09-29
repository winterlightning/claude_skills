"""Restored the complete diamond mortarboard over a curved crown within an upright rounded card."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='078c527e-7fad-4791-9242-4409c4f071d0'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__academic-graduation-cap-solo/20260928T171406Z-thuan-mac/reference/Academic Graduation Cap_078c527e-7fad-4791-9242-4409c4f071d0.svg'
AUTHOR='gpt-6'
PLAN='Restored the complete diamond mortarboard over a curved crown within an upright rounded card.'
CONSTRUCTION_REFERENCE='Lucide graduation-cap: diamond board distinct from its curved crown; source: enclosing portrait card.'
OMISSIONS='None.'
class Drawing(Solo48):
    icon_id='academic-graduation-cap-solo'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('academic', 'graduation', 'cap', 'solo')

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
        self.box('card',8,4,40,44,4)
        self.add_polyline('board',(24,14),(34,20),(31,22),(24,26),(17,22),(14,20),closed=True)
        self.path('crown',(17,22),[('L',(17,31)),('C',(24,34),(20,33),(22,34)),('C',(31,31),(26,34),(28,33)),('L',(31,22))])
        self.relate('connect','board','crown')

    # User delegated visual exceptions; original automatic findings remain recorded.
    exception = {'reason': 'Preserve a complete diamond mortarboard and separate curved crown inside the portrait card. Board/card side gaps are 2 visible units and the crown openings remain visible; merging the board seam caused the rejected roof-like symbol.', 'approved_by': 'user-delegated:gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '74f649fb495065d34ff196ce05b9a8f3eb2516394d4523badbd36000e578043d'}
