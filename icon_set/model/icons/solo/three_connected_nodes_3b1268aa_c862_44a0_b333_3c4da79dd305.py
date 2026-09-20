'Three Connected Circles Symbol.\nPlan: Three round network nodes connect at one central junction.\nConstruction reference: Lucide network: linked nodes and a shared branch point.\nReduction: All three nodes retained.\nKeyshape: SQUARE; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3b1268aa-c862-44a0-b333-3c4da79dd305'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_39/vanadyl_3b1268aa-c862-44a0-b333-3c4da79dd305.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-connected-nodes'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('three', 'connected', 'nodes')

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

        circle('left',11,24,5);circle('top',37,11,5);circle('bottom',37,37,5)
        self.add_polyline('branches',(16,24),(24,24),(34,15));self.relate('connect','branches','left');self.relate('connect','branches','top')
        self.add_line('bottom-link',(24,24),(34,33));self.relate('connect','bottom-link','branches');self.relate('connect','bottom-link','bottom')
