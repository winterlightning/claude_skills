"""A suitcase on a baseline beneath a floating weighing dial.
Plan: Symmetric dial and case around x24; the needle is deliberately diagonal; handle joins the case roof.
Construction reference: search: a round dial; rectangle-horizontal: rounded case corners.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'ee2a071e-6904-4d7d-a879-a7315aec3bd6'
SOURCE_PATH = 'icon_set/work/todo-references/baggage weight_ee2a071e-6904-4d7d-a879-a7315aec3bd6.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'baggage-weight'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('baggage', 'weight')
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
        self.circle('dial',24,14,8)
        self.add_line('needle',(24,14),(27,11))
        self.add_polyline('handle',(20,32),(20,26),(28,26),(28,32))
        self.add_line('roof-left',(16,32),(20,32))
        self.add_line('roof-middle',(20,32),(28,32))
        self.add_line('roof-right',(28,32),(32,32))
        self.add_arc('case-top-right',(32,32),(36,36),radius_x=4)
        self.add_line('case-right',(36,36),(36,38))
        self.add_arc('case-bottom-right',(36,38),(32,42),radius_x=4)
        self.add_line('case-bottom',(32,42),(16,42))
        self.add_arc('case-bottom-left',(16,42),(12,38),radius_x=4)
        self.add_line('case-left',(12,38),(12,36))
        self.add_arc('case-top-left',(12,36),(16,32),radius_x=4)
        self.add_contour('case','roof-left','roof-middle','roof-right','case-top-right','case-right','case-bottom-right','case-bottom','case-bottom-left','case-left','case-top-left',closed=True)
        for a,b in [('handle-1','roof-left'),('handle-1','roof-middle'),('handle-3','roof-middle'),('handle-3','roof-right')]:
            self.relate('connect',a,b)
        self.add_line('stripe',(21,37),(27,37))
        self.add_line('ground-left',(6,42),(16,42))
        self.add_line('ground-right',(32,42),(42,42))
        for a in ('case-bottom','case-bottom-left'):
            self.relate('connect','ground-left',a)
        for a in ('case-bottom','case-bottom-right'):
            self.relate('connect','ground-right',a)
