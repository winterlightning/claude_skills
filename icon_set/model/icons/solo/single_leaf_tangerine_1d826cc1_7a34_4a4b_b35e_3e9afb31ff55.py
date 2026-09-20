'Tangerine with Leaf.\nPlan: Tangerine with rounded fruit, short stem and one broad pointed leaf.\nConstruction reference: Lucide sprout: one broad leaf attached at a stem node.\nReduction: Fruit slightly flattened and leaf enlarged for a clear opening.\nKeyshape: VRECT_L; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1d826cc1-7a34-4a4b-b35e-3e9afb31ff55'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_37/tangerine_1d826cc1-7a34-4a4b-b35e-3e9afb31ff55.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'single-leaf-tangerine'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('single', 'leaf', 'tangerine')

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

        path('fruit',(24,24),[((40,34),16,10,True),((24,44),16,10,True),((8,34),16,10,True),((24,24),16,10,True)],True)
        self.add_polyline('stem',(24,24),(20,16),(16,8));self.relate('connect','stem','fruit')
        path('leaf',(20,16),[((40,4),20,12,True),((20,16),20,12,True)],True);self.relate('connect','leaf','stem')
