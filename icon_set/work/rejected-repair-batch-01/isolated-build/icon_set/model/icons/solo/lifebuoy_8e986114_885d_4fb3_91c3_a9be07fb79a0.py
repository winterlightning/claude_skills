'A circular lifebuoy has a large central opening and four bands wrapped across the ring at the cardinal points. The bands project slightly beyond the outer circular edge.\n\nConstruction: Concentric ring and four cardinal band seams, all derived from shared center and radii. Outer radius20, inner radius10.\nLucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8e986114-885d-4fb3-91c3-a9be07fb79a0'
SOURCE_PATH = 'pictographic-primitives/wayfinding/safety float_8e986114-885d-4fb3-91c3-a9be07fb79a0.svg'
AUTHOR = 'gpt-6'

class Lifebuoy(Solo48):
    icon_id = 'lifebuoy'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/wayfinding'
    aliases = ()
    keywords = ('lifebuoy', 'life', 'ring', 'rescue', 'water', 'safety')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_arc('outer-0', (24, 4), (44, 24), radius_x=20, radius_y=20, large_arc=False, sweep=True)
        self.add_arc('outer-1', (44, 24), (24, 44), radius_x=20, radius_y=20, large_arc=False, sweep=True)
        self.add_arc('outer-2', (24, 44), (4, 24), radius_x=20, radius_y=20, large_arc=False, sweep=True)
        self.add_arc('outer-3', (4, 24), (24, 4), radius_x=20, radius_y=20, large_arc=False, sweep=True)
        self.add_arc('inner-0', (24, 14), (34, 24), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_arc('inner-1', (34, 24), (24, 34), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_arc('inner-2', (24, 34), (14, 24), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_arc('inner-3', (14, 24), (24, 14), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_line('band-0', (24, 4), (24, 14))
        self.add_line('band-1', (44, 24), (34, 24))
        self.add_line('band-2', (24, 44), (24, 34))
        self.add_line('band-3', (4, 24), (14, 24))
        self.add_contour('outer', 'outer-0', 'outer-1', 'outer-2', 'outer-3', closed=True)
        self.add_contour('inner', 'inner-0', 'inner-1', 'inner-2', 'inner-3', closed=True)
        self.relate('connect', 'band-0', 'inner')
        self.relate('connect', 'band-0', 'outer')
        self.relate('connect', 'band-1', 'inner')
        self.relate('connect', 'band-1', 'outer')
        self.relate('connect', 'band-2', 'inner')
        self.relate('connect', 'band-2', 'outer')
        self.relate('connect', 'band-3', 'inner')
        self.relate('connect', 'band-3', 'outer')
