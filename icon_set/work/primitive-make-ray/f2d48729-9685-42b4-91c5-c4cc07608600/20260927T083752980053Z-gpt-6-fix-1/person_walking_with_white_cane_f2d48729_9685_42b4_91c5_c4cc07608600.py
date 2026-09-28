"""Revision from the inspected source: The current figure had a long straight left arm unlike the source bent walking pose; the cane and person merged into a generic stick figure.

Changes: Bent the free arm to distinguish the gait while preserving the right-hand cane attachment.
Full-body or bust construction follows icon_set/references/human_ref.
"""
'A walking person has spread legs and arms swinging in opposite directions. The right hand holds a long straight cane extending diagonally downward and ahead of the figure.\n\nConstruction: Walking stick figure probing ahead with a long diagonal white cane. Bounds (6,6)-(42,42).\nLucide: person-standing: separate head and shared shoulder/hip points.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'f2d48729-9685-42b4-91c5-c4cc07608600'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__person-walking-with-white-cane/20260927T083143Z-thuan-mac-1/reference/disability walk blind_f2d48729-9685-42b4-91c5-c4cc07608600.svg'
AUTHOR = "gpt-6"

class PersonWalkingWithWhiteCane(Solo48):
    icon_id = 'person-walking-with-white-cane'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'wayfinding'
    categories = ('wayfinding', 'primitives')
    aliases = ()
    keywords = ('blind', 'cane', 'walking', 'person', 'accessibility', 'mobility')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_arc('person-head-top', (19, 9), (25, 9), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('person-head-bottom', (25, 9), (19, 9), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('person-body-1', (22, 21), (20, 30))
        self.add_line('person-legs-1', (10, 42), (20, 30))
        self.add_line('person-legs-2', (20, 30), (28, 42))
        self.add_line('person-arms-1a', (6, 28), (9, 23))
        self.add_line('person-arms-1b', (9, 23), (22, 21))
        self.add_line('person-arms-2', (22, 21), (30, 28))
        self.add_line('white-cane', (30, 28), (42, 42))
        self.add_contour('person-head', 'person-head-top', 'person-head-bottom', closed=True)
        self.add_contour('person-body', 'person-body-1', closed=False)
        self.add_contour('person-legs', 'person-legs-1', 'person-legs-2', closed=False)
        self.add_contour('person-arms', 'person-arms-1a', 'person-arms-1b', 'person-arms-2', closed=False)
        self.relate('connect', 'person-body', 'person-legs')
        self.relate('connect', 'person-body', 'person-arms')
        self.relate('connect', 'white-cane', 'person-arms')
