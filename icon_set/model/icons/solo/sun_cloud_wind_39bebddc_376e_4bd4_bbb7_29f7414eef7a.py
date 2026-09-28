'Sun Cloud and Wind Weather.\nPlan: Sun behind a rounded cloud with three horizontal wind strokes.\nConstruction reference: Lucide cloud-sun and wind: exposed solar disc and horizontal wind strokes.\nReduction: Tiny sun rays omitted; three wind strokes retained.\nKeyshape: SQUARE; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '39bebddc-376e-4bd4-bbb7-29f7414eef7a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_40/weather cloud sun wind_39bebddc-376e-4bd4-bbb7-29f7414eef7a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'sun-cloud-wind'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('sun', 'cloud', 'wind')

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

        path('outline',(12,18),[((6,12),6,6,True),((12,6),6,6,True),((18,12),6,6,True),((30,12),6,4,True),((42,18),12,6,True),((36,23),6,5,True),(18,23),((12,18),6,5,True)],True)
        path('sun-seam',(18,12),[((12,18),6,6,True)]);self.relate('connect','sun-seam','outline')

        self.add_line('wind-middle',(6,33),(28,33));self.add_line('wind-bottom',(10,42),(22,42))
