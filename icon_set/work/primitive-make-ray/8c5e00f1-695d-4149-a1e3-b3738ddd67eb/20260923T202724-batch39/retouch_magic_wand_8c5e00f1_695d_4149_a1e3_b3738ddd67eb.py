"""A magic retouch wand inside a circular badge.

Plan: Circular boundary encloses a diagonal outlined wand and three plus sparkles.
Construction: wand-sparkles: rounded diagonal tool and detached sparkle series
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '8c5e00f1-695d-4149-a1e3-b3738ddd67eb'
SOURCE_PATH = 'icon_set/work/todo-references/retouch magic wand_8c5e00f1-695d-4149-a1e3-b3738ddd67eb.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'retouch-magic-wand'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('retouch', 'magic', 'wand')

    def build(self):
        self.circle('badge',24,24,20)
        self.add_polyline('wand',(9,36),(24,21),(30,27),(15,42),closed=True)
        self.add_line('tip-band',(20,25),(26,31))
        for name,x,y in [('left',15,16),('top',28,12),('right',36,23)]:
            self.add_polyline(name+'-h',(x-2,y),(x,y),(x+2,y))
            self.add_polyline(name+'-v',(x,y-2),(x,y),(x,y+2))
            for a in (1,2):
                for b in (1,2):self.relate('connect',f'{name}-h-{a}',f'{name}-v-{b}')

    def circle(self, name, x, y, r):
        self.add_arc(name+'-top',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(name+'-bottom',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

    def box(self, name, l, t, r, b, rad=2):
        pts=[(l+rad,t),(r-rad,t),(r,t+rad),(r,b-rad),(r-rad,b),(l+rad,b),(l,b-rad),(l,t+rad)]
        for i in range(8):
            a,z=pts[i],pts[(i+1)%8]
            if i%2:self.add_arc(f'{name}-{i}',a,z,radius_x=rad)
            else:self.add_line(f'{name}-{i}',a,z)
        self.add_contour(name,*(f'{name}-{i}' for i in range(8)),closed=True)

    def arrow(self, name, start, tip, wing1, wing2):
        self.add_line(name+'-shaft',start,tip)
        self.add_polyline(name+'-head',wing1,tip,wing2)
        for i in (1,2):self.relate('connect',name+'-shaft',f'{name}-head-{i}')

    def heart(self, name, x, top, half, bottom):
        # Mirrored lobes share dimensions and meet the pointed lower silhouette.
        self.add_bezier(name+'-left',(x,top+2),((x-half,top-5),(x-half-3,top+4),(x-half,top+7)),((x-half+2,top+10),(x, bottom),(x,bottom)))
        self.add_bezier(name+'-right',(x,bottom),((x,bottom),(x+half-2,top+10),(x+half,top+7)),((x+half+3,top+4),(x+half,top-5),(x,top+2)))
        self.add_contour(name,name+'-left',name+'-right',closed=True)
