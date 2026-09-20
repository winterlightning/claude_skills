'Winking Face with Tongue.\nPlan: Winking tongue-out face with rounded tongue, small left wink and right eye.\nConstruction reference: No useful exact local Lucide match; geometric arcs and coherent contours preserve the supplied subject.\nReduction: Reduce hollow eye to a dot and flatten mouth, preserving wink and rounded projecting tongue.\nKeyshape: CIRCLE; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'adcd6a14-942c-4a8f-b3bd-aca71c218d67'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_17/face grin tongue wink_adcd6a14-942c-4a8f-b3bd-aca71c218d67.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'winking-face-with-rounded-tongue'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('winking', 'face', 'with', 'rounded', 'tongue')

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

        circle('face',24,24,20)
        path('wink',(15,17),[((19,17),2,1,True)])
        self.add_dot('eye',(31,17))
        self.add_line('mouth',(16,26),(32,26))
        path('tongue',(20,26),[(20,31),((28,31),4,4,False),(28,26)]);self.relate('connect','tongue','mouth')
