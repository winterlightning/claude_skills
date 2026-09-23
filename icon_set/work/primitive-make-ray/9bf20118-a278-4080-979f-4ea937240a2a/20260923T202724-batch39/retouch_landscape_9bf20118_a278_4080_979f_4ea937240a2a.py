"""A landscape picture with a retouch wand and sparkle.

Plan: Open picture boundary holds two mountains and a sun; detached diagonal wand at upper right.
Construction: wand-sparkles: diagonal wand and sparse rays
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '9bf20118-a278-4080-979f-4ea937240a2a'
SOURCE_PATH = 'icon_set/work/todo-references/retouch landscape_9bf20118-a278-4080-979f-4ea937240a2a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'retouch-landscape'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('retouch', 'landscape')

    def build(self):
        self.add_polyline('frame',(24,10),(6,10),(6,42),(42,42),(42,26))
        self.circle('sun',16,21,3)
        self.add_polyline('small-mountain',(10,42),(18,29),(25,42))
        self.add_polyline('large-mountain',(22,42),(32,25),(42,42))
        self.add_line('wand',(32,14),(42,24))
        self.add_line('ray-up',(34,6),(34,8))
        self.add_line('ray-right',(40,12),(42,10))
        self.add_line('ray-left',(26,6),(28,8))

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
