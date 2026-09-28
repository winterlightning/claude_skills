'Two Finger Horizontal Swipe Gesture.\nPlan: Two upright rounded fingertips beneath a broad shallow contact arc.\nConstruction reference: Lucide hand: rounded finger ends; supplied two-finger count and overhead arc retained.\nReduction: Keep the defining silhouette and essential parts.\nKeyshape: HRECT_L; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '461555a7-a057-437a-85da-8c65cab1dabe'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_20/gesture swipe horizontal right two fingers_461555a7-a057-437a-85da-8c65cab1dabe.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'two-fingertips-beneath-contact-arc'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('two', 'fingertips', 'beneath', 'contact', 'arc')

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

        path('contact',(4,14),[((44,14),20,6,True)])
        for x in (12,28):path(f'finger-{x}',(x,40),[(x,27),((x+8,27),4,4,True),(x+8,40)])
