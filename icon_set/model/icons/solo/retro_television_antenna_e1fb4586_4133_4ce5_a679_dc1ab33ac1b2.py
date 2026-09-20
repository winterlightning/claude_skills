'Retro Television.\nPlan: Rounded cabinet with inset screen and V aerial; shared aerial junction24,16. Bounds6..42; omit small feet.\nReference: Lucide tv: rounded screen silhouette with connected V antenna.\nKeyshape: SQUARE; constructed to exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e1fb4586-4133-4ce5-a679-dc1ab33ac1b2'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_37/telescreen_e1fb4586-4133-4ce5-a679-dc1ab33ac1b2.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'retro-television-antenna'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('retro', 'television', 'antenna')

    def build(self):
        def path(name, start, steps, closed=False):
            members = []
            point = start
            for index, step in enumerate(steps):
                member = f"{name}-{index}"
                if len(step) == 2:
                    self.add_line(member, point, step)
                    point = step
                else:
                    end, rx, ry, sweep = step
                    self.add_arc(member, point, end, radius_x=rx, radius_y=ry, sweep=sweep)
                    point = end
                members.append(member)
            self.add_contour(name, *members, closed=closed)

        def circle(name, x, y, radius):
            path(name, (x-radius,y), [((x+radius,y),radius,radius,True),
                 ((x-radius,y),radius,radius,True)], True)

        def box(name, left, top, right, bottom, radius):
            r = radius
            path(name, (left+r,top), [(right-r,top), ((right,top+r),r,r,True),
                 (right,bottom-r), ((right-r,bottom),r,r,True), (left+r,bottom),
                 ((left,bottom-r),r,r,True), (left,top+r), ((left+r,top),r,r,True)], True)

        path('cabinet',(10,16),[(24,16),(38,16),((42,20),4,4,True),(42,38),((38,42),4,4,True),(10,42),((6,38),4,4,True),(6,20),((10,16),4,4,True)],True)
        self.add_polyline('antenna',(14,6),(24,16),(34,6));self.relate('connect','cabinet','antenna')
        box('screen',15,25,33,33,3)
