from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='fc535717-5e07-564a-aad9-923ace667ffb'
SOURCE_PATH='pictographic-primitives/holidays/star_fc535717-5e07-564a-aad9-923ace667ffb.svg'
AUTHOR='gpt-6'
PLAN='Five-point star centered in a round award medal, with paired ribbon ends beneath. Wider star and deeper lower notch increase internal space.'
CONSTRUCTION_REFERENCES='star: mirrored alternating outer points and inner valleys; supplied medal owns ribbon.'
OMISSIONS=[]
class Drawing(Solo48):
    icon_id='star-award-badge-ribbon'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('star',)

    def path(self,n,start,commands,closed=False):
        here=start;members=[]
        for i,(kind,end,*a) in enumerate(commands):
            k=f'{n}-{i}';members.append(k)
            if kind=='L':self.add_line(k,here,end)
            elif kind=='A':self.add_arc(k,here,end,radius_x=a[0],radius_y=a[1],sweep=a[2])
            elif kind=='C':self.add_bezier(k,here,(a[0],a[1],end))
            here=end
        self.add_contour(n,*members,closed=closed)
    def circle(self,n,x,y,r):
        self.path(n,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
    def box(self,n,l,t,r,b,k=4):
        self.path(n,(l+k,t),[('L',(r-k,t)),('A',(r,t+k),k,k,True),('L',(r,b-k)),('A',(r-k,b),k,k,True),('L',(l+k,b)),('A',(l,b-k),k,k,True),('L',(l,t+k)),('A',(l+k,t),k,k,True)],True)

    def build(self):
        self.path('medal',(24,4),[('A',(40,20),16,16,True),('A',(24,36),16,16,True),('A',(8,20),16,16,True),('A',(24,4),16,16,True)],True)
        self.add_polyline('star',(24,11),(27,17),(34,18),(29,23),(30,30),(24,27),(18,30),(19,23),(14,18),(21,17),closed=True)
        self.add_polyline('ribbon',(12,31),(12,44),(24,40),(36,44),(36,31))
        # The ribbon ends meet the circle at integer 3-4-5 nodes below.
