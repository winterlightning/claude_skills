"""A 4M height restriction mark between opposing chevrons.
Plan: SQUARE retains the text and top/bottom direction marks.
Reduction: Shortened the glyph height and four crossbar; reduced chevron size. No character or arrow omitted.
Construction: Lucide expand: opposing chevrons; source supplies the 4M lettering.
Layout: Chevrons mirror around y24. Letterforms are naturally asymmetric and use actual stroke junctions."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '51d07cc0-5d3e-489d-b18a-12bf56b9cf6a'
SOURCE_PATH = 'pictographic-primitives/transportation/road sign 4m high_51d07cc0-5d3e-489d-b18a-12bf56b9cf6a.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'road-sign-4m-high'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transportation"
    categories = ("transportation", "primitives")
    aliases = ()
    keywords = ('road', 'sign', '4m', 'high')

    def build(self):
        self.add_polyline('four-left',(14,17),(6,27),(16,27),(18,27))
        self.add_polyline('four-stem',(16,17),(16,27),(16,31))
        self.relate('connect','four-left','four-stem')
        self.add_polyline('m',(28,31),(28,17),(35,26),(42,17),(42,31))
        self.add_polyline('up',(21,9),(24,6),(27,9))
        self.add_polyline('down',(21,39),(24,42),(27,39))


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
