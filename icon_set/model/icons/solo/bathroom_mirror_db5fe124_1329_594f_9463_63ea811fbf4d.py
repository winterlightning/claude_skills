"""A rounded rectangular bathroom mirror on a short central pedestal.
Plan: Symmetric mirror outline and pedestal; a single diagonal reflection mark.
Construction reference: rectangle-horizontal: equal-radius corners and tangent straight sides.
"""
from ...keyshapes import Keyshape
from icon_set.model.profiles import Profile
from ._base import Solo48

SOURCE_ICON_ID = 'db5fe124-1329-594f-9463-63ea811fbf4d'
SOURCE_PATH = 'icon_set/work/todo-references/bathroom mirror_db5fe124-1329-594f-9463-63ea811fbf4d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'bathroom-mirror'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('bathroom', 'mirror')
    # Bounds are supplied by the contract; geometry below is authored to them.
    planned_visible_bounds = Keyshape.VRECT_L.bounds_for(Profile.SOLO48)

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
        self.add_line('top',(14,4),(34,4))
        self.add_arc('tr',(34,4),(38,8),radius_x=4)
        self.add_line('right',(38,8),(38,32))
        self.add_arc('br',(38,32),(34,36),radius_x=4)
        self.add_line('bottom-right',(34,36),(24,36))
        self.add_line('bottom-left',(24,36),(14,36))
        self.add_arc('bl',(14,36),(10,32),radius_x=4)
        self.add_line('left',(10,32),(10,8))
        self.add_arc('tl',(10,8),(14,4),radius_x=4)
        self.add_contour('mirror','top','tr','right','br','bottom-right','bottom-left','bl','left','tl',closed=True)
        self.add_line('reflection',(19,24),(27,16))
        self.add_line('stem',(24,36),(24,44))
        self.add_line('foot-left',(8,44),(24,44))
        self.add_line('foot-right',(24,44),(40,44))
        for other in ('bottom-right','bottom-left','foot-left','foot-right'):
            self.relate('connect','stem',other)
