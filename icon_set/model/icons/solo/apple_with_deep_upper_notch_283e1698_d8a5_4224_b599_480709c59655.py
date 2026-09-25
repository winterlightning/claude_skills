'Apple with Stem and Leaf.\nPlan: Upright apple centered x24, deep notch, four cardinal exterior arcs and a short stem.\nConstruction reference: Lucide apple: smooth mirrored shoulders and bottom indent.\nReduction: Leaf omitted after its attachment trapped an undersized hole; apple and stem retained.\nKeyshape: VRECT_L; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '283e1698-d8a5-4224-b599-480709c59655'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_20/fruit_283e1698-d8a5-4224-b599-480709c59655.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'apple-with-deep-upper-notch'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('apple', 'with', 'deep', 'upper', 'notch')

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

        path('fruit',(24,20),[((16,16),8,4,False),((8,24),8,8,False),((16,44),8,20,False),((24,42),8,2,False),((32,44),8,2,False),((40,24),8,20,False),((32,16),8,8,False),((24,20),8,4,False)],True)
        self.add_line('stem',(24,20),(24,4));self.relate('connect','stem','fruit')
