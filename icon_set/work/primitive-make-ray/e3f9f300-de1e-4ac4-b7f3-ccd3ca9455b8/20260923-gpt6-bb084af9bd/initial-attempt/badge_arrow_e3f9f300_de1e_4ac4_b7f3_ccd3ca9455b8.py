"""A blank upright badge with a peaked arrow-like top.
Plan: One symmetric peaked enclosure; paired lower quarter-circle corners with radius 4.
Construction reference: rectangle-horizontal: tangent quarter-circle transitions at the lower corners.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'e3f9f300-de1e-4ac4-b7f3-ccd3ca9455b8'
SOURCE_PATH = 'icon_set/work/todo-references/badge arrow_e3f9f300-de1e-4ac4-b7f3-ccd3ca9455b8.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'badge-arrow'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('badge', 'arrow')
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
        axis=24
        self.add_polyline('peak',(8,40),(8,18),(axis,4),(40,18),(40,40))
        self.add_arc('lower-right',(40,40),(36,44),radius_x=4)
        self.add_line('bottom',(36,44),(12,44))
        self.add_arc('lower-left',(12,44),(8,40),radius_x=4)
        self.add_contour('outline','peak-1','peak-2','peak-3','peak-4','lower-right','bottom','lower-left',closed=True)
