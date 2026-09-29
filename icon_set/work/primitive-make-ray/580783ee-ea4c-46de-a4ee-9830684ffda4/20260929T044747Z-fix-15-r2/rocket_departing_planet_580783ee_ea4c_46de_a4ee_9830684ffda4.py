"""Rejected rocket and planet are loose hooks and bars. Restore the pointed rocket with fins, a detached exhaust flame and a round planet with an elliptical departure path."""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='580783ee-ea4c-46de-a4ee-9830684ffda4'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__rocket-departing-planet/20260929T044747Z-thuan-mac/reference/rocket earth_580783ee-ea4c-46de-a4ee-9830684ffda4.svg'
AUTHOR='gpt-6'
PLAN='Rejected rocket and planet are loose hooks and bars. Restore the pointed rocket with fins, a detached exhaust flame and a round planet with an elliptical departure path.'
CONSTRUCTION_REFERENCE='Lucide rocket original/atomic-debug: tapered pointed shell and distinct exhaust; original defines planet and orbit.'
OMISSIONS='Secondary source detail simplified only where needed for 48 px legibility.'
class Drawing(Solo48):
    icon_id='rocket-departing-planet'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=()

    def circle(self,n,x,y,r):
        self.add_arc(n+'a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'a',n+'b',closed=True)
    def path(self,n,start,commands,closed=False):
        ids=[]; here=start
        for i,c in enumerate(commands):
            tag,end,*args=c; eid=f'{n}-{i}'
            if tag=='L': self.add_line(eid,here,end)
            elif tag=='A': self.add_arc(eid,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
            elif tag=='C': self.add_bezier(eid,here,(args[0],args[1],end))
            ids.append(eid); here=end
        self.add_contour(n,*ids,closed=closed)
    def box(self,n,l,t,r,b,rad=3):
        self.path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)

    def build(self):
        self.path('planet',(27,16),[('C',(7,23),(18,10),(8,15)),('C',(20,42),(3,33),(10,42)),('C',(34,27),(30,42),(38,35))])
        self.path('rocket',(31,13),[('C',(42,6),(34,8),(38,7)),('C',(37,20),(42,12),(40,17)),('L',(34,23)),('L',(27,16)),('L',(31,13))],True)
        self.add_polyline('fin',(31,13),(27,12),(26,15));self.relate('connect','rocket','fin')
        self.add_line('exhaust',(29,24),(25,28))
        self.path('trail',(19,30),[('C',(6,42),(12,39),(4,46)),('C',(7,32),(2,40),(5,34))])
        self.relate('connect','planet','trail')
