'Open palm with rounded fingertips, horizontal thumb crease and open right wrist.'
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID='21f148ad-8725-429c-aa23-cad9257d7f13'
SOURCE_PATH='pictographic-primitives/other/give hand 1_21f148ad-8725-429c-aa23-cad9257d7f13.svg'
AUTHOR='gpt-6'
PLAN='Open palm with rounded fingertips, horizontal thumb crease and open right wrist.'
CONSTRUCTION_REFERENCE='Lucide hand-helping: smooth palm and crease construction; supplied gesture controls orientation.'
class Drawing(Solo48):
    icon_id='open-palm-helping-hand'
    keyshape=Keyshape.HRECT_M
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('give', 'hand', '1')
    def circle(self,n,x,y,r):
        self.add_arc(n+'-top',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-bottom',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-top',n+'-bottom',closed=True)

    def path(self,n,start,commands,closed=False):
        ids=[];here=start
        for i,c in enumerate(commands):
            tag,end,*args=c; eid=f'{n}-{i}'
            if tag=='L': self.add_line(eid,here,end)
            elif tag=='A': self.add_arc(eid,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
            elif tag=='C': self.add_bezier(eid,here,(args[0],args[1],end))
            ids.append(eid);here=end
        self.add_contour(n,*ids,closed=closed)

    def box(self,n,l,t,r,b,rad=4):
        self.path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)

    def file(self,l=8,t=4,r=40,b=44):
        self.path('page',(l+4,t),[('L',(r-10,t)),('L',(r,t+10)),('L',(r,b-4)),('A',(r-4,b),4,4,True),('L',(l+4,b)),('A',(l,b-4),4,4,True),('L',(l,t+4)),('A',(l+4,t),4,4,True)],True)

    def build(self):
        self.path('upper',(44,16),[('C',(30,10),(38,16),(36,10)),('C',(20,14),(26,10),(24,14)),('L',(18,14)),('A',(18,22),4,4,False),('L',(28,22))])
        self.path('palm',(14,18),[('L',(8,13)),('C',(4,18),(5,10),(4,14)),('C',(22,38),(4,24),(15,38)),('C',(36,34),(28,38),(30,34)),('C',(44,34),(40,34),(42,34))])
        self.relate('connect','upper','palm')

# Keyshape: HRECT_M balances the horizontal open hand and its cupped palm.
# Visual review: Thumb now turns into a horizontal crease; palm and open wrist follow the upturned gesture. Deeper palm curvature fits the required keyshape.
OMISSIONS='Fine finger divisions omitted; the source has one principal thumb crease.'
