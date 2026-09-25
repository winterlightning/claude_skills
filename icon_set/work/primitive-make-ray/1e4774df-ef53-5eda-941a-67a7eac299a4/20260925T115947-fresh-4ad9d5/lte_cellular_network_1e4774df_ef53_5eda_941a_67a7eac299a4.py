"""Capital LTE in one row with aligned tops and baselines; shared eight-unit letter width and spacing."""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='1e4774df-ef53-5eda-941a-67a7eac299a4'
SOURCE_PATH='pictographic-primitives/mobile/lte_1e4774df-ef53-5eda-941a-67a7eac299a4.svg'
AUTHOR='gpt-6'
PLAN='All three letters share top y10, baseline y38, 8-unit widths and 8-unit gaps. The height is reduced from the previous 32 units to 28 while retaining the source letter forms.'
CONSTRUCTION_REFERENCE='No useful Lucide letter-set match; supplied LTE reference determines the three letters.'
OMISSIONS='No omissions. This is custom SOLO48 lettering, not typeface v2.'
class Drawing(Solo48):
    icon_id='lte-cellular-network'
    keyshape=Keyshape.HRECT_M
    semantic_role='MAIN'
    semantic_kind='noun'
    aliases=()
    keywords=('lte',)
    category='objects/general'

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
        top,bottom=10,38;middle=24
        self.add_polyline('l',(4,top),(4,bottom),(12,bottom))
        self.add_polyline('t-bar',(20,top),(24,top),(28,top))
        self.add_line('t-stem',(24,top),(24,bottom));self.relate('connect','t-stem','t-bar')
        self.add_polyline('e',(44,top),(36,top),(36,middle),(36,bottom),(44,bottom))
        self.add_line('e-middle',(36,middle),(44,middle));self.relate('connect','e-middle','e')
