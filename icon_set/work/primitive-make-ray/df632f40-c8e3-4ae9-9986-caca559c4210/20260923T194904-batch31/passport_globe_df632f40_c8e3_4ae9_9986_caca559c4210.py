"""A passport showing a globe in front of a larger world globe.
Symbol plan: Large globe is occluded by the foreground passport; the cover carries a small gridded globe. Ink extremes (4,4)-(44,44).
Construction: globe: circular outline, elliptical meridian and equator; book: foreground cover.
Human construction: Not applicable.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'df632f40-c8e3-4ae9-9986-caca559c4210'
SOURCE_PATH = 'icon_set/work/todo-references/passport globe_df632f40-c8e3-4ae9-9986-caca559c4210.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'passport-globe'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('passport', 'globe')

    def build(self):
        self.add_arc('world',(34,20),(20,34),radius_x=14,large_arc=True,sweep=False)
        self.add_polyline('continent',(6,20),(14,20),(14,26),(12,26),(12,31))
        self.relate('connect','world','continent')
        self.box('passport',20,20,42,42,3)
        self.relate('connect','world','passport')
        # Four cardinal nodes are shared by the cover globe, equator and meridian.
        nodes=[(31,25),(37,31),(31,37),(25,31)]
        for i,a in enumerate(nodes):self.add_arc(f'globe-{i}',a,nodes[(i+1)%4],radius_x=6)
        self.add_contour('globe',*[f'globe-{i}' for i in range(4)],closed=True)
        self.add_arc('meridian-right',(31,25),(31,37),radius_x=2,radius_y=6)
        self.add_arc('meridian-left',(31,37),(31,25),radius_x=2,radius_y=6)
        self.add_contour('meridian','meridian-right','meridian-left',closed=True)
        self.relate('connect','meridian','globe')
        self.add_line('equator',(25,31),(37,31))
        self.relate('connect','equator','globe')
        self.relate('connect','equator','meridian')

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

