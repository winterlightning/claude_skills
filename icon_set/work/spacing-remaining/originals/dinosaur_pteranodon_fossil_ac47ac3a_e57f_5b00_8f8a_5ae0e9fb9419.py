'Fossil tablet: a clear fossil silhouette inside a smooth balanced stone frame.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ac47ac3a-e57f-5b00-8f8a-5ae0e9fb9419'
SOURCE_PATH = 'pictographic-primitives/animals/dinosaur pteranodon fossil_ac47ac3a-e57f-5b00-8f8a-5ae0e9fb9419.svg'
AUTHOR = 'gpt-6'


class FossilTablet(Solo48):
    icon_id = 'fossil-tablet'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('fossil', 'dinosaur', 'skeleton', 'pterosaur', 'stone', 'tablet', 'archaeology', 'prehistoric')

    def build(self):
        # Fossil tablet: a clear fossil silhouette inside a smooth balanced stone frame.
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

        r('tablet',6,6,42,42,4)
        p('fossil',(15,31),(15,23),(30,18),(33,29))
        p('spine',(26,15),(23,22),(29,30),(26,33))
        link('connect','spine','fossil')
