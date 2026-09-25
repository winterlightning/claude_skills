"""Hospital with a tall center block, lower side wings, clear medical cross and central doorway."""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID='d9212b2f-353c-4ae0-96bd-8e2bf060245f'
SOURCE_PATH='pictographic-primitives/other/hospital 1_d9212b2f-353c-4ae0-96bd-8e2bf060245f.svg'
AUTHOR='gpt-6'
PLAN='The cross arms are larger, both side-wing divisions are restored, and the central doorway is retained. Equal wing widths and a shared center axis control all details.'
CONSTRUCTION_REFERENCE='hospital original and atomic-debug: cross, side blocks and central entry.'
OMISSIONS='No defining parts omitted. Overall building is wider and lower than the source to preserve cross clearance.'
class Drawing(Solo48):
    icon_id='hospital-with-cross'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    aliases=()
    keywords=('hospital', '1')
    category = 'primitives-generate'

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
        self.add_polyline('center',(12,40),(12,24),(12,8),(36,8),(36,24),(36,40),(28,40),(28,32),(20,32),(20,40),(12,40))
        self.add_polyline('wing-l',(12,24),(4,24),(4,40),(12,40));self.relate('connect','wing-l','center')
        self.add_polyline('wing-r',(36,24),(44,24),(44,40),(36,40));self.relate('connect','wing-r','center')
        self.add_line('cross-h',(20,20),(28,20));self.add_line('cross-v',(24,16),(24,24));self.relate('connect','cross-h','cross-v')
