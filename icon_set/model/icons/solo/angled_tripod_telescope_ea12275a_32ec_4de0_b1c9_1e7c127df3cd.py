'Astronomical Telescope on Tripod.\nPlan: Diagonal telescope with a broad objective collar; three legs share a true lower tube node.\nConstruction reference: Lucide telescope: diagonal optical tube, objective band and shared tripod pivot.\nReduction: Narrow eyepiece omitted; objective collar restored for recognition.\nKeyshape: SQUARE; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ea12275a-32ec-4de0-b1c9-1e7c127df3cd'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_37/telescope_ea12275a-32ec-4de0-b1c9-1e7c127df3cd.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'angled-tripod-telescope'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('angled', 'tripod', 'telescope')

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

        self.add_polyline('tube',(6,22),(27,10),(34,6),(42,20),(35,24),(28,28),(14,36),closed=True)
        self.add_line('objective-rim',(27,10),(35,24));self.relate('connect','objective-rim','tube')
        self.add_polyline('tripod',(16,42),(28,28),(40,42));self.relate('connect','tripod','tube')
        self.add_line('middle-leg',(28,28),(28,42));self.relate('connect','middle-leg','tube');self.relate('connect','middle-leg','tripod')
