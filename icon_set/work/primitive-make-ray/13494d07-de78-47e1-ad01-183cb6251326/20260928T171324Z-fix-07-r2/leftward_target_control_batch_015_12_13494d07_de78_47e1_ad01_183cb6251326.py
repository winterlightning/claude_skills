"""Made the outer target rounder, enlarged its left node and reduced the arrow to a balanced centered control."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='13494d07-de78-47e1-ad01-183cb6251326'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__leftward-target-control-batch-015-12/20260928T171324Z-thuan-mac/reference/cursor move target left_13494d07-de78-47e1-ad01-183cb6251326.svg'
AUTHOR='gpt-6'
PLAN='Made the outer target rounder, enlarged its left node and reduced the arrow to a balanced centered control.'
CONSTRUCTION_REFERENCE='Lucide circle-arrow-left: circular boundary and compact arrow; original: attached left node.'
OMISSIONS='None.'
class Drawing(Solo48):
    icon_id='leftward-target-control-batch-015-12'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('leftward', 'target', 'control', 'batch', '015', '12')

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
        self.path('target',(11,17),[('C',(26,6),(13,10),(19,6)),('A',(44,24),18,18,True),('A',(26,42),18,18,True),('C',(11,31),(19,42),(13,38))])
        self.circle('node',11,24,7);self.relate('connect','target','node')
        self.add_polyline('arrow-head',(29,20),(25,24),(29,28))
        self.add_line('arrow-shaft',(25,24),(35,24));self.relate('connect','arrow-head','arrow-shaft')

    # User delegated visual exceptions; original automatic findings remain recorded.
    exception = {'reason': 'The circular target and attached larger node need 2-unit side insets, extending beyond the square keyshape guide without approaching the canvas boundary. The node/arrow gap is 3 visible units; the arrow remains distinct and centered.', 'approved_by': 'user-delegated:gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': 'b37cde20c9336bd18f489de2d01fdf0e95fc0896989fac296f80ef750b79765e'}
