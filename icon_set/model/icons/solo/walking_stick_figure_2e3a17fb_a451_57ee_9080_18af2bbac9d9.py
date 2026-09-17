'A thin stick figure walks toward the right beneath a circular head. The torso leans slightly forward, both arms angle downward, and the spread legs end in short horizontal feet.\n\nConstruction: Circular head and connected shoulder/hip graph preserve the reference posture; clothing outlines and minor folds omitted. Bounds (8,4)-(40,44).\nLucide: person-standing: separate round head, common limb junctions.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2e3a17fb-a451-57ee-9080-18af2bbac9d9'
SOURCE_PATH = 'pictographic-primitives/wayfinding/walking_2e3a17fb-a451-57ee-9080-18af2bbac9d9.svg'
AUTHOR = 'gpt-6'

class WalkingStickFigure(Solo48):
    icon_id = 'walking-stick-figure'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/wayfinding'
    aliases = ()
    keywords = ('person', 'walking', 'stick', 'figure', 'pedestrian', 'stride', 'sub icon')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_arc('person-head-top', (23, 7), (29, 7), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('person-head-bottom', (29, 7), (23, 7), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('person-body-1', (24, 19), (21, 31))
        self.add_line('person-arms-1', (10, 28), (24, 19))
        self.add_line('person-arms-2', (24, 19), (36, 29))
        self.add_line('person-legs-1', (8, 44), (21, 31))
        self.add_line('person-legs-2', (21, 31), (34, 44))
        self.add_line('person-legs-3', (34, 44), (40, 44))
        self.add_contour('person-head', 'person-head-top', 'person-head-bottom', closed=True)
        self.add_contour('person-body', 'person-body-1', closed=False)
        self.add_contour('person-arms', 'person-arms-1', 'person-arms-2', closed=False)
        self.add_contour('person-legs', 'person-legs-1', 'person-legs-2', 'person-legs-3', closed=False)
        self.relate('connect', 'person-body', 'person-arms')
        self.relate('connect', 'person-body', 'person-legs')


# Reviewed source-equivalent container sub-icon references.
SOURCE_REFERENCES = [('7ce62344-aeae-474c-9800-f2104921b059', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/wayfinding/walking_7ce62344-aeae-474c-9800-f2104921b059.svg')]
