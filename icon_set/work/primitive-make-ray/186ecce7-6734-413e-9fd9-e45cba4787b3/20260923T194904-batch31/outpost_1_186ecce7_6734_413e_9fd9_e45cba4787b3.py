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
        self.add_polyline('roof',(6,18),(9,16),(24,6),(39,16),(42,18))
        for i,x in enumerate((9,39)):
            self.add_line(f'post-{i}',(x,16),(x,34))
            self.relate('connect',f'post-{i}','roof')
        self.add_polyline('ground-left',(6,34),(9,34),(18,34))
        self.add_polyline('ground-right',(30,34),(39,34),(42,34))
        self.relate('connect','ground-left','post-0')
        self.relate('connect','ground-right','post-1')
        # The checkpoint wall is split at both the divider and ground attachments.
        self.add_line('box-top',(22,22),(26,22))
        self.add_arc('box-tr',(26,22),(30,26),radius_x=4)
        self.add_line('box-right-upper',(30,26),(30,32))
        self.add_line('box-right-middle',(30,32),(30,34))
        self.add_line('box-right-lower',(30,34),(30,38))
        self.add_arc('box-br',(30,38),(26,42),radius_x=4)
        self.add_line('box-base',(26,42),(22,42))
        self.add_arc('box-bl',(22,42),(18,38),radius_x=4)
        self.add_line('box-left-lower',(18,38),(18,34))
        self.add_line('box-left-middle',(18,34),(18,32))
        self.add_line('box-left-upper',(18,32),(18,26))
        self.add_arc('box-tl',(18,26),(22,22),radius_x=4)
        self.add_contour('checkpoint','box-top','box-tr','box-right-upper','box-right-middle','box-right-lower','box-br','box-base','box-bl','box-left-lower','box-left-middle','box-left-upper','box-tl',closed=True)
        self.add_line('checkpoint-divider',(18,32),(30,32))
        self.relate('connect','checkpoint-divider','checkpoint')
        self.relate('connect','ground-left','checkpoint')
        self.relate('connect','ground-right','checkpoint')

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

