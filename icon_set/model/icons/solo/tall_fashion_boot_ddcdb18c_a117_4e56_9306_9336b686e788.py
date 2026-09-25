'Tall Women Fashion Boot.\nPlan: Tall right-facing fashion boot with narrow ankle, rounded toe and block heel.\nConstruction reference: No useful exact local Lucide match; geometric arcs and coherent contours preserve the supplied subject.\nReduction: Retain heel and sloping sole; stitching omitted.\nKeyshape: VRECT_L; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ddcdb18c-a117-4e56-9306-9336b686e788'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_19/footwear boots female_ddcdb18c-a117-4e56-9306-9336b686e788.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'tall-fashion-boot'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('tall', 'fashion', 'boot')

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

        path('boot',(10,4),[(28,4),(26,26),((34,34),8,8,False),((40,40),6,6,True),((34,44),6,4,True),(22,40),(18,44),(10,44),(10,34),(8,34),(10,4)],True)
