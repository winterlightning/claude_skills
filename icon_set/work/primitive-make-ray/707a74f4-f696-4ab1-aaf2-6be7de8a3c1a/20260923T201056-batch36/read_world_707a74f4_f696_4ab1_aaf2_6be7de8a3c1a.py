"""An open book below a globe dome.
Symbol plan: A symmetric globe dome and meridians sit above bowed book pages and their text marks. Ink extremes (6,2)-(42,46).
Construction: book-open: paired page curvature and shared spine; globe: dome, longitude and latitude grid.
Human construction: Not applicable.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '707a74f4-f696-4ab1-aaf2-6be7de8a3c1a'
SOURCE_PATH = 'icon_set/work/todo-references/read world_707a74f4-f696-4ab1-aaf2-6be7de8a3c1a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'read-world'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('read', 'world')

    def build(self):
        # Radius15 globe: 9-12-15 nodes make every latitude attachment exact.
        nodes=[(9,19),(12,10),(24,4),(36,10),(39,19)]
        for i,(a,b) in enumerate(zip(nodes,nodes[1:])):self.add_arc(f'dome-{i}',a,b,radius_x=15)
        self.add_contour('globe-dome',*[f'dome-{i}' for i in range(4)])
        for name,a,b in [('longitude-left-top',(24,4),(20,10)),('longitude-left-bottom',(20,10),(19,19)),('longitude-right-top',(24,4),(28,10)),('longitude-right-bottom',(28,10),(29,19))]:
            self.add_arc(name,a,b,radius_x=5,radius_y=15,sweep=name.startswith('longitude-right'))
        self.add_contour('longitude-left','longitude-left-top','longitude-left-bottom')
        self.add_contour('longitude-right','longitude-right-top','longitude-right-bottom')
        for n in ('longitude-left','longitude-right'):self.relate('connect',n,'globe-dome')
        self.relate('connect','longitude-left','longitude-right')
        self.add_polyline('latitude',(12,10),(20,10),(28,10),(36,10))
        for n in ('globe-dome','longitude-left','longitude-right'):self.relate('connect','latitude',n)
        self.add_bezier('book-top',(8,27),((16,27),(20,28),(24,31)),((28,28),(32,27),(40,27)))
        self.add_line('book-right',(40,27),(40,40))
        self.add_bezier('book-bottom',(40,40),((32,40),(28,41),(24,44)),((20,41),(16,40),(8,40)))
        self.add_line('book-left',(8,40),(8,27))
        self.add_contour('book','book-top','book-right','book-bottom','book-left',closed=True)
        self.add_line('spine',(24,31),(24,44))
        self.relate('connect','spine','book')
        for i,x in enumerate((14,30)):self.add_line(f'text-{i}',(x,34),(x+4,35))

    def circle(self,name,cx,cy,rx,ry=None):
        ry=rx if ry is None else ry
        self.add_arc(name+'-upper',(cx-rx,cy),(cx+rx,cy),radius_x=rx,radius_y=ry)
        self.add_arc(name+'-lower',(cx+rx,cy),(cx-rx,cy),radius_x=rx,radius_y=ry)
        self.add_contour(name,name+'-upper',name+'-lower',closed=True)

    def box(self,name,x,y,right,bottom,r=4):
        pts=[(x+r,y),(right-r,y),(right,y+r),(right,bottom-r),(right-r,bottom),(x+r,bottom),(x,bottom-r),(x,y+r)]
        members=[]
        for i in range(8):
            a,b=pts[i],pts[(i+1)%8]
            if a==b:continue
            n=f'{name}-{i}'
            if i%2:self.add_arc(n,a,b,radius_x=r)
            else:self.add_line(n,a,b)
            members.append(n)
        self.add_contour(name,*members,closed=True)

    def opening_quote(self,name,x,closing=False):
        # A shared 15-unit body and 25-unit pitch own both repeated quotation marks.
        def p(v):
            a,b=v
            return (x+15-a,48-b) if closing else (x+a,b)
        def line(n,a,b):self.add_line(name+n,p(a),p(b))
        def arc(n,a,b):self.add_arc(name+n,p(a),p(b),radius_x=4)
        def bez(n,a,*segs):self.add_bezier(name+n,p(a),*[(p(a),p(b),p(c)) for a,b,c in segs])
        bez('-outer',(0,24),((0,16),(5,8),(11,8)))
        arc('-crown',(11,8),(15,12))
        arc('-return',(15,12),(11,16))
        bez('-inner',(11,16),((7,16),(7,20),(7,24)))
        line('-shelf',(7,24),(11,24))
        arc('-tr',(11,24),(15,28))
        line('-right',(15,28),(15,36))
        arc('-br',(15,36),(11,40))
        line('-bottom',(11,40),(4,40))
        arc('-bl',(4,40),(0,36))
        line('-left',(0,36),(0,24))
        self.add_contour(name,*[name+n for n in ('-outer','-crown','-return','-inner','-shelf','-tr','-right','-br','-bottom','-bl','-left')],closed=True)

