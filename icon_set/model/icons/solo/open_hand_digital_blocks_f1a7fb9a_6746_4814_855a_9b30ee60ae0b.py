'Hand Holding Digital Building Blocks.\nPlan: Open palm under connected digital blocks with one detached top-right square.\nConstruction reference: Lucide hand-helping: broad upturned palm.\nReduction: One connected block cluster and one floating block preserve the digital motif.\nKeyshape: SQUARE; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f1a7fb9a-6746-4814-855a-9b30ee60ae0b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_37/technology robot hand ai logic_f1a7fb9a-6746-4814-855a-9b30ee60ae0b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'open-hand-digital-blocks'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('open', 'hand', 'digital', 'blocks')

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

        path('hand',(6,42),[(22,42),((42,32),20,10,False),(24,32),(16,32),((6,28),10,4,True)])
        self.add_polyline('blocks',(6,6),(16,6),(16,14),(24,14),(24,22),(14,22),(14,16),(6,16),closed=True)
        box('floating',34,6,42,14,2)
