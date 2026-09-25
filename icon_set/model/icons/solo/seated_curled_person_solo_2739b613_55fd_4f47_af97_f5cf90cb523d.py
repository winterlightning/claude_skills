"""Seated curled person.

Construction reference: human_ref/full_body_ref.png.
Head r=6 at y=12, torso starts y=26: exact 4 ink gap. Folded pose simplified to shared human line vocabulary.
SOLO48 explicitly requested for this source main by the user.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._side_main50_geometry import box, circle, path

SOURCE_ICON_ID = '2739b613-55fd-4f47-af97-f5cf90cb523d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/other/poverty person_2739b613-55fd-4f47-af97-f5cf90cb523d.svg'
AUTHOR = 'gpt-6'


class SourceMain(Solo48):
    icon_id = 'seated-curled-person-solo-2739b613'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ('seated-curled-person',)
    keywords = ('seated', 'curled', 'person')

    def build(self):
        # Head follows the upper torso axis; both knees fold toward the arm.
        circle(self,'head',12,12,6)
        self.add_line('torso',(12,26),(12,34))
        path(self,'seat',(12,34),[('A',(20,42),8,8,False)])
        self.add_polyline('legs',(20,42),(30,30),(42,42))
        self.add_polyline('arm',(12,26),(30,26),(30,30))
        self.relate('connect','torso','seat')
        self.relate('connect','seat','legs')
        self.relate('connect','torso','arm')
        self.relate('connect','arm','legs')
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
