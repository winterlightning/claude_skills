'Western Cowboy Boot.\nPlan: Western boot: tall upright shaft, curved instep, extended rounded toe and distinct heel. Bounds6..42.\nConstruction reference: No useful exact local Lucide match; geometric arcs and coherent contours preserve the supplied subject.\nReduction: Retain shaft seam, heel and toe; omit sole seam to preserve clear interior.\nKeyshape: SQUARE; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '831680e3-7005-41a2-993a-b2cd1e024a57'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_19/footwear boots cowboy_831680e3-7005-41a2-993a-b2cd1e024a57.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'cowboy-boot-profile'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('cowboy', 'boot', 'profile')

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

        path('boot',(6,6),[(24,6),(24,22),((34,32),10,10,False),((42,40),8,8,True),(42,42),(20,42),(14,38),(14,42),(6,42),(6,6)],True)
        self.add_line('shaft-seam',(15,6),(15,26));self.relate('connect','shaft-seam','boot')
