'Toilet Paper Roll.\nPlan: Paper roll with rounded cut end, core hole and a hanging right sheet.\nConstruction reference: No useful exact local Lucide match; geometric arcs and coherent contours preserve the supplied subject.\nReduction: Oval cut end uses a straight rear seam to leave a clear opening and hanging sheet.\nKeyshape: SQUARE; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ada39c49-073a-4e0e-bbcd-c258c5d26b9d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_38/toilet paper_ada39c49-073a-4e0e-bbcd-c258c5d26b9d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'toilet-paper-roll'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('toilet', 'paper', 'roll')

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

        path('end',(17,6),[(28,6),(28,34),(17,34),((17,6),11,14,True)],True)
        circle('hole',17,20,2)
        path('sheet',(28,6),[(30,6),((42,18),12,12,True),(42,42),(28,42),(28,34)]);self.relate('connect','sheet','end')
