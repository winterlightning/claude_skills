"""Rejected headband is a narrow ellipse above oversized cups. Restore the broad semicircular arch and proportional rounded earcups, with equal radii and a shared center axis.
Symbol plan: shared dimensions and symmetry for paired parts; coherent contours and explicit real junctions.
Construction reference: headphones.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='d5c2108b-d4dd-540a-bbca-681acd128bdf'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__headphones-with-rounded-earcups/20260928T171322Z-thuan-mac/reference/headphones_d5c2108b-d4dd-540a-bbca-681acd128bdf.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='headphones-with-rounded-earcups'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('headphones',)
    def build(self):
        path=self.path;circle=self.circle;box=self.box;line=self.add_line;poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        path('headband',(6,30),[('L',(6,24)),('A',(24,6),18,True),('A',(42,24),18,True),('L',(42,30))])
        for n,l,r in [('left',6,16),('right',32,42)]:box(n+'-cup',l,26,r,42,4);join(n+'-cup','headband')


    def path(self,n,start,commands,closed=False):
        ids=[]
        for i,c in enumerate(commands):
            ident=f'{n}-{i}';k,end,*a=c
            if k=='L':self.add_line(ident,start,end)
            elif k=='A':self.add_arc(ident,start,end,radius_x=a[0],sweep=a[1])
            elif k=='E':self.add_arc(ident,start,end,radius_x=a[0],radius_y=a[1],sweep=a[2])
            elif k=='C':self.add_bezier(ident,start,(a[0],a[1],end))
            ids.append(ident);start=end
        self.add_contour(n,*ids,closed=closed)
    def circle(self,n,x,y,r):
        self.path(n,(x,y-r),[('A',(x+r,y),r,True),('A',(x,y+r),r,True),('A',(x-r,y),r,True),('A',(x,y-r),r,True)],True)
    def box(self,n,l,t,r,b,q):
        self.path(n,(l+q,t),[('L',(r-q,t)),('A',(r,t+q),q,True),('L',(r,b-q)),('A',(r-q,b),q,True),('L',(l+q,b)),('A',(l,b-q),q,True),('L',(l,t+q)),('A',(l+q,t),q,True)],True)

