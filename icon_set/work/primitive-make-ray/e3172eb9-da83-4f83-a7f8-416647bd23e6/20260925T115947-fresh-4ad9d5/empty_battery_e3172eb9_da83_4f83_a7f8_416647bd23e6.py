"""Horizontal rounded empty battery with a smaller rounded attached terminal."""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='e3172eb9-da83-4f83-a7f8-416647bd23e6'
SOURCE_PATH='pictographic-primitives/photography/battery_e3172eb9-da83-4f83-a7f8-416647bd23e6.svg'
AUTHOR='gpt-6'
PLAN='The empty cell has matched small-radius corners and a smaller rounded right terminal. Both terminal joins are real connections to the cell.'
CONSTRUCTION_REFERENCE='battery original and atomic-debug: simple cell silhouette; source owns attached terminal.'
OMISSIONS='No omissions.'
class Drawing(Solo48):
    icon_id='empty-battery'
    keyshape=Keyshape.HRECT_M
    semantic_role='MAIN'
    semantic_kind='noun'
    aliases=()
    keywords=('battery',)
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
        self.box('cell',4,10,36,38,3)
        self.path('terminal',(36,18),[('L',(42,18)),('A',(44,20),2,2,True),('L',(44,28)),('A',(42,30),2,2,True),('L',(36,30))])
        self.relate('connect','cell','terminal')
