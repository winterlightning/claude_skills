'Anonymous Figure Wearing a Hoodie.\nPlan: Pointed enclosing hood around a blank circular face. Face center24,24 radius6 ends y30; body top34 gives zero ink gap.\nConstruction reference: human_ref/user.svg: circular face and broad curved shoulders; source pointed hood retained.\nReduction: Jacket seam omitted.\nKeyshape: SQUARE; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5788eae1-ef63-448b-b49c-a5c74e0c2260'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_22/hood_5788eae1-ef63-448b-b49c-a5c74e0c2260.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'blank-faced-hooded-bust'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('blank', 'faced', 'hooded', 'bust')

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

        self.add_arc('head-top',(18,24),(30,24),radius_x=6)
        self.add_arc('head-bottom',(30,24),(18,24),radius_x=6)
        self.add_contour('face','head-top','head-bottom',closed=True)
        path('hood',(6,30),[((24,6),30,30,True),((42,30),30,30,True)])
        self.add_arc('body-top',(6,42),(42,42),radius_x=18,radius_y=8)
        self.add_contour('shoulders','body-top')
        self.relate('connect','face','shoulders')
