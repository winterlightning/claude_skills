'Rounded currency banknote with four concave corner ornaments and an open central medallion.'
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='b1e5658b-c303-4f04-bd4a-6e87cd1ca809'
SOURCE_PATH='pictographic-primitives/_uncategorized_27/money bill_b1e5658b-c303-4f04-bd4a-6e87cd1ca809.svg'
AUTHOR='gpt-6'
PLAN='Rounded currency banknote with four concave corner ornaments and an open central medallion.'
CONSTRUCTION_REFERENCE='Lucide banknote: rounded outer border and central currency mark; supplied inset ornament.'
class Drawing(Solo48):
    icon_id='decorated-currency-banknote'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('money', 'bill')
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
        self.path('note',(7,8),[('L',(14,8)),('L',(34,8)),('L',(41,8)),('A',(44,11),3,3,True),('L',(44,18)),('L',(44,30)),('L',(44,37)),('A',(41,40),3,3,True),('L',(34,40)),('L',(14,40)),('L',(7,40)),('A',(4,37),3,3,True),('L',(4,30)),('L',(4,18)),('L',(4,11)),('A',(7,8),3,3,True)],True)
        for n,a,b in [('tl',(4,18),(14,8)),('tr',(34,8),(44,18)),('br',(44,30),(34,40)),('bl',(14,40),(4,30))]:
            self.add_arc(n,a,b,radius_x=10,sweep=False);self.relate('connect','note',n)
        self.circle('medallion',24,24,5)

# Keyshape: HRECT_L keeps a wide currency frame and clear circular medallion.
# Visual review: Central open medallion retained. Four concave corner ornaments restore currency detail without crowding a complete nested frame.
OMISSIONS='Continuous inset border reduced to four attached concave corner ornaments; central medallion stays open.'
