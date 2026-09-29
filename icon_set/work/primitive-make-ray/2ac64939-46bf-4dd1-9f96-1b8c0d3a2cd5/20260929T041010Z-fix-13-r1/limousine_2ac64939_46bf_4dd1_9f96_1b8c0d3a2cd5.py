"""Rejected short high cabin reads as a normal car. Stretch the cabin, lower the body, reduce wheel dominance and retain the center window divider."""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='2ac64939-46bf-4dd1-9f96-1b8c0d3a2cd5'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__limousine/20260929T041010Z-thuan-mac/reference/limo_2ac64939-46bf-4dd1-9f96-1b8c0d3a2cd5.svg'
AUTHOR='gpt-6'
PLAN='Rejected short high cabin reads as a normal car. Stretch the cabin, lower the body, reduce wheel dominance and retain the center window divider.'
CONSTRUCTION_REFERENCE='Lucide car original and atomic-debug: wheels sit in a continuous low chassis.'
OMISSIONS='Only insignificant source detail omitted.'
class Drawing(Solo48):
    icon_id='limousine'
    keyshape=Keyshape.HRECT_M
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
        self.circle('wheel-left',11,33,5);self.circle('wheel-right',37,33,5)
        self.path('body',(6,33),[('L',(4,33)),('L',(4,25)),('A',(8,21),4,4,True),('L',(11,21)),('L',(19,10)),('L',(30,10)),('L',(39,21)),('L',(40,21)),('A',(44,25),4,4,True),('L',(44,33)),('L',(42,33))])
        self.add_line('sill',(16,33),(32,33));self.add_line('windows',(11,21),(39,21));self.add_line('divider',(25,10),(25,21))
        self.relate('connect','body','wheel-left','wheel-right','windows','divider');self.relate('connect','windows','divider');self.relate('connect','sill','wheel-left','wheel-right')
