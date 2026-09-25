"""The OpenVPN keyhole logo within an open circular arc.
Symbol plan: An incomplete radius-20 outer circle frames a circular-headed, tapered keyhole. Ink radius22 about(24,24).
Construction: No useful exact Lucide match found; supplied logo owns the construction.
Human construction: Not applicable.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'df6e98df-8c0b-4cb1-a4f6-d0483b468f10'
SOURCE_PATH = 'icon_set/work/todo-references/openvpn logo_df6e98df-8c0b-4cb1-a4f6-d0483b468f10.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'openvpn-logo'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('openvpn', 'logo')

    def build(self):
        self.add_arc('outer-left',(8,36),(24,4),radius_x=20)
        self.add_arc('outer-right',(24,4),(40,36),radius_x=20)
        self.add_contour('outer-ring','outer-left','outer-right')
        self.add_bezier('keyhole-head',(20,27),((12,23),(16,13),(24,13)),((32,13),(36,23),(28,27)))
        self.add_line('keyhole-right',(28,27),(32,40))
        self.add_bezier('keyhole-base',(32,40),((32,42),(16,42),(16,40)))
        self.add_line('keyhole-left',(16,40),(20,27))
        self.add_contour('keyhole','keyhole-head','keyhole-right','keyhole-base','keyhole-left',closed=True)

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

