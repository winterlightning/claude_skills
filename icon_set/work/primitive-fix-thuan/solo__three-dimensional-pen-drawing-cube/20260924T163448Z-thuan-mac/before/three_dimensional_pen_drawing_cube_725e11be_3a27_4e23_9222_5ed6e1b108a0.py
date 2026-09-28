'3D Pen Drawing Cube.\nPlan: Open cube shares its upper-right drawing point with the diagonal pen nib. Three-dimensional tool deliberately touches the object being drawn.\nConstruction reference: Lucide box and guitar: shared cube vertices and diagonal tool silhouette.\nReduction: Trailing cord omitted.\nKeyshape: SQUARE; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '725e11be-3a27-4e23-9222-5ed6e1b108a0'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_01/3 d pen box_725e11be-3a27-4e23-9222-5ed6e1b108a0.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-dimensional-pen-drawing-cube'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('three', 'dimensional', 'pen', 'drawing', 'cube')

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

        self.add_polyline('cube',(6,26),(18,20),(30,26),(30,36),(18,42),(6,36),closed=True)
        self.add_polyline('faces',(6,26),(18,32),(30,26));self.relate('connect','faces','cube')
        self.add_line('front',(18,32),(18,42));self.relate('connect','front','cube');self.relate('connect','front','faces')
        path('pen',(30,26),[(28,18),(36,6),((42,12),6,6,True),(38,20),(30,26)],True)
        self.relate('connect','pen','cube');self.relate('connect','pen','faces')
