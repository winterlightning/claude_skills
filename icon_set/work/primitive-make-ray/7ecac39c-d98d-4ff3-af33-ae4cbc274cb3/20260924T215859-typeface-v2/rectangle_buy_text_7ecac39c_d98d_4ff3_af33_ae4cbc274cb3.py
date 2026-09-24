from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='7ecac39c-d98d-4ff3-af33-ae4cbc274cb3'
SOURCE_PATH='pictographic-primitives/other/rectangle buy text_7ecac39c-d98d-4ff3-af33-ae4cbc274cb3.svg'
AUTHOR='gpt-6'
PLAN='Typeface v2 native paths translated only. Full word retained. Strict SOLO48 fit attempt.'
class Drawing(Solo48):
    icon_id='rectangle-buy-text'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('rectangle', 'buy', 'text')
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)
    def build(self):
        self.rect('button',4,8,44,40)
        self.add_line('glyph-0-0-0',(3.9998999999999967, 16.49975),(7.144639999999997, 16.49975))
        self.add_bezier('glyph-0-0-1',(7.144639999999997, 16.49975),((9.139699999999996, 16.49975), (10.756999999999996, 18.11704), (10.756999999999996, 20.11208)))
        self.add_line('glyph-0-0-2',(10.756999999999996, 20.11208),(10.756999999999996, 20.387430000000002))
        self.add_bezier('glyph-0-0-3',(10.756999999999996, 20.387430000000002),((10.756999999999996, 22.382460000000002), (9.140099999999997, 23.49975), (7.145089999999996, 23.49975)))
        self.add_line('glyph-0-0-4',(7.145089999999996, 23.49975),(4.0003499999999965, 23.49975))
        self.add_line('glyph-0-0-5',(4.0003499999999965, 23.49975),(3.9998999999999967, 16.49975))
        self.add_contour("glyph-0-0",*['glyph-0-0-0', 'glyph-0-0-1', 'glyph-0-0-2', 'glyph-0-0-3', 'glyph-0-0-4', 'glyph-0-0-5'],closed=True)
        self.add_line('glyph-0-1-0',(4.000799999999996, 23.50927),(8.388019999999997, 23.50927))
        self.add_bezier('glyph-0-1-1',(8.388019999999997, 23.50927),((10.383099999999997, 23.50927), (11.999899999999997, 25.62655), (11.999899999999997, 27.62155)))
        self.add_line('glyph-0-1-2',(11.999899999999997, 27.62155),(11.999899999999997, 27.88755))
        self.add_bezier('glyph-0-1-3',(11.999899999999997, 27.88755),((11.999899999999997, 29.882550000000002), (10.382599999999996, 31.499850000000002), (8.387569999999997, 31.499850000000002)))
        self.add_line('glyph-0-1-4',(8.387569999999997, 31.499850000000002),(4.0003499999999965, 31.499850000000002))
        self.add_line('glyph-0-1-5',(4.0003499999999965, 31.499850000000002),(4.000799999999996, 23.50927))
        self.add_contour("glyph-0-1",*['glyph-0-1-0', 'glyph-0-1-1', 'glyph-0-1-2', 'glyph-0-1-3', 'glyph-0-1-4', 'glyph-0-1-5'],closed=True)
        self.add_line('glyph-1-0-0',(28.0001, 16.49975),(28.0001, 28.49975))
        self.add_bezier('glyph-1-0-1',(28.0001, 28.49975),((28.0001, 28.49975), (27.9999, 31.49975), (23.99988, 31.49975)))
        self.add_bezier('glyph-1-0-2',(23.99988, 31.49975),((19.9999, 31.49975), (19.9999, 28.49975), (19.9999, 28.49975)))
        self.add_line('glyph-1-0-3',(19.9999, 28.49975),(19.9999, 16.49975))
        self.add_contour("glyph-1-0",*['glyph-1-0-0', 'glyph-1-0-1', 'glyph-1-0-2', 'glyph-1-0-3'],closed=False)
        self.add_line('glyph-2-0-0',(44.0001, 16.50024),(40.0001, 24.50025))
        self.add_contour("glyph-2-0",*['glyph-2-0-0'],closed=False)
        self.add_line('glyph-2-1-0',(36.0001, 16.50024),(40.0001, 24.50025))
        self.add_contour("glyph-2-1",*['glyph-2-1-0'],closed=False)
        self.add_line('glyph-2-2-0',(40.0001, 24.50025),(40.0001, 31.50025))
        self.add_contour("glyph-2-2",*['glyph-2-2-0'],closed=False)

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
