"""The letters P and B separated by a plus sign.
Symbol plan: Two upright hand-built letterforms flank a centered plus. Shared bowl dimensions preserve the text series. Ink extremes (2,8)-(46,40).
Construction: square-parking: open stem and smooth P bowl; B/R authored using the same bowl definition.
Human construction: Not applicable.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'dfc037b7-3cf4-5183-a3ea-94c433baaa81'
SOURCE_PATH = 'icon_set/work/todo-references/park and bike_dfc037b7-3cf4-5183-a3ea-94c433baaa81.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'park-and-bike'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('park', 'and', 'bike')

    def build(self):
        self.parking_letter('p',4,10,38,10,14)
        self.plus(24,24)
        self.parking_letter('right',34,10,38,10,14)
        self.add_line('b-mid',(34,24),(37,24))
        self.add_arc('b-lower-bowl',(37,24),(37,38),radius_x=7)
        self.add_line('b-base',(37,38),(34,38))
        self.add_contour('lower-bowl','b-mid','b-lower-bowl','b-base')
        self.relate('connect','lower-bowl','right-loop')
        self.relate('connect','lower-bowl','right-stem-lower')

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

