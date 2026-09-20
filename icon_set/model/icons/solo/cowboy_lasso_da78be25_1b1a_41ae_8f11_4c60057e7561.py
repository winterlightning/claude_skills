'Traditional Western Cowboy Lasso.\nPlan: Broad rope loop above a hanging teardrop loop, joined by short rope. Bounds6..42.\nReference: Lucide lasso: coherent oval loop and attached rope; source lower loop retained.\nKeyshape: SQUARE, exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'da78be25-1b1a-41ae-8f11-4c60057e7561'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_24/lasso_da78be25-1b1a-41ae-8f11-4c60057e7561.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'cowboy-lasso'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('cowboy', 'lasso')

    def build(self):
        def path(name, start, steps, closed=False):
            members = []
            point = start
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

        def circle(name, x, y, radius):
            path(name, (x-radius,y), [((x+radius,y),radius,radius,True),
                 ((x-radius,y),radius,radius,True)], True)

        def box(name, left, top, right, bottom, radius):
            r = radius
            path(name, (left+r,top), [(right-r,top), ((right,top+r),r,r,True),
                 (right,bottom-r), ((right-r,bottom),r,r,True), (left+r,bottom),
                 ((left,bottom-r),r,r,True), (left,top+r), ((left+r,top),r,r,True)], True)

        path('upper-loop',(6,14),[((24,6),18,8,True),((42,14),18,8,True),((24,22),18,8,True),((6,14),18,8,True)],True)
        self.add_line('rope',(24,22),(24,32));self.relate('connect','rope','upper-loop')
        path('lower-loop',(24,32),[(30,36),((18,36),6,6,True),(24,32)],True);self.relate('connect','lower-loop','rope')
