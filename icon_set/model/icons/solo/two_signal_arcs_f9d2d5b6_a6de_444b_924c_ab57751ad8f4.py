'Wireless Radio Signal Waves.\nPlan: Two nested upward-curving signal arcs. Upper span4..44 apex10; inner ends38. Exact4,10..44,38.\nConstruction reference: Lucide radio original and atomic-debug: repeated detached circular signal bands; source contains only two crests.\nReduction: Keep the defining silhouette and essential parts.\nKeyshape: HRECT_M; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f9d2d5b6-a6de-444b-924c-ab57751ad8f4'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_24/key fob battery low_f9d2d5b6-a6de-444b-924c-ab57751ad8f4.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'two-signal-arcs'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('two', 'signal', 'arcs')

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

        path('outer',(4,24),[((24,10),20,14,True),((44,24),20,14,True)])
        path('inner',(14,38),[((24,32),10,6,True),((34,38),10,6,True)])
