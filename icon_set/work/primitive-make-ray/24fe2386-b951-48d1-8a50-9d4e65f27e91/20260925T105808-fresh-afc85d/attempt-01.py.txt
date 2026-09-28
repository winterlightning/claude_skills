"""Browser enclosing distinct hand-drawn capital A and D; widened layout budgets the side walls and letters."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='24fe2386-b951-48d1-8a50-9d4e65f27e91'
SOURCE_PATH='pictographic-primitives/other/ui webpage ad text_24fe2386-b951-48d1-8a50-9d4e65f27e91.svg'
AUTHOR='gpt-6'
PLAN='Browser enclosing distinct hand-drawn capital A and D; widened layout budgets the side walls and letters.'
CONSTRUCTION_REFERENCE='panels-top-left: rounded chrome'
OMISSIONS='Tiny header dashes omitted to reserve text area.'

class Drawing(Solo48):
    icon_id='webpage-advertisement'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('ui', 'webpage', 'ad', 'text')

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
        self.box('browser',4,8,44,40)
        self.add_line('header',(4,16),(44,16)); self.relate('connect','header','browser')
        self.add_polyline('a',(12,32),(16,22),(20,32))
        self.add_line('crossbar',(14,28),(18,28));self.relate('connect','a','crossbar')
        self.add_line('d-stem',(28,24),(28,32))
        self.add_arc('d-bowl',(28,24),(28,32),radius_x=8,radius_y=4)
        self.relate('connect','d-stem','d-bowl')
