'Traditional Mexican Style Taco.\nPlan: Wide semicircular taco shell with a low rounded filling crest behind its upper rim.\nConstruction reference: No useful exact local Lucide match; geometric arcs and coherent contours preserve the supplied subject.\nReduction: Small irregular filling bumps consolidated into one low broad crest; shell remains full-width.\nKeyshape: HRECT_L; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'add330ed-f5b1-4bc0-b2c1-655024b39398'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_37/taco_add330ed-f5b1-4bc0-b2c1-655024b39398.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'filled-taco'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('filled', 'taco')

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

        path('shell',(4,38),[((12,22),20,20,True),((24,18),20,20,True),((36,22),20,20,True),((44,38),20,20,True),(44,40),(4,40),(4,38)],True)
        path('filling',(12,22),[(12,16),((20,8),8,8,True),(28,8),((36,16),8,8,True),(36,22)]);self.relate('connect','filling','shell')

# Batch-016: unresolved native-size meaning review; see the batch results log.
