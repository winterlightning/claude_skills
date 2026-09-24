"""Sad Head Profile.

Plan: Continuous anatomical neck and right-facing skull; expression marks remain intrinsic. Bounds (8,4)-(40,44). Human user.svg informs smooth skull; reference profile keeps its natural neck.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '96c50c3f-13ad-5908-ba78-3a34437c067f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/depression disorder symptoms_96c50c3f-13ad-5908-ba78-3a34437c067f.svg'
AUTHOR = 'gpt-6'


class SadHeadProfile(Solo48):
    icon_id = 'sad-head-profile'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/health'
    aliases = ()
    keywords = ('sad', 'head', 'profile')

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
        self.add_line('eye',(23,19),(26,17))
