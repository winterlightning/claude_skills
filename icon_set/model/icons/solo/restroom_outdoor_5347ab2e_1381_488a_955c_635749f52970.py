"""A portable outdoor restroom with a triangular door sign.

Plan: Symmetric domed cabin owns a nested doorway and triangle.
Construction: house: continuous enclosure and open doorway
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5347ab2e-1381-488a-955c-635749f52970'
SOURCE_PATH = 'icon_set/work/todo-references/restroom outdoor_5347ab2e-1381-488a-955c-635749f52970.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'restroom-outdoor'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "wayfinding"
    aliases = ()
    keywords = ('restroom', 'outdoor')

    def build(self):
        self.add_arc('roof-left',(8,12),(16,4),radius_x=8)
        self.add_line('roof-top',(16,4),(32,4))
        self.add_arc('roof-right',(32,4),(40,12),radius_x=8)
        wall_points=[(40,12),(40,44),(32,44),(16,44),(8,44),(8,12)]
        for i in range(5):self.add_line(f'walls-{i+1}',wall_points[i],wall_points[i+1])
        self.add_contour('cabin','roof-left','roof-top','roof-right',*(f'walls-{i}' for i in range(1,6)),closed=True)
        self.add_polyline('door',(16,44),(16,20),(32,20),(32,44))
        self.add_polyline('sign',(20,33),(24,26),(28,33),closed=True)
        self.relate('connect','door-1','walls-3');self.relate('connect','door-1','walls-4')
        self.relate('connect','door-3','walls-2');self.relate('connect','door-3','walls-3')

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
