from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='dd80ecbb-13f8-47dc-9883-44bd19aa7cc6'
SOURCE_PATH='pictographic-primitives/other/monitor letters_dd80ecbb-13f8-47dc-9883-44bd19aa7cc6.svg'
AUTHOR='gpt-6'
PLAN='Typeface v2 native paths translated only. Full word retained. Strict SOLO48 fit attempt.'
class Drawing(Solo48):
    icon_id='monitor-letters'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('monitor', 'letters')
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)
    def build(self):
        self.monitor(l=4,t=8,r=44,b=32,foot=40)
        self.add_bezier('glyph-0-0-0',(3.9999999999999964, 27.49975250000937),((3.9999999999999964, 27.49975250000937), (4.000059999999997, 19.49979250000937), (4.000059999999997, 15.49989250000937)))
        self.add_bezier('glyph-0-0-1',(4.000059999999997, 15.49989250000937),((4.000059999999997, 11.49998250000937), (11.999999999999996, 11.49995250000937), (11.999999999999996, 15.49988250000937)))
        self.add_bezier('glyph-0-0-2',(11.999999999999996, 15.49988250000937),((11.999999999999996, 16.920642500009368), (11.999999999999996, 27.499852500009368), (11.999999999999996, 27.499852500009368)))
        self.add_contour("glyph-0-0",*['glyph-0-0-0', 'glyph-0-0-1', 'glyph-0-0-2'],closed=False)
        self.add_line('glyph-0-1-0',(3.9999999999999964, 22.570052500009368),(11.999999999999996, 22.570052500009368))
        self.add_contour("glyph-0-1",*['glyph-0-1-0'],closed=False)
        self.add_line('glyph-1-0-0',(19.999999999999996, 12.49995250000937),(23.14474, 12.49995250000937))
        self.add_bezier('glyph-1-0-1',(23.14474, 12.49995250000937),((25.139799999999994, 12.49995250000937), (26.757099999999994, 14.11724250000937), (26.757099999999994, 16.11228250000937)))
        self.add_line('glyph-1-0-2',(26.757099999999994, 16.11228250000937),(26.757099999999994, 16.387632500009367))
        self.add_bezier('glyph-1-0-3',(26.757099999999994, 16.387632500009367),((26.757099999999994, 18.38266250000937), (25.140199999999997, 19.49995250000937), (23.145189999999996, 19.49995250000937)))
        self.add_line('glyph-1-0-4',(23.145189999999996, 19.49995250000937),(20.000449999999997, 19.49995250000937))
        self.add_line('glyph-1-0-5',(20.000449999999997, 19.49995250000937),(19.999999999999996, 12.49995250000937))
        self.add_contour("glyph-1-0",*['glyph-1-0-0', 'glyph-1-0-1', 'glyph-1-0-2', 'glyph-1-0-3', 'glyph-1-0-4', 'glyph-1-0-5'],closed=True)
        self.add_line('glyph-1-1-0',(20.000899999999994, 19.50947250000937),(24.388119999999997, 19.50947250000937))
        self.add_bezier('glyph-1-1-1',(24.388119999999997, 19.50947250000937),((26.383199999999995, 19.50947250000937), (27.999999999999996, 21.626752500009367), (27.999999999999996, 23.62175250000937)))
        self.add_line('glyph-1-1-2',(27.999999999999996, 23.62175250000937),(27.999999999999996, 23.88775250000937))
        self.add_bezier('glyph-1-1-3',(27.999999999999996, 23.88775250000937),((27.999999999999996, 25.882752500009367), (26.382699999999996, 27.500052500009367), (24.387669999999996, 27.500052500009367)))
        self.add_line('glyph-1-1-4',(24.387669999999996, 27.500052500009367),(20.000449999999997, 27.500052500009367))
        self.add_line('glyph-1-1-5',(20.000449999999997, 27.500052500009367),(20.000899999999994, 19.50947250000937))
        self.add_contour("glyph-1-1",*['glyph-1-1-0', 'glyph-1-1-1', 'glyph-1-1-2', 'glyph-1-1-3', 'glyph-1-1-4', 'glyph-1-1-5'],closed=True)
        self.add_bezier('glyph-2-0-0',(44.0, 12.50005250000937),((43.0, 12.49993250000937), (42.511599999999994, 12.49995250000937), (41.6887, 12.49995250000937)))
        self.add_bezier('glyph-2-0-1',(41.6887, 12.49995250000937),((38.54691, 12.49995250000937), (36.0, 15.85781250000937), (36.0, 19.99995250000937)))
        self.add_bezier('glyph-2-0-2',(36.0, 19.99995250000937),((36.0, 24.14205250000937), (38.54691, 27.49995250000937), (41.6887, 27.49995250000937)))
        self.add_bezier('glyph-2-0-3',(41.6887, 27.49995250000937),((42.511599999999994, 27.49995250000937), (43.0, 27.49995250000937), (44.0, 27.49995250000937)))
        self.add_contour("glyph-2-0",*['glyph-2-0-0', 'glyph-2-0-1', 'glyph-2-0-2', 'glyph-2-0-3'],closed=False)

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
