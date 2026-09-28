'Sydney Opera House Landmark.\nPlan: Three overlapping sail shells rise from a low podium; tallest central shell and low right shell.\nConstruction reference: No useful exact local Lucide match; geometric arcs and coherent contours preserve the supplied subject.\nReduction: Smallest rear shell omitted; three main sails preserve the landmark.\nKeyshape: HRECT_L; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c7364773-fda3-4a38-a60d-6690249945af'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_37/sydney opera house 1_c7364773-fda3-4a38-a60d-6690249945af.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'sydney-opera-house-shells'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('sydney', 'opera', 'house', 'shells')

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

        self.add_polyline('podium',(4,32),(14,32),(26,32),(40,32),(44,32),(44,40),(4,40),closed=True)
        path('left-shell',(14,32),[(8,18),((26,32),22,18,True)]);self.relate('connect','left-shell','podium')
        path('middle-shell',(26,32),[(20,8),((34,24),14,16,True)]);self.relate('connect','middle-shell','podium')
        path('right-shell',(26,32),[((34,24),8,8,True),((44,22),10,2,True),(40,32)]);self.relate('connect','right-shell','podium');self.relate('connect','right-shell','middle-shell')
