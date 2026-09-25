'Whale Tail In Water.\nPlan: Whale flukes with central V-notch, narrow stock and two water levels. Bounds6..42.\nConstruction reference: No useful exact local Lucide match; geometric arcs and coherent contours preserve the supplied subject.\nReduction: Upper water is straight at stock attachments; lower water retains waves.\nKeyshape: SQUARE; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4e52c061-7d53-41ae-87b5-9945a54f08f0'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_19/fluke_4e52c061-7d53-41ae-87b5-9945a54f08f0.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'whale-tail-above-waves'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('whale', 'tail', 'above', 'waves')

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

        self.add_bezier('top',(6,6),((8,12),(18,6),(24,16)),((30,6),(40,12),(42,6)))
        self.add_bezier('right',(42,6),((42,20),(30,18),(30,22)))
        self.add_line('stock-right',(30,22),(30,30))
        self.add_line('stock-bottom',(30,30),(18,30))
        self.add_line('stock-left',(18,30),(18,22))
        self.add_bezier('left',(18,22),((18,18),(6,20),(6,6)))
        self.add_contour('tail','top','right','stock-right','stock-bottom','stock-left','left',closed=True)
        self.add_line('water-left',(6,30),(18,30));self.add_line('water-right',(30,30),(42,30))
        self.relate('connect','tail','water-left');self.relate('connect','tail','water-right')
        path('wave',(6,40),[((18,40),6,2,True),((30,40),6,2,False),((42,40),6,2,True)])
