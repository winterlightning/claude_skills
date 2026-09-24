'Traditional Bird Feather Quill.\nPlan: Diagonal feather with one broad notch and a projecting shaft.\nConstruction reference: Lucide feather: diagonal shaft and broad rounded vane; one source notch retained.\nReduction: Multiple fine notches reduced to one broad notch.\nKeyshape: SQUARE; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '93e084e6-277a-40cc-ae9f-d30ce99eb92e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_18/feather_93e084e6-277a-40cc-ae9f-d30ce99eb92e.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'notched-feather'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('notched', 'feather')

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

        path('vane',(12,36),[(12,22),(28,6),(34,6),((42,14),8,8,True),(42,20),(32,22),(38,30),(24,36),(12,36)],True)
        self.add_polyline('shaft',(6,42),(12,36),(24,24));self.relate('connect','shaft','vane')
