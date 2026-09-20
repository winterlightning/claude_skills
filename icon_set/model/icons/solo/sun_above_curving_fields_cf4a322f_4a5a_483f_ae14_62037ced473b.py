'Sun rising over agricultural fields.\nPlan: A sun on the horizon overlooks two broad sweeping field bands.\nConstruction reference: Lucide sunrise: half-disc meeting a level horizon.\nReduction: Small background hill stripes and cropping baseline omitted; curving cultivated field bands retained.\nKeyshape: SQUARE; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cf4a322f-4a5a-483f-ae14-62037ced473b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_18/farmland_cf4a322f-4a5a-483f-ae14-62037ced473b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'sun-above-curving-fields'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('sun', 'above', 'curving', 'fields')

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

        path('sun',(14,16),[((34,16),10,10,True)])
        self.add_polyline('horizon',(6,16),(14,16),(34,16),(42,16));self.relate('connect','sun','horizon')
        path('field-upper',(6,42),[((42,26),36,16,True)])
        path('field-lower',(18,42),[((42,36),24,6,True)])
