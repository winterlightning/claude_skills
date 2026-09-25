'Air Transportation Helicopter.\nPlan: Rounded left cabin, open tail boom and upturned fin; rotor and skids attached at explicit nodes.\nConstruction reference: Lucide helicopter: rounded cabin and shared attachment nodes.\nReduction: Window removed; thin enclosed tail reduced to a structural tail boom. Actual reference faces left.\nKeyshape: HRECT_L; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2864e350-fc3e-4769-9be9-7c7eb49a587f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_22/helicopter_2864e350-fc3e-4769-9be9-7c7eb49a587f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'side-view-helicopter'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('side', 'view', 'helicopter')

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

        path('body',(4,26),[((16,16),12,10,True),(22,16),((28,22),6,6,True),(28,24),(28,26),((22,32),6,6,True),(16,32),(10,32),((4,26),6,6,True)],True)
        self.add_polyline('tail',(28,24),(44,20),(44,12));self.relate('connect','tail','body')
        self.add_polyline('rotor',(4,8),(16,8),(34,8))
        self.add_line('shaft',(16,8),(16,16));self.relate('connect','shaft','rotor');self.relate('connect','shaft','body')
        self.add_polyline('skid',(6,40),(16,40),(28,40))
        self.add_line('strut',(16,32),(16,40));self.relate('connect','strut','skid');self.relate('connect','strut','body')
