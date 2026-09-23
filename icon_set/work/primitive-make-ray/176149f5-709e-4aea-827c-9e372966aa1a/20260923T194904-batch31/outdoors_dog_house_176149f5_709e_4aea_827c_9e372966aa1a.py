"""A standing dog underneath a sloping outdoor shelter.
Symbol plan: One lean-to outline encloses a coherent dog silhouette with ear, muzzle, back, belly and legs. Ink extremes (4,4)-(44,44).
Construction: dog: coherent animal contour and purposeful pointed ear; input owns the full-body pose.
Human construction: Not applicable.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '176149f5-709e-4aea-827c-9e372966aa1a'
SOURCE_PATH = 'icon_set/work/todo-references/outdoors dog house_176149f5-709e-4aea-827c-9e372966aa1a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'outdoors-dog-house'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('outdoors', 'dog', 'house')

    def build(self):
        self.add_polyline('shelter',(42,6),(6,18),(6,42),(42,42))
        self.add_bezier('dog-back',(12,28),((13,23),(14,22),(18,22)),((22,22),(28,22),(30,22)))
        self.add_line('dog-head-1',(30, 22),(35, 14))
        self.add_line('dog-head-2',(35, 14),(36, 19))
        self.add_line('dog-head-3',(36, 19),(42, 22))
        self.add_line('dog-head-4',(42, 22),(40, 25))
        self.add_line('dog-head-5',(40, 25),(36, 25))
        self.add_bezier('dog-chest',(36,25),((33,27),(33,31),(33,36)))
        self.add_line('dog-front-leg-1',(33, 36),(35, 38))
        self.add_line('dog-front-leg-2',(35, 38),(29, 38))
        self.add_line('dog-front-leg-3',(29, 38),(29, 30))
        self.add_line('dog-front-leg-4',(29, 30),(22, 30))
        self.add_bezier('dog-belly',(22,30),((19,30),(19,35),(18,38)))
        self.add_line('dog-hind-leg-1',(18, 38),(13, 38))
        self.add_line('dog-hind-leg-2',(13, 38),(13, 32))
        self.add_line('dog-hind-leg-3',(13, 32),(16, 28))
        self.add_contour('dog','dog-back','dog-head-1','dog-head-2','dog-head-3','dog-head-4','dog-head-5','dog-chest','dog-front-leg-1','dog-front-leg-2','dog-front-leg-3','dog-front-leg-4','dog-belly','dog-hind-leg-1','dog-hind-leg-2','dog-hind-leg-3')

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

