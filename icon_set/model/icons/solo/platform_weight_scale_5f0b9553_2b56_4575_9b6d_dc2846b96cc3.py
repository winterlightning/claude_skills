'Platform Weight Scale with Dial.\nPlan: Platform scale with tall right post, round dial and short angled needle. Bounds6..42.\nConstruction reference: Lucide scale original/atomic-debug clear central support and measured object; supplied round-dial platform arrangement.\nReduction: Keep the defining silhouette and essential parts.\nKeyshape: SQUARE; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5f0b9553-2b56-4575-9b6d-dc2846b96cc3'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/scale 2_5f0b9553-2b56-4575-9b6d-dc2846b96cc3.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'platform-weight-scale'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('other', 'primitives-generate')
    aliases = ()
    keywords = ('platform', 'weight', 'scale')

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

        circle('dial',31,17,11)
        self.add_line('post',(31,28),(31,42));self.relate('connect','post','dial')
        self.add_line('platform',(6,42),(31,42));self.relate('connect','platform','post')
        self.add_line('needle',(30,18),(33,15))
