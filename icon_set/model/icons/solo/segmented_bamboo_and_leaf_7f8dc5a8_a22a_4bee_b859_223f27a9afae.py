'Bamboo Stalk with Leaf.\nPlan: Three shared stalk segments; broad attached leaf at lower right.\nConstruction reference: No useful exact local Lucide match; geometric arcs and coherent contours preserve the supplied subject.\nReduction: Leaf vein omitted to protect the broad leaf opening.\nKeyshape: VRECT_L; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7f8dc5a8-a22a-4bee-b859-223f27a9afae'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_22/hide column_7f8dc5a8-a22a-4bee-b859-223f27a9afae.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'segmented-bamboo-and-leaf'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('segmented', 'bamboo', 'and', 'leaf')

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

        self.add_polyline('stalk',(8,4),(20,4),(20,16),(20,28),(20,44),(8,44),(8,28),(8,16),closed=True)
        for y in (16,28):self.add_line(f'joint-{y}',(8,y),(20,y));self.relate('connect','stalk',f'joint-{y}')
        path('leaf',(20,44),[((40,24),20,20,True),((20,44),20,20,True)],True)
        self.relate('connect','leaf','stalk')
