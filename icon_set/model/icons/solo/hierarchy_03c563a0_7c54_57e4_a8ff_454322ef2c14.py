'Hierarchy: equal child boxes, a centered parent and evenly spaced connecting branches.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '03c563a0-7c54-57e4-a8ff-454322ef2c14'
SOURCE_PATH = 'pictographic-primitives/programing/hierarchy_03c563a0-7c54-57e4-a8ff-454322ef2c14.svg'
AUTHOR = 'gpt-6'

class Hierarchy(Solo48):
    icon_id = 'hierarchy'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'programing'
    aliases = ()
    keywords = ('hierarchy', 'programing')

    def build(self):
        # Hierarchy: equal child boxes, a centered parent and evenly spaced connecting branches.
        l = self.add_line
        p = self.add_polyline
        link = self.relate

        def a(name, start, end, rx, ry=None, sweep=True):
            self.add_arc(name, start, end, radius_x=rx,
                         radius_y=rx if ry is None else ry, sweep=sweep)

        def r(name, x0, y0, x1, y1, radius=4):
            # Equal corner radii and shared tangent endpoints own the rounded box.
            points = [(x0+radius,y0),(x1-radius,y0),(x1,y0+radius),
                      (x1,y1-radius),(x1-radius,y1),(x0+radius,y1),
                      (x0,y1-radius),(x0,y0+radius)]
            ids=[]
            for index,start in enumerate(points):
                end=points[(index+1)%8]
                if start==end:
                    continue
                part=f'{name}-{index}'
                if index%2:
                    a(part,start,end,radius)
                else:
                    l(part,start,end)
                ids.append(part)
            self.add_contour(name,*ids,closed=True)

        r('parent',16,6,32,16,3)
        r('left',6,32,20,42,3)
        r('right',28,32,42,42,3)
        p('branches',(13,32),(13,24),(35,24),(35,32))
        l('stem',(24,16),(24,24))
        link('connect','stem','parent')
        link('connect','stem','branches')
        link('connect','branches','left')
        link('connect','branches','right')
