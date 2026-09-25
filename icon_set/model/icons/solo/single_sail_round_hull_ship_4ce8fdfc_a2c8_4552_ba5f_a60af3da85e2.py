'Ancient Wooden Sailing Ship.\nPlan: Rounded hull with raised bow/stern and one semicircular sail on central mast.\nConstruction reference: No useful exact local Lucide match; geometric arcs and coherent contours preserve the supplied subject.\nReduction: Portholes removed to retain a broad open hull at 48px.\nKeyshape: SQUARE; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4ce8fdfc-a2c8-4552-ba5f-a60af3da85e2'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_22/history noahs ark_4ce8fdfc-a2c8-4552-ba5f-a60af3da85e2.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'single-sail-round-hull-ship'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('single', 'sail', 'round', 'hull', 'ship')

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

        path('hull',(6,28),[(6,30),((18,42),12,12,False),(30,42),((42,30),12,12,False),(42,28)])
        self.add_polyline('deck',(6,28),(24,28),(42,28));self.relate('connect','hull','deck')
        self.add_line('mast',(24,6),(24,28));self.relate('connect','mast','deck')
        path('sail',(24,6),[((24,20),13,7,True)])
        self.relate('connect','sail','mast')
