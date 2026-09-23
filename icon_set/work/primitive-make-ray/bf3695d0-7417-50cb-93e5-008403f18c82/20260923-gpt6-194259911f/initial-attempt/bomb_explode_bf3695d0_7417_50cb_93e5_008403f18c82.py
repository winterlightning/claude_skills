"""A round fused bomb with an explosion burst over its lower-right side.
Plan: Asymmetric composition: open bomb silhouette, attached two-arc fuse, and one angular burst outline.
Construction reference: bomb: round shell and short fuse neck; retain the supplied foreground explosion.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'bf3695d0-7417-50cb-93e5-008403f18c82'
SOURCE_PATH = 'icon_set/work/todo-references/bomb explode_bf3695d0-7417-50cb-93e5-008403f18c82.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'bomb-explode'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('bomb', 'explode')
    # Bounds are supplied by the contract; geometry below is authored to them.
    planned_visible_bounds = Keyshape.SQUARE.bounds_for(Profile.SOLO48)

    def circle(self, name, cx, cy, rx, ry=None):
        ry = rx if ry is None else ry
        self.add_arc(name+'-top', (cx-rx,cy), (cx+rx,cy), radius_x=rx, radius_y=ry)
        self.add_arc(name+'-bottom', (cx+rx,cy), (cx-rx,cy), radius_x=rx, radius_y=ry)
        self.add_contour(name, name+'-top', name+'-bottom', closed=True)

    def box(self, name, left, top, right, bottom, radius=4):
        r = radius
        points = [(left+r,top),(right-r,top),(right,top+r),(right,bottom-r),
                  (right-r,bottom),(left+r,bottom),(left,bottom-r),(left,top+r)]
        members = []
        for i, start in enumerate(points):
            end = points[(i+1)%8]
            part = f'{name}-{i}'
            if i%2:
                self.add_arc(part,start,end,radius_x=r)
            else:
                self.add_line(part,start,end)
            members.append(part)
        self.add_contour(name,*members,closed=True)

    def build(self):
        self.add_arc('shell-left',(18,42),(18,16),radius_x=12,radius_y=13)
        self.add_polyline('neck',(18,16),(18,10),(22,10),(26,10),(26,18))
        self.add_arc('shell-right',(26,18),(34,28),radius_x=12)
        self.add_contour('shell','shell-left','neck-1','neck-2','neck-3','neck-4','shell-right')
        self.add_arc('fuse-rise',(22,10),(30,6),radius_x=8,radius_y=4)
        self.add_arc('fuse-fall',(30,6),(42,10),radius_x=12,radius_y=4)
        self.add_contour('fuse','fuse-rise','fuse-fall')
        for member in ('neck-2','neck-3'):
            self.relate('connect','fuse-rise',member)
        self.add_polyline('burst',(30,24),(33,30),(42,26),(37,34),(42,38),(34,38),(32,42),(28,36),(22,40),(25,32),(22,28),(29,29),closed=True)
