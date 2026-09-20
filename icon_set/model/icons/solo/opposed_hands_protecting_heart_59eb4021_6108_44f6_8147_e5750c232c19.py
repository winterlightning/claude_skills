'Hands Protecting a Heart.\nPlan: Two diagonally opposed hands cup a heart between them, following the reference asymmetry.\nConstruction reference: Lucide hand-heart: round finger ends; opposed hands keep their intentional diagonal placement.\nReduction: Fine palm creases removed.\nKeyshape: SQUARE; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '59eb4021-6108-44f6-8147-e5750c232c19'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_37/support 2_59eb4021-6108-44f6-8147-e5750c232c19.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'opposed-hands-protecting-heart'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('opposed', 'hands', 'protecting', 'heart')

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

        path('upper-hand',(42,6),[(32,6),((32,14),4,4,False),(36,14),(42,22)])
        path('lower-hand',(6,32),[(14,42),(26,42),((26,34),4,4,False),(22,34)])
        path('heart',(14,20),[((6,20),4,4,False),(14,28),(22,20),((14,20),4,4,False)],True)
