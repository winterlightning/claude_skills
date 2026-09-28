"""The binary digits 010 above 001 in two aligned rows.
Plan: Two rows at y14 and y34; column centers 8,24,40; every zero uses the same ellipse.
Construction reference: No useful Lucide match for this exact six-glyph arrangement; shared ellipse geometry and regular spacing.
"""
from ...keyshapes import Keyshape
from icon_set.model.profiles import Profile
from ._base import Solo48

SOURCE_ICON_ID = 'abff6337-b854-552e-afe3-b89605887cad'
SOURCE_PATH = 'icon_set/work/todo-references/binary_abff6337-b854-552e-afe3-b89605887cad.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'binary'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "programing"
    categories = ("programing", "primitives")
    aliases = ()
    keywords = ('binary',)
    # Bounds are supplied by the contract; geometry below is authored to them.
    planned_visible_bounds = Keyshape.HRECT_L.bounds_for(Profile.SOLO48)

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
        columns=[8,24,40]
        for row, digits in enumerate(('010','001')):
            cy=14+row*20
            for col,digit in enumerate(digits):
                cx=columns[col]
                name=f'digit-{row}-{col}'
                if digit=='0':
                    self.circle(name,cx,cy,4,6)
                else:
                    self.add_line(name,(cx,cy-6),(cx,cy+6))
