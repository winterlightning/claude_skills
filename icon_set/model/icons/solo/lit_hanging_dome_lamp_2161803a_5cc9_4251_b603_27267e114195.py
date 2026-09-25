'Hanging Pendant Lamp.\nPlan: Domed lamp under a central cord; bulb below the rim and three separated light rays.\nConstruction reference: Lucide lamp-ceiling: dome, central cord and bulb attachment.\nReduction: Small cap absorbed into the cord/dome junction.\nKeyshape: SQUARE; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2161803a-5cc9-4251-b603-27267e114195'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_19/fixture_2161803a-5cc9-4251-b603-27267e114195.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'lit-hanging-dome-lamp'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('lit', 'hanging', 'dome', 'lamp')

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

        path('shade',(6,26),[((24,8),18,18,True),((42,26),18,18,True),(30,26),(18,26),(6,26)],True)
        self.add_line('cord',(24,6),(24,8));self.relate('connect','cord','shade')
        path('bulb',(30,26),[((18,26),6,6,True)]);self.relate('connect','bulb','shade')
        self.add_line('ray-center',(24,40),(24,42))
        self.add_line('ray-left',(8,36),(6,38));self.add_line('ray-right',(40,36),(42,38))
