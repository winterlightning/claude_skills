from ...keyshapes import Keyshape
from icon_set.model.profiles import Profile
from ._base import Solo48
SOURCE_ICON_ID='8d4aec38-b440-43a0-b4f2-b3a846ae4cb1'
SOURCE_PATH='pictographic-primitives/other/person magnifying glass_8d4aec38-b440-43a0-b4f2-b3a846ae4cb1.svg'
AUTHOR='gpt-6'
PLAN='Larger circular lens with eight mirrored cubic octants and radial handle at37,37. Human-reference user.svg: round head radius3, shoulder apex29 and head bottom21 => exact8 centerline/4 ink gap. Short open bust inside lens; deliberate handle asymmetry.'
class Drawing(Solo48):
    icon_id='person-magnifying-glass-solo'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    categories = ('other', 'primitives-generate')
    aliases=()
    keywords=('person', 'magnifying', 'glass', 'solo')
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)
    def build(self):
        # Eight smoothly joined cubic octants keep all control points on the grid.
        self.path('lens',(24,6),[('B',(37,11),(29,6),(34,8)),('B',(42,24),(40,14),(42,19)),('B',(37,37),(42,29),(40,34)),('B',(24,42),(34,40),(29,42)),('B',(11,37),(19,42),(14,40)),('B',(6,24),(8,34),(6,29)),('B',(11,11),(6,19),(8,14)),('B',(24,6),(14,8),(19,6))],True)
        self.add_line('handle',(37,37),(42,42));self.relate('connect','lens','handle')
        self.circle('person-head',24,18,3)
        self.add_arc('shoulders',(19,31),(29,31),radius_x=5,radius_y=2)
        self.add_line('body-left',(19,31),(19,32));self.add_line('body-right',(29,31),(29,32))
        self.relate('connect','shoulders','body-left');self.relate('connect','shoulders','body-right')

    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)
    def path(self,n,start,ops,closed=False):
        at=start;members=[]
        for i,op in enumerate(ops):
            eid=f'{n}-{i}';kind,end,*args=op
            if end==at:continue
            if kind=='L':self.add_line(eid,at,end)
            elif kind=='A':self.add_arc(eid,at,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
            elif kind=='B':self.add_bezier(eid,at,(*args,end))
            at=end;members.append(eid)
        self.add_contour(n,*members,closed=closed)
    def rect(self,n,l,t,r,b,q=4):
        self.path(n,(l+q,t),[('L',(r-q,t)),('A',(r,t+q),q,q,True),('L',(r,b-q)),('A',(r-q,b),q,q,True),('L',(l+q,b)),('A',(l,b-q),q,q,True),('L',(l,t+q)),('A',(l+q,t),q,q,True)],True)

    def monitor(self,l=6,t=6,r=42,b=34,foot=42):
        q=4
        self.path('screen',(l+q,t),[('L',(r-q,t)),('A',(r,t+q),q,q,True),('L',(r,b-q)),('A',(r-q,b),q,q,True),('L',(24,b)),('L',(l+q,b)),('A',(l,b-q),q,q,True),('L',(l,t+q)),('A',(l+q,t),q,q,True)],True)
        self.add_line('stand',(24,b),(24,foot))
        self.add_polyline('foot',(16,foot),(24,foot),(32,foot))
        self.relate('connect','stand','screen');self.relate('connect','stand','foot')
