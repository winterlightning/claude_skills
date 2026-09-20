'Wired Computer Mouse with USB.\nPlan: Upright mouse with upper cable looping left to a large horizontal USB connector above. Bounds6..42.\nConstruction reference: Lucide mouse original/atomic-debug rounded body; source cabled USB mouse arrangement.\nReduction: Reposition USB plug to the left for clear separation; omit tiny contacts and reduce enclosing cable loop.\nKeyshape: SQUARE; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'edeebc99-5db6-408a-828d-f317f5d07c5b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_24/keyboard usb_edeebc99-5db6-408a-828d-f317f5d07c5b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'wired-usb-mouse'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('wired', 'usb', 'mouse')

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

        box('mouse',22,18,42,42,10)
        self.add_line('wheel',(32,27),(32,31))
        path('cable',(32,18),[(32,14),((22,6),10,8,False),(14,6),((6,14),8,8,False),(6,26)])
        self.relate('connect','mouse','cable')
        box('plug',6,26,14,42,2);self.relate('connect','plug','cable')
