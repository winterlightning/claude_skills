'Three People Team Symbol.\nPlan: Three abstract arches: taller raised center, two shorter lower side forms.\nConstruction reference: No useful exact local Lucide match; geometric arcs and coherent contours preserve the supplied subject.\nReduction: Only the visible arches are drawn; no human anatomy inferred from the catalog.\nKeyshape: HRECT_L; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3d26f7e7-ad61-40c0-a373-0dccd4de8251'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_20/gamasutra 1_3d26f7e7-ad61-40c0-a373-0dccd4de8251.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-arched-silhouettes'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'users'
    categories = ('users', 'primitive', 'primitives')
    aliases = ()
    keywords = ('three', 'arched', 'silhouettes')

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

        for j,(x,y,w,ry,bottom) in enumerate(((4,28,8,4,40),(20,14,8,6,28),(36,28,8,4,40))):
         path(f'arch-{j}',(x,y),[((x+w,y),w//2,ry,True),(x+w,bottom),(x,bottom),(x,y)],True)
