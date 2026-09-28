"""Throat and Mouth Section.

Plan: Continuous head outline and one inner throat wall describe an open anatomical section. User.svg informs rounded head; preserve continuous neck. Bounds (8,4)-(40,44).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '9f38ce10-e55a-5a94-96d2-dbb79d2aca3a'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__throat-and-mouth-section/20260927T155415Z-thuan-mac-1/reference/condition throat problem_9f38ce10-e55a-5a94-96d2-dbb79d2aca3a.svg'
AUTHOR = "gpt-6"


class ThroatAndMouthSection(Solo48):
    icon_id = 'throat-and-mouth-section'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    categories = ('health', 'primitives')
    aliases = ()
    keywords = ('throat', 'and', 'mouth', 'section')

    def build(self):
        self.add_line('back',(40,44),(40,18))
        self.add_arc('skull',(40,18),(12,18),radius_x=14,sweep=False)
        self.add_polyline('face',(12,18),(12,23),(8,28),(13,29),(13,32),(8,35))
        self.add_bezier('throat-top',(8,35),((23,28),(30,35),(30,44)))
        self.add_contour('head','back','skull','face-1','face-2','face-3','face-4','face-5','throat-top')
        # The mouth opens into two separated walls of the throat section.
        self.contours=[c for c in self.contours if c.contour_id!='face']
        self.add_line('mouth-bottom',(8,35),(16,35))
        self.add_bezier('throat-bottom',(16,35),((19,35),(20,39),(20,44)))
        self.add_contour('inner-throat','mouth-bottom','throat-bottom')
        self.relate('connect','head','inner-throat')
