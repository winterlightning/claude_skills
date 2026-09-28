'Animal Paw Print.\nPlan: Four equal circular toes arc above a broad pad; repeated toe radii and mirrored centers.\nConstruction reference: Lucide paw-print: separated toe circles and a single coherent main pad.\nReduction: Toe ellipses made circular for clean small holes; four-toe count retained.\nKeyshape: SQUARE; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b7dc186c-d334-4937-b220-2a4c409ee232'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_20/furry_b7dc186c-d334-4937-b220-2a4c409ee232.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'four-toed-paw-print'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('four', 'toed', 'paw', 'print')

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

        for j,(x,y) in enumerate(((9,22),(16,9),(32,9),(39,22))):circle(f'toe-{j}',x,y,3)
        path('pad',(16,32),[((24,28),8,8,True),((32,32),8,8,True),((36,37),6,6,True),((30,42),6,5,True),(18,42),((12,37),6,5,True),((16,32),6,6,True)],True)

# Additional original represented by this same concept; no duplicate drawing.
SOURCE_REFERENCES = [{'source_icon_id': 'f880db22-3d86-4bd8-a4ca-6c2995942d3d', 'source_path': '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_25/lion footprint_f880db22-3d86-4bd8-a4ca-6c2995942d3d.svg'}, ('959794ae-1023-4273-a3cf-8add9155265b', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/paw print_959794ae-1023-4273-a3cf-8add9155265b.svg')]
