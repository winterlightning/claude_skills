'Tall Skyscraper Building.\nPlan: Slender pointed tower with upper shaft band, spire and broad baseline.\nConstruction reference: Lucide building: structural outline and simple internal division.\nReduction: No monument identity invented.\nKeyshape: VRECT_L; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5941e74d-42b8-4621-9a9a-4940df608b50'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_24/landmark_5941e74d-42b8-4621-9a9a-4940df608b50.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'pointed-landmark-tower'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('pointed', 'landmark', 'tower')

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

        self.add_polyline('tower',(16,44),(16,18),(24,10),(32,18),(32,44))
        self.add_line('spire',(24,4),(24,10));self.relate('connect','spire','tower')
        self.add_line('division',(16,26),(32,26));self.relate('connect','division','tower')
        self.add_polyline('base',(8,44),(16,44),(32,44),(40,44));self.relate('connect','base','tower')
