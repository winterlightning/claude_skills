"""A pig profile facing an apple pictured on a panel.
Symbol plan: A cropped pig head faces right toward an upright apple panel. Ink extremes (4,4)-(44,44).
Construction: apple: twin lobes, central indentation and curved stem; piggy-bank: projecting snout and pointed ear.
Human construction: Not applicable.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '1c6d508d-38fb-4b6a-bfe9-e20ebd9e9bf4'
SOURCE_PATH = 'icon_set/work/todo-references/outdoors pig apple_1c6d508d-38fb-4b6a-bfe9-e20ebd9e9bf4.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'outdoors-pig-apple'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('outdoors', 'pig', 'apple')

    def build(self):
        self.add_polyline('panel',(22,30),(22,6),(42,6),(42,38),(22,38),(22,34))
        self.add_bezier('pig-jaw',(8,42),((10,37),(17,36),(22,34)))
        self.add_bezier('snout',(22,34),((25,34),(26,30),(22,30)))
        self.add_bezier('pig-forehead',(22,30),((17,30),(14,25),(12,24)))
        self.add_bezier('ear',(12,24),((11,19),(8,18),(6,18)),((6,24),(8,25),(12,24)))
        self.add_contour('pig-profile','pig-jaw','snout','pig-forehead')
        self.relate('connect','pig-profile','ear')
        self.relate('connect','pig-profile','panel')
        self.add_bezier('apple',(32,19),((25,15),(26,29),(32,28)),((38,30),(39,16),(32,19)))
        self.add_contour('apple-outline','apple',closed=True)
        self.add_bezier('stem',(32,19),((32,16),(32,15),(34,14)))
        self.relate('connect','stem','apple-outline')

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

