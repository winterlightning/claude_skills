"""An outpost shelter with a checkpoint box in front.
Symbol plan: Pitched roof and paired posts frame the centered upright checkpoint box. Ink extremes (4,4)-(44,44).
Construction: house: mirrored pitched roof and supports; input owns the foreground checkpoint arrangement.
Human construction: Not applicable.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '186ecce7-6734-413e-9fd9-e45cba4787b3'
SOURCE_PATH = 'icon_set/work/todo-references/outpost 1_186ecce7-6734-413e-9fd9-e45cba4787b3.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'outpost-1'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('outpost', '1')

    def build(self):
        self.add_polyline('roof',(6,18),(12,14),(24,6),(36,14),(42,18))
        for i,x in enumerate((12,36)):
            self.add_line(f'post-{i}',(x,14),(x,34))
            self.relate('connect',f'post-{i}','roof')
        for i,(a,b) in enumerate(((6,16),(32,42))):
            self.add_line(f'ground-{i}',(a,34),(b,34))
            self.relate('connect',f'ground-{i}',f'post-{i}')
        self.box('checkpoint',16,22,32,42,4)
        self.add_line('checkpoint-divider',(16,32),(32,32))
        self.relate('connect','checkpoint-divider','checkpoint')
        for i in range(2):self.relate('connect',f'ground-{i}','checkpoint')
        self.add_line('checkpoint-mark',(22,37),(26,37))

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

