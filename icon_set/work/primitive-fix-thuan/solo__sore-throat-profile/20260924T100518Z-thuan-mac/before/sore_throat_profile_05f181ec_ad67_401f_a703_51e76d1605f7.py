"""Sore Throat Profile.

Plan: Left-facing continuous head and neck; two diagonal throat marks integrated by open neck space. Bounds (8,4)-(40,44). Human reference informs skull simplicity; retain natural neck.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '05f181ec-ad67-401f-a703-51e76d1605f7'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/sore throat_05f181ec-ad67-401f-a703-51e76d1605f7.svg'
AUTHOR = 'gpt-6'


class SoreThroatProfile(Solo48):
    icon_id = 'sore-throat-profile'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/health'
    aliases = ()
    keywords = ('sore', 'throat', 'profile')

    def build(self):
        self.add_line('back-neck',(40,44),(40,32))
        self.add_line('back-bend',(40,32),(40,22))
        self.add_line('back',(40,22),(40,18))
        self.add_arc('skull',(40,18),(12,18),radius_x=14,sweep=False)
        self.add_line('nose-0',(12, 18),(8, 26))
        self.add_line('nose-1',(8, 26),(18, 26))
        self.add_line('nose-2',(18, 26),(18, 30))
        self.add_arc('chin',(18,30),(20,36),radius_x=2,radius_y=6,sweep=False)
        self.add_line('front-neck',(20,36),(20,44))
        self.add_contour('profile','back-neck','back-bend','back','skull','nose-0','nose-1','nose-2','chin','front-neck')
        self.add_line('symptom',(27,28),(30,31))
