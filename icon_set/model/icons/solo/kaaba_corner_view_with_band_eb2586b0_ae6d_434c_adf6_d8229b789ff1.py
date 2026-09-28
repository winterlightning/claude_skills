'The Holy Kaaba Shrine.\nPlan: Corner view of the Kaaba with a continuous upper band wrapping both visible walls.\nConstruction reference: Lucide box: shared corner and two exposed faces.\nReduction: No added religious lettering.\nKeyshape: VRECT_L; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'eb2586b0-ae6d-434c-adf6-d8229b789ff1'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_24/kaaba_eb2586b0-ae6d-434c-adf6-d8229b789ff1.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'kaaba-corner-view-with-band'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('kaaba', 'corner', 'view', 'with', 'band')

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

        self.add_polyline('outline',(24,4),(40,10),(40,20),(40,38),(24,44),(8,38),(8,20),(8,10),closed=True)
        self.add_polyline('roof-edge',(8,10),(24,16),(40,10));self.relate('connect','roof-edge','outline')
        self.add_polyline('band',(8,20),(24,26),(40,20));self.relate('connect','band','outline')
        self.add_polyline('corner',(24,16),(24,26),(24,44));self.relate('connect','corner','outline');self.relate('connect','corner','band');self.relate('connect','corner','roof-edge')
