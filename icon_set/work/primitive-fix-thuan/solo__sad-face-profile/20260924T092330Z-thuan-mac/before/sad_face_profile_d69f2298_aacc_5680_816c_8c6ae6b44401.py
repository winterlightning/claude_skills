"""Sad Face Profile.

Plan: Continuous anatomical neck and right-facing skull; expression marks remain intrinsic. Bounds (8,4)-(40,44). Human user.svg informs smooth skull; reference profile keeps its natural neck.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd69f2298-aacc-5680-816c-8c6ae6b44401'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/sadness emotions_d69f2298-aacc-5680-816c-8c6ae6b44401.svg'
AUTHOR = 'gpt-6'


class SadFaceProfile(Solo48):
    icon_id = 'sad-face-profile'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/health'
    aliases = ()
    keywords = ('sad', 'face', 'profile')

    def build(self):
        self.add_line('rear-neck',(14,44),(14,34))
        self.add_arc('rear-bend',(14,34),(8,26),radius_x=6,radius_y=8)
        self.add_line('rear',(8,26),(8,18))
        self.add_arc('skull',(8,18),(36,18),radius_x=14)
        self.add_line('nose-0',(36, 18),(40, 26))
        self.add_line('nose-1',(40, 26),(30, 26))
        self.add_line('nose-2',(30, 26),(30, 32))
        self.add_arc('chin',(30,32),(24,38),radius_x=6)
        self.add_line('neck-front',(24,38),(24,44))
        self.add_contour('profile','rear-neck','rear-bend','rear','skull','nose-0','nose-1','nose-2','chin','neck-front')
        self.add_arc('mouth',(22,34),(30,32),radius_x=8,radius_y=2)
        self.relate('connect','mouth','profile')
        self.add_line('eye',(23,18),(26,18))
