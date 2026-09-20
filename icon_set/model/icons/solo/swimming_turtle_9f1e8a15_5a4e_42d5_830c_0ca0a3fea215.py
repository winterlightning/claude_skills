'Swimming Sea Turtle.\nPlan: Domed left-facing turtle with round head and two flowing flipper strokes.\nConstruction reference: Lucide turtle: dome with attached head and limbs.\nReduction: Flippers are open strokes; shell panel detail omitted.\nKeyshape: HRECT_L; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9f1e8a15-5a4e-42d5-830c-0ca0a3fea215'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_39/turtle 1_9f1e8a15-5a4e-42d5-830c-0ca0a3fea215.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'swimming-turtle'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('swimming', 'turtle')

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

        path('shell',(14,24),[((29,8),15,16,True),((44,24),15,16,True),(36,24),(22,24),(14,24)],True)
        path('head',(14,24),[(8,24),((4,20),4,4,True),((8,16),4,4,True),(14,16),(14,24)],True);self.relate('connect','head','shell')
        path('front-flipper',(22,24),[((28,40),8,16,False)]);self.relate('connect','front-flipper','shell')
        path('rear-flipper',(36,24),[((44,34),10,10,False)]);self.relate('connect','rear-flipper','shell')
