"""Throat and Mouth Section.

Plan: Continuous head outline and one inner throat wall describe an open anatomical section. User.svg informs rounded head; preserve continuous neck. Bounds (8,4)-(40,44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9f38ce10-e55a-5a94-96d2-dbb79d2aca3a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/condition throat problem_9f38ce10-e55a-5a94-96d2-dbb79d2aca3a.svg'
AUTHOR = 'gpt-6'


class ThroatAndMouthSection(Solo48):
    icon_id = 'throat-and-mouth-section'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    aliases = ()
    keywords = ('throat', 'and', 'mouth', 'section')

    def build(self):
        self.add_line('back',(40,44),(40,18))
        self.add_arc('skull',(40,18),(12,18),radius_x=14,sweep=False)
        self.add_polyline('face',(12,18),(8,26),(18,26))
        self.add_arc('throat-top',(18,26),(30,38),radius_x=12)
        self.add_line('throat-back',(30,38),(30,44))
        self.add_contour('head','back','skull','face-1','face-2','throat-top','throat-back')
        # Replace the temporary polyline contour with the full continuous head contour.
        self.contours=[c for c in self.contours if c.contour_id!='face']
        self.add_line('mouth-bottom',(8,36),(14,36))
        self.add_arc('throat-bottom',(14,36),(20,42),radius_x=6)
        self.add_line('throat-front',(20,42),(20,44))
        self.add_contour('inner-throat','mouth-bottom','throat-bottom','throat-front')
