'Audio Speaker with Sound Waves.\nPlan: Left speaker housing joins widening horn; two separated wave arcs at right.\nConstruction reference: Lucide volume-2: horn polygon and concentric sound arcs.\nReduction: Rear rounding removed to prioritize readable horn and two waves.\nKeyshape: HRECT_M; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd01cc462-7f9a-42c6-8c2a-0631d64fc03d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_21/hake_d01cc462-7f9a-42c6-8c2a-0631d64fc03d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'speaker-with-two-sound-arcs'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('speaker', 'with', 'two', 'sound', 'arcs')

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

        self.add_polyline('speaker',(4,18),(12,18),(24,10),(24,38),(12,30),(4,30),closed=True)
        path('wave-inner',(33,18),[((33,30),2,6,True)])
        path('wave-outer',(38,10),[((38,38),6,14,True)])
