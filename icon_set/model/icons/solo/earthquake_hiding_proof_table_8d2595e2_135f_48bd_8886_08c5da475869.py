"""A crouching person shelters beneath a table with earthquake marks.
Plan: SQUARE fits the shelter and person.
Reduction: Table thickness and small limb folds omitted; outlined figure reinterpreted as a round-headed stick figure; each tremor simplified to two segments.
Construction: human_ref/full_body_ref.png: round head, coherent bent limbs and minimal anatomy. Head center (17,29), radius 3; neck (28,29) lies on the horizontal upper-torso axis. Actual nearest centerline gap 11-3=8, ink gap 4. No useful exact Lucide scene match.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8d2595e2-135f-48bd-8886-08c5da475869'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_16/earthquake hiding proof table_8d2595e2-135f-48bd-8886-08c5da475869.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'earthquake-hiding-proof-table'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('earthquake', 'hiding', 'proof', 'table')

    def path(self, name, start, segments, closed=False):
        members = []
        for i, spec in enumerate(segments):
            part = f"{name}-{i+1}"
            if len(spec) == 2:
                end = spec
                self.add_line(part, start, end)
            else:
                end, rx, ry, sweep = spec
                self.add_arc(part, start, end, radius_x=rx, radius_y=ry, sweep=sweep)
            members.append(part)
            start = end
        self.add_contour(name, *members, closed=closed)

    def circle(self, name, x, y, r):
        self.path(name, (x-r,y), [((x+r,y),r,r,True),((x-r,y),r,r,True)], True)

    def rect(self, name, x, y, w, h, r=3):
        self.path(name, (x+r,y), [(x+w-r,y),((x+w,y+r),r,r,True),(x+w,y+h-r),((x+w-r,y+h),r,r,True),(x+r,y+h),((x,y+h-r),r,r,True),(x,y+r),((x+r,y),r,r,True)], True)

    def build(self):
        # Human vocabulary: human_ref/full_body_ref.png, crouching round-headed figure.
        # Head (17,29), r3; horizontal neck at (28,29): 11-3=8 centerline / 4 ink gap.
        # Table's thin top and simplified limbs leave room for the complete shelter scene.
        self.add_polyline('table',(6,42),(6,18),(42,18),(42,42))
        for side in (-1,1):
            self.add_polyline(f'tremor-{side}',(24+side*18,10),(24+side*12,6),(24+side*6,10))
        self.circle('head',17,29,3)
        self.add_line('torso',(28,29),(32,29))
        self.add_line('back',(32,29),(32,34));self.relate('connect','torso','back')
        self.add_polyline('bent-leg',(32,34),(24,42),(22,42));self.relate('connect','back','bent-leg')
        self.add_line('right-leg',(32,34),(34,42));self.relate('connect','back','right-leg');self.relate('connect','bent-leg','right-leg')
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
