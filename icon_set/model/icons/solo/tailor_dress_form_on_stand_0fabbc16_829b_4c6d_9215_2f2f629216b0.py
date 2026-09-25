'Tailor Mannequin Dress Form.\nPlan: Headless tailor form with neck stump, narrow waist, rounded hips and central stand.\nConstruction reference: No useful exact local Lucide match; geometric arcs and coherent contours preserve the supplied subject.\nReduction: Long central construction seam omitted; waist division retained.\nKeyshape: VRECT_L; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0fabbc16-829b-4c6d-9215-2f2f629216b0'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_18/fashion design 2_0fabbc16-829b-4c6d-9215-2f2f629216b0.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'tailor-dress-form-on-stand'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('tailor', 'dress', 'form', 'on', 'stand')

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

        path('form',(20,4),[(28,4),(28,10),(40,14),((32,26),18,18,False),((40,36),18,18,False),((8,36),16,4,True),((16,26),18,18,False),((8,14),18,18,False),(20,10),(20,4)],True)
        self.add_polyline('waist',(16,26),(24,26),(32,26));self.relate('connect','waist','form')
        self.add_line('stand',(24,40),(24,44));self.relate('connect','stand','form')
