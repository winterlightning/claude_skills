"""A padlock containing a receding road.

Plan: Symmetric lock body and arched shackle contain a trapezoidal road.
Construction: lock: arched shackle above rounded body
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'ea945a43-10ca-4ee5-a157-515c7b4149fa'
SOURCE_PATH = 'icon_set/work/todo-references/road lock_ea945a43-10ca-4ee5-a157-515c7b4149fa.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'road-lock'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('road', 'lock')

    def build(self):
        self.box('body',8,24,40,44,3)
        self.add_line('shackle-left',(14,24),(14,14))
        self.add_arc('shackle-top',(14,14),(34,14),radius_x=10)
        self.add_line('shackle-right',(34,14),(34,24))
        self.add_contour('shackle','shackle-left','shackle-top','shackle-right')
        self.relate('connect','shackle-left','body-0');self.relate('connect','shackle-right','body-0')
        self.add_polyline('road',(14,44),(20,32),(28,32),(34,44))
        self.relate('connect','road-1','body-4');self.relate('connect','road-3','body-4')
        self.add_line('road-dash',(24,38),(24,40))

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
