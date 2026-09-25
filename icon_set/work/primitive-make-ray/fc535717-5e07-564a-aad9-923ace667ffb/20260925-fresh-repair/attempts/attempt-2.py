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
        # Slightly upright round medal, with ribbon contacts owned by explicit nodes.
        self.path('medal',(24,4),[('C',(40,19),(33,4),(40,10)),('C',(36,29),(40,23),(39,26)),('C',(24,34),(33,32),(28,34)),('C',(12,29),(20,34),(15,32)),('C',(8,19),(9,26),(8,23)),('C',(24,4),(8,10),(15,4))],True)
        # Rounded outer tips and inner valleys remove the pinched straight star arms.
        self.path('star',(24,13),[('C',(27,17),(25,13),(26,16)),('C',(31,19),(28,18),(31,17)),('C',(28,22),(31,20),(28,21)),('C',(28,25),(28,23),(30,25)),('C',(24,23),(27,25),(25,23)),('C',(20,25),(23,23),(21,25)),('C',(20,22),(18,25),(20,23)),('C',(17,19),(20,21),(17,20)),('C',(21,17),(17,17),(20,18)),('C',(24,13),(22,16),(23,13))],True)
        self.add_polyline('ribbon',(12,29),(10,44),(24,42),(38,44),(36,29));self.relate('connect','ribbon','medal')
