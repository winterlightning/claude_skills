'Pet Food Bowl.\nPlan: Pet bowl with rounded lower rim, curved opening and food mound rising above it. Bounds4,10..44,38.\nConstruction reference: No useful exact local Lucide match; geometric arcs and coherent contours preserve the supplied subject.\nReduction: Omit the hidden back rim; use the food mound as the upper silhouette.\nKeyshape: HRECT_M; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6db383b2-bb6d-42b0-9269-1f26cc85e9de'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/pet feeder_6db383b2-bb6d-42b0-9269-1f26cc85e9de.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'pet-food-bowl'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('pet', 'food', 'bowl')

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

        self.add_bezier('food',(8,18),((8,12),(12,10),(16,12)),((18,12),(20,10),(24,10)),((28,10),(30,12),(32,12)),((36,10),(40,12),(40,18)))
        path('body',(40,18),[(44,32),((24,38),20,6,True),((4,32),20,6,True),(8,18)])
        path('rim',(8,18),[((40,18),16,8,False)])
        self.relate('connect','food','body');self.relate('connect','food','rim');self.relate('connect','body','rim')
