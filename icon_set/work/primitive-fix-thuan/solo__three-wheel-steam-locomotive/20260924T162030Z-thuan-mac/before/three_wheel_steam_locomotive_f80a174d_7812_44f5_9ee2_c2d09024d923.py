'Vintage Steam Locomotive.\nPlan: Rear cab and boiler above one large rear wheel and two small front wheels. Exact4,8..44,40.\nConstruction reference: Lucide train-front rounded wheels and clear divisions; source side-view layout.\nReduction: Omit wheel hub, chimney flare and cowcatcher teeth; retain all three wheels.\nKeyshape: HRECT_L; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f80a174d-7812-44f5-9ee2-c2d09024d923'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_36/steam engine_f80a174d-7812-44f5-9ee2-c2d09024d923.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-wheel-steam-locomotive'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('three', 'wheel', 'steam', 'locomotive')

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

        self.add_polyline('cab',(4,34),(4,8),(16,8),(16,34))
        self.add_polyline('boiler',(16,16),(40,16),(40,25),(16,25));self.relate('connect','cab','boiler')
        self.add_polyline('chimney',(27,16),(27,8),(37,8),(37,16));self.relate('connect','chimney','boiler')
        circle('rear-wheel',10,34,6)
        for x in (28,42):circle(f'wheel-{x}',x,38,2)
        self.add_line('front',(40,25),(44,25));self.relate('connect','front','boiler')

        self.relate('connect','rear-wheel','cab')
