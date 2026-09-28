'Hanging Skulls Trophy.\nPlan: Two overlapping skulls with three visible eyes suspended from a common loop.\nConstruction reference: No useful exact local Lucide match; geometric arcs and coherent contours preserve the supplied subject.\nReduction: Rear right eye is occluded as in the original. Tooth seams omitted; rear lower jaw merged into its visible outline.\nKeyshape: SQUARE; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'dc12832a-b75c-4002-ad7b-827928ab99e4'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_18/fantasy medieval bounty hunter 1_dc12832a-b75c-4002-ad7b-827928ab99e4.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'two-skulls-hanging-from-loop'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('two', 'skulls', 'hanging', 'from', 'loop')

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

        circle('loop',39,9,3)
        self.add_polyline('cord-left',(36,9),(15,9));self.relate('connect','cord-left','loop')
        self.add_line('cord-right',(39,12),(41,29));self.relate('connect','cord-right','loop')
        path('front',(16,34),[((17,29),13,13,True),((24,22),13,13,True),((29,21),13,13,True),((41,29),13,13,True),((42,34),13,13,True),(42,40),(36,40),(36,42),(22,42),(22,40),(16,40),(16,38),(16,34)],True)
        path('rear',(24,22),[(24,18),((15,9),9,9,False),((6,18),9,9,False),(6,30),(8,30),(8,38),(16,38)])
        self.relate('connect','front','rear');self.relate('connect','front','cord-right');self.relate('connect','rear','cord-left')
        self.add_dot('rear-eye',(15,18));self.add_dot('front-eye-left',(25,32));self.add_dot('front-eye-right',(33,32))
