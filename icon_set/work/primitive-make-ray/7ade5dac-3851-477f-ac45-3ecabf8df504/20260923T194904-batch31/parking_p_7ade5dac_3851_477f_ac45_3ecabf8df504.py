"""A car beneath a circular parking sign.
Symbol plan: Front-view car is partially behind the upper-right parking circle. Ink extremes (4,4)-(44,44).
Construction: circle-parking: circle with a P; car-front inspected in batch30 for roof, body and paired wheels.
Human construction: Not applicable.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '7ade5dac-3851-477f-ac45-3ecabf8df504'
SOURCE_PATH = 'icon_set/work/todo-references/parking p_7ade5dac-3851-477f-ac45-3ecabf8df504.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'parking-p'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('parking', 'p')

    def build(self):
        nodes=[(32,6),(42,16),(32,26),(24,22),(22,16)]
        for i,a in enumerate(nodes):self.add_arc(f'sign-{i}',a,nodes[(i+1)%len(nodes)],radius_x=10)
        self.add_contour('sign',*[f'sign-{i}' for i in range(len(nodes))],closed=True)
        self.parking_letter('p',29,11,22,7,8)
        self.add_polyline('roof-left',(6,30),(10,22),(24,22))
        self.add_line('roof-right',(32,26),(34,30))
        for n in ('roof-left','roof-right'):self.relate('connect',n,'sign')
        self.add_polyline('car-body',(6,30),(34,30),(34,38),(30,38),(10,38),(6,38),closed=True)
        for n in ('roof-left','roof-right'):self.relate('connect',n,'car-body')
        for i,x in enumerate((10,30)):
            self.add_line(f'wheel-{i}',(x,38),(x,42))
            self.relate('connect',f'wheel-{i}','car-body')

    def circle(self, name, cx, cy, rx, ry=None):
        ry = rx if ry is None else ry
        self.add_arc(name+'-upper',(cx-rx,cy),(cx+rx,cy),radius_x=rx,radius_y=ry)
        self.add_arc(name+'-lower',(cx+rx,cy),(cx-rx,cy),radius_x=rx,radius_y=ry)
        self.add_contour(name,name+'-upper',name+'-lower',closed=True)

    def box(self, name, x, y, right, bottom, r=4):
        pts=[(x+r,y),(right-r,y),(right,y+r),(right,bottom-r),(right-r,bottom),(x+r,bottom),(x,bottom-r),(x,y+r)]
        members=[]
        for i in range(8):
            a,b=pts[i],pts[(i+1)%8]
            if a==b: continue
            n=f'{name}-{i}'
            if i%2: self.add_arc(n,a,b,radius_x=r)
            else: self.add_line(n,a,b)
            members.append(n)
        self.add_contour(name,*members,closed=True)

    def parking_letter(self,name,x,top,bottom,width=10,bowl_height=14):
        # Vertical stem split at the bowl attachment; one smooth half-ellipse owns its loop.
        mid=top+bowl_height; shoulder=x+3
        self.add_line(name+'-stem-upper',(x,mid),(x,top))
        self.add_line(name+'-top',(x,top),(shoulder,top))
        self.add_arc(name+'-bowl',(shoulder,top),(shoulder,mid),radius_x=width-3,radius_y=bowl_height//2)
        self.add_line(name+'-return',(shoulder,mid),(x,mid))
        self.add_contour(name+'-loop',name+'-stem-upper',name+'-top',name+'-bowl',name+'-return',closed=True)
        self.add_line(name+'-stem-lower',(x,mid),(x,bottom))
        self.relate('connect',name+'-loop',name+'-stem-lower')

    def plus(self,x,y,r=2):
        names=[]
        for i,p in enumerate(((x-r,y),(x+r,y),(x,y-4),(x,y+4))):
            n=f'plus-{i}';self.add_line(n,p,(x,y))
            for prev in names:self.relate('connect',n,prev)
            names.append(n)

