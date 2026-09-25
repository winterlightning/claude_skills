"""An open book above an online-course panel.
Symbol plan: Mirrored page curves share a central spine; a wide panel and centered rule sit below. Ink extremes (6,2)-(42,46).
Construction: book-open: mirrored bowed pages and a shared central spine.
Human construction: Not applicable.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '82791e1b-7e30-4905-85e9-1bf64f1e2489'
SOURCE_PATH = 'icon_set/work/todo-references/online learning online course 2_82791e1b-7e30-4905-85e9-1bf64f1e2489.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'online-learning-online-course-2'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('online', 'learning', 'online', 'course', '2')

    def build(self):
        self.add_bezier('book-top',(10,4),((18,4),(21,5),(24,8)),((27,5),(30,4),(38,4)))
        self.add_line('book-right',(38,4),(38,16))
        self.add_bezier('book-bottom',(38,16),((30,16),(27,17),(24,20)),((21,17),(18,16),(10,16)))
        self.add_line('book-left',(10,16),(10,4))
        self.add_contour('book','book-top','book-right','book-bottom','book-left',closed=True)
        self.add_line('spine',(24,8),(24,20))
        self.relate('connect','spine','book')
        self.add_polyline('online-panel',(8,28),(40,28),(40,44),(8,44),closed=True)
        self.add_line('panel-rule',(16,36),(32,36))

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

