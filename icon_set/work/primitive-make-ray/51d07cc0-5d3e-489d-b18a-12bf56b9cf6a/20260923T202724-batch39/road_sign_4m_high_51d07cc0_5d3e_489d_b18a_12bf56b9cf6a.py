"""A four-metre height restriction mark with vertical chevrons.

Plan: Hand-authored 4 and M retain the text; mirrored top/bottom chevrons mark height.
Construction: expand: paired directional chevrons
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '51d07cc0-5d3e-489d-b18a-12bf56b9cf6a'
SOURCE_PATH = 'icon_set/work/todo-references/road sign 4m high_51d07cc0-5d3e-489d-b18a-12bf56b9cf6a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'road-sign-4m-high'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('road', 'sign', '4m', 'high')

    def build(self):
        self.add_polyline('four',(6,28),(18,14),(18,28),(18,34))
        self.add_polyline('four-bar',(6,28),(18,28),(22,28))
        for a in ('four-2','four-3'):
            for b in ('four-bar-1','four-bar-2'):self.relate('connect',a,b)
        self.relate('connect','four-1','four-bar-1')
        self.add_polyline('m',(28,34),(28,14),(35,26),(42,14),(42,34))
        self.add_polyline('up',(20,10),(24,6),(28,10))
        self.add_polyline('down',(20,38),(24,42),(28,38))

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
