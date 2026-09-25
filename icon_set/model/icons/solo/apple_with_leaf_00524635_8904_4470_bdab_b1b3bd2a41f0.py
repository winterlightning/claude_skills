"""Round apple with smooth crown and bottom dimples, a stem and an attached right-hand leaf."""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID='00524635-8904-4470-bdab-b1b3bd2a41f0'
SOURCE_PATH='pictographic-primitives/_uncategorized_03/apple whole_00524635-8904-4470-bdab-b1b3bd2a41f0.svg'
AUTHOR='gpt-6'
PLAN='Restored the leaf with an open pointed oval, kept a connecting stem, and rebuilt the apple with smooth upper and lower dimples instead of angular bottom joints.'
CONSTRUCTION_REFERENCE='apple original and atomic-debug: organic paired lobes and shallow bottom dimple.'
OMISSIONS='No defining features omitted; the body is shortened to reserve leaf and stem clearance.'
class Drawing(Solo48):
    icon_id='apple-with-leaf'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    aliases=()
    keywords=('apple', 'whole')
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
        self.path('apple',(24,24),[('C',(16,22),(20,24),(20,22)),('C',(8,30),(10,22),(8,25)),('C',(18,44),(8,38),(12,44)),('C',(24,42),(21,44),(21,42)),('C',(30,44),(27,42),(27,44)),('C',(40,30),(36,44),(40,38)),('C',(32,22),(40,25),(38,22)),('C',(24,24),(28,22),(28,24))],True)
        self.path('leaf',(24,14),[('C',(36,4),(24,6),(30,4)),('C',(24,14),(36,12),(30,14))],True)
        self.add_line('stem',(24,14),(24,24));self.relate('connect','stem','leaf');self.relate('connect','stem','apple')
