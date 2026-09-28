'Three Rating Stars.\nPlan: Three five-point outlined stars with generous central openings.\nConstruction reference: No useful exact local Lucide match; geometric arcs and coherent contours preserve the supplied subject.\nReduction: Star tips shortened slightly to open their centers; all three outlined five-point stars retained.\nKeyshape: SQUARE; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cb80e0b8-7fca-4265-8886-79c66c6d169c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_36/stars_cb80e0b8-7fca-4265-8886-79c66c6d169c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'triangular-three-rating-stars'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('triangular', 'three', 'rating', 'stars')

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

        def star(n,cx,cy,rx):
         self.add_polyline(n,(cx,cy-8),(cx+3,cy-3),(cx+rx,cy-3),(cx+5,cy+2),(cx+5,cy+(6 if n=='top' else 8)),(cx,cy+5),(cx-5,cy+(6 if n=='top' else 8)),(cx-5,cy+2),(cx-rx,cy-3),(cx-3,cy-3),closed=True)
        star('top',24,14,8);star('left',13,34,7);star('right',35,34,7)
