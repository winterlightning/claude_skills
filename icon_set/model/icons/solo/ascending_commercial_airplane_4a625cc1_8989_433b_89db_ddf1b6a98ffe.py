"""Side-view airliner climbs rightward with a broad round nose, long lower edge, angular upper-left wing and a deep notch above its left tail."""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID='4a625cc1-8989-433b-89db-ddf1b6a98ffe'
SOURCE_PATH='pictographic-primitives/other/airplane_4a625cc1-8989-433b-89db-ddf1b6a98ffe.svg'
AUTHOR='gpt-6'
PLAN='Side-view airliner climbs rightward with a broad round nose, long lower edge, angular upper-left wing and a deep notch above its left tail.'
CONSTRUCTION_REFERENCE='plane-takeoff original and atomic-debug: sloping fuselage, single visible wing and rear fin.'
OMISSIONS='No defining features omitted; ground line is not in the supplied reference and is not added.'
class Drawing(Solo48):
    icon_id='ascending-commercial-airplane'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('airplane',)

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
        self.path('airframe',(30,18),[('L',(36,14)),('C',(44,18),(40,11),(44,13)),('C',(40,24),(44,21),(42,23)),('L',(16,39)),('C',(12,40),(14,40),(13,40)),('L',(4,32)),('L',(8,26)),('L',(14,28)),('L',(22,23)),('L',(8,14)),('L',(16,8)),('L',(30,18))],True)

# Keyshape rationale: HRECT_L fits the diagonal fuselage and projecting wing.
# Visual review: Upward-right side view, broad rounded nose, angular wing and open V notch match the feedback.
