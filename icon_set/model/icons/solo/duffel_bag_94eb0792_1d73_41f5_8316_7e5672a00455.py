'Travel Duffel Bag.\nPlan: Rounded duffel bag with a tall arching handle and front pocket mark.\nConstruction reference: Lucide briefcase: handle attaches to body; source rounded duffel silhouette retained.\nReduction: Keep the defining silhouette and essential parts.\nKeyshape: HRECT_L; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '94eb0792-1d73-41f5-8316-7e5672a00455'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_16/duffel_94eb0792-1d73-41f5-8316-7e5672a00455.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'duffel-bag'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('duffel', 'bag')

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

        box('bag',4,20,44,40,8)
        path('handle',(14,20),[(14,18),((34,18),10,10,True),(34,20)]);self.relate('connect','handle','bag')
        self.add_line('pocket',(20,30),(28,30))
