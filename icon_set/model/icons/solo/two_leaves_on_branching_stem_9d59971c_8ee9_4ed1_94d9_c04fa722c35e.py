'Two Small Leaves Vegan Symbol.\nPlan: Two asymmetric pointed leaf contours meet a branching stem; left upright and right spreading. Extrema6..42.\nConstruction reference: Lucide sprout and leaf originals and atomic-debug: pointed paired leaf contours and shared stem endpoints.\nReduction: Keep the defining silhouette and essential parts.\nKeyshape: SQUARE; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9d59971c-8ee9-4ed1-94d9-c04fa722c35e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_19/food allegic vegan meal symbol_9d59971c-8ee9-4ed1-94d9-c04fa722c35e.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'two-leaves-on-branching-stem'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('two', 'leaves', 'on', 'branching', 'stem')

    def build(self):

        def path(name, start, steps, closed=False):
            members, point = [], start
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

        def ellipse(name, x, y, rx, ry):
            path(name, (x-rx,y), [((x+rx,y),rx,ry,True), ((x-rx,y),rx,ry,True)], True)

        def circle(name, x, y, radius):
            ellipse(name,x,y,radius,radius)

        def box(name, left, top, right, bottom, radius=4):
            r = radius
            path(name, (left+r,top), [(right-r,top), ((right,top+r),r,r,True),
                 (right,bottom-r), ((right-r,bottom),r,r,True), (left+r,bottom),
                 ((left,bottom-r),r,r,True), (left,top+r), ((left+r,top),r,r,True)], True)

        path('left-leaf',(6,6),[((18,30),24,30,True),((6,6),14,30,True)],True)
        self.add_bezier('right-leaf',(42,10),((42,24),(38,30),(28,30)),((28,16),(34,10),(42,10)))
        self.add_polyline('stem',(18,30),(20,42),(28,30))
        self.relate('connect','stem','left-leaf');self.relate('connect','stem','right-leaf')
