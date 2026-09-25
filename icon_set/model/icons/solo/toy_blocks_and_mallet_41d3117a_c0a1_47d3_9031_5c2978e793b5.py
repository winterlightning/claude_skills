'Toy Blocks and Mallet.\nPlan: Four stacked blocks beside an upright toy mallet.\nConstruction reference: No useful exact local Lucide match; geometric arcs and coherent contours preserve the supplied subject.\nReduction: Stack stagger and mallet lean reduced; four blocks and mallet remain.\nKeyshape: SQUARE; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '41d3117a-c0a1-47d3-9031-5c2978e793b5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_38/toys building_41d3117a-c0a1-47d3-9031-5c2978e793b5.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'toy-blocks-and-mallet'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('toy', 'blocks', 'and', 'mallet')

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

        for j in range(4):
         y=6+j*12
         if j==3:y=34
        # Shared stack edges avoid overlapping strokes.
        path('stack',(6,6),[(22,6),(22,42),(6,42),(6,6)],True)
        for y in (15,24,33):
         self.add_line(f'seam-{y}',(6,y),(22,y));self.relate('connect',f'seam-{y}','stack')
        box('head',30,30,42,42,3)
        self.add_line('handle',(36,6),(36,30));self.relate('connect','handle','head')
