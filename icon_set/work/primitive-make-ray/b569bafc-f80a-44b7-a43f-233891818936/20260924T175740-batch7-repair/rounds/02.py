"""A passport booklet with a globe printed on its cover.
Symbol plan: Offset upper cover edge and a rounded front cover enclose a latitude/longitude globe. Ink extremes (6,2)-(42,46).
Construction: globe: round world outline with longitude and latitude strokes; book: offset cover edge.
Human construction: Not applicable.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'b569bafc-f80a-44b7-a43f-233891818936'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_30/passport hand_b569bafc-f80a-44b7-a43f-233891818936.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'passport-hand'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('passport', 'hand')

    def build(self):
        self.box('cover',8,12,40,44,4)
        self.add_line('back-left',(8,12),(8,8))
        self.add_arc('back-tl',(8,8),(12,4),radius_x=4)
        self.add_line('back-top',(12,4),(32,4))
        self.add_arc('back-tr',(32,4),(36,8),radius_x=4)
        self.add_line('back-right',(36,8),(36,12))
        self.add_contour('back-cover','back-left','back-tl','back-top','back-tr','back-right')
        self.relate('connect','back-cover','cover')
        # Four cardinal circle quadrants expose exact equator/meridian attachment nodes.
        nodes=[(17,28),(24,21),(31,28),(24,35)]
        for i,a in enumerate(nodes):self.add_arc(f'globe-{i}',a,nodes[(i+1)%4],radius_x=7)
        self.add_contour('globe',*[f'globe-{i}' for i in range(4)],closed=True)
        self.add_polyline('equator',(17,28),(24,28),(31,28))
        self.relate('connect','equator','globe')

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

