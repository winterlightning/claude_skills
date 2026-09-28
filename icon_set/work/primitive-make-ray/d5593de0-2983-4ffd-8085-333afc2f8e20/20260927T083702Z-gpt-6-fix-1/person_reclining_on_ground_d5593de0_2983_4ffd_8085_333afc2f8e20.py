"""Revision from the inspected source: The rejected figure had a tiny offset head and rigid reclining posture; the source has a larger head above a relaxed body.

Changes: Aligned and enlarged the head, set its exact detached gap to the torso, and brought the leaning upper body under it.
Full-body or bust construction follows icon_set/references/human_ref.
"""
'A seated person leans backward on one arm with the knees raised. The torso angles toward the round head, and the bent legs stretch across the lower-right side.\n\nConstruction: Reclining seated figure supports the body with one arm and raises both knees. Bounds (4,8)-(44,40).\nLucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'd5593de0-2983-4ffd-8085-333afc2f8e20'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__person-reclining-on-ground/20260927T083143Z-thuan-mac-1/reference/sitting relax_d5593de0-2983-4ffd-8085-333afc2f8e20.svg'
AUTHOR = "gpt-6"

class PersonRecliningOnGround(Solo48):
    icon_id = 'person-reclining-on-ground'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'wayfinding'
    categories = ('wayfinding', 'primitives')
    aliases = ()
    keywords = ('person', 'reclining', 'sitting', 'rest', 'ground', 'relax')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_arc('person-head-top', (12, 12), (20, 12), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('person-head-bottom', (20, 12), (12, 12), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('person-torso-1', (16, 24), (22, 40))
        self.add_line('person-arm-1', (16, 24), (10, 40))
        self.add_line('person-arm-2', (10, 40), (4, 40))
        self.add_line('person-legs-1', (22, 40), (34, 24))
        self.add_line('person-legs-2', (34, 24), (44, 36))
        self.add_contour('person-head', 'person-head-top', 'person-head-bottom', closed=True)
        self.add_contour('person-torso', 'person-torso-1', closed=False)
        self.add_contour('person-arm', 'person-arm-1', 'person-arm-2', closed=False)
        self.add_contour('person-legs', 'person-legs-1', 'person-legs-2', closed=False)
        self.relate('connect', 'person-torso', 'person-arm')
        self.relate('connect', 'person-torso', 'person-legs')
