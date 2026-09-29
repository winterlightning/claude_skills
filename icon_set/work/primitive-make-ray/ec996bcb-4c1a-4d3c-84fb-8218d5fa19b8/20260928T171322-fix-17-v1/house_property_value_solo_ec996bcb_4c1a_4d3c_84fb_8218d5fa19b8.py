"""Rejected dollar has squared bends and dominates the house. Restore a smooth compact S with a fine vertical stem inside the upright house silhouette.
Symbol plan: shared dimensions and symmetry for paired parts; coherent contours and explicit real junctions.
Construction reference: house; dollar-sign.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='ec996bcb-4c1a-4d3c-84fb-8218d5fa19b8'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__house-property-value-solo/20260928T171322Z-thuan-mac/reference/house dollar_ec996bcb-4c1a-4d3c-84fb-8218d5fa19b8.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='house-property-value-solo'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('house', 'dollar')
    def build(self):
        path=self.path;circle=self.circle;box=self.box;line=self.add_line;poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        path('house',(8,20),[('L',(24,4)),('L',(40,20)),('L',(40,40)),('A',(36,44),4,True),('L',(12,44)),('A',(8,40),4,True),('L',(8,20))],True)
        path('dollar',(30,21),[('C',(24,19),(28,19),(27,19)),('C',(18,23),(20,19),(18,20)),('C',(24,27),(18,26),(21,27)),('C',(30,31),(27,27),(30,28)),('C',(24,35),(30,34),(27,35)),('C',(18,33),(21,35),(20,35))])
        poly('stem',(24,16),(24,19),(24,27),(24,35),(24,38));join('stem','dollar')


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

