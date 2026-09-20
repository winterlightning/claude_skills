'Worried Face With Sweat Drop.\nPlan: Open circular face around a large sweat drop with one visible eye and round open mouth. Bounds6..42.\nConstruction reference: No useful exact local Lucide match; geometric arcs and coherent contours preserve the supplied subject.\nReduction: Open the face contour behind the sweat drop; omit brows and covered eye, reduce wide open mouth to round opening.\nKeyshape: SQUARE; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e7345811-ff31-4d0a-b09b-edeaa642a06e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_18/face tongue sweat_e7345811-ff31-4d0a-b09b-edeaa642a06e.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'sweating-face-with-open-mouth'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('sweating', 'face', 'with', 'open', 'mouth')

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

        path('face',(24,6),[((6,24),18,18,False),((24,42),18,18,False)])
        self.add_bezier('cheek',(24,42),((32,42),(38,36),(38,32)));self.relate('connect','face','cheek')
        path('sweat',(36,6),[(42,18),((30,18),6,6,True),(36,6)],True)
        self.add_dot('eye',(17,18));circle('mouth',23,30,3)
