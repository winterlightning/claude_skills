'Hand Finger Tapping Gesture.\nPlan: Raised index finger and folded fingers over a rounded palm, with an open contact arc.\nConstruction reference: Lucide hand: one palm silhouette, one clearly extended digit.\nReduction: Folded finger creases merged into one knuckle contour.\nKeyshape: VRECT_L; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7cd3d777-8324-4e1a-97bc-54f53f64ab25'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_20/gesture tap 2_7cd3d777-8324-4e1a-97bc-54f53f64ab25.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'tapping-hand-with-contact-arc'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('tapping', 'hand', 'with', 'contact', 'arc')

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

        path('hand',(14,44),[(8,32),((12,26),4,6,True),(14,26),(18,30),(18,18),((26,18),4,4,True),(26,28),(34,28),((40,34),6,6,True),(36,44)])
        path('contact',(10,14),[((34,14),12,10,True)])
