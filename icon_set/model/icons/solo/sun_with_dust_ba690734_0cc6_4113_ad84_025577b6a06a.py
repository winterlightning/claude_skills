'Sun with Dust Particles.\nPlan: Sun with seven rays and four separated dust particles below.\nConstruction reference: Lucide sun: radial strokes around a circular center.\nReduction: All seven rays and four dust particles retained; top ray shortened to a dot.\nKeyshape: SQUARE; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ba690734-0cc6-4113-ad84-025577b6a06a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_36/sun dust_ba690734-0cc6-4113-ad84-025577b6a06a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'sun-with-dust'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('sun', 'with', 'dust')

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

        circle('sun',24,20,6)
        self.add_dot('ray-top',(24,6))
        for j,(a,b) in enumerate([((6,20),(8,20)),((40,20),(42,20)),((8,6),(11,9)),((40,6),(37,9)),((6,32),(9,29)),((42,32),(39,29))]):self.add_line(f'ray-{j}',a,b)
        for j,p in enumerate(((14,38),(24,34),(34,38),(24,42))):self.add_dot(f'dust-{j}',p)
