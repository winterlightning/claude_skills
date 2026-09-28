"""Revision of person. The rejected arms made a peaked Y. Redrew them as the original shallow U-shaped shoulder sweep below a circular head and central stem.
Symbol plan: redraw the original subject with one coherent SOLO48 construction.
"""
'person: independent smooth-curve repair.\n\nConstruction: Person with detached circular head and lifted curved arms. Head lower edge 18, shoulder/torso node 26 gives exactly four units of ink gap.\nKeyshape: VRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/human_ref/user.svg (human proportions).\nOriginal source and parent geometry preserved.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '39d4dade-8ad3-48bc-a8ba-99e528562c38'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__person/20260927T074149Z-thuan-mac-1/reference/person_39d4dade-8ad3-48bc-a8ba-99e528562c38.svg'
AUTHOR = "gpt-6"


class Person(Solo48):
    icon_id = 'person'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    categories = ('symbol',)
    aliases = ()
    keywords = ('person', 'symbol')
    keyshape = Keyshape.VRECT_L

    def build(self):
        ellipse(self,'head',24,11,7)
        self.add_bezier('left-arm',(8,30),((12,34),(16,36),(24,36)))
        self.add_bezier('right-arm',(24,36),((32,36),(36,34),(40,30)))
        self.add_contour('shoulders','left-arm','right-arm')
        line(self,'torso-upper',(24,26),(24,36))
        line(self,'torso-lower',(24,36),(24,44))
        self.relate('connect','shoulders','torso-upper')
        self.relate('connect','shoulders','torso-lower')
        self.relate('connect','torso-upper','torso-lower')
        self.mark_human_figure('person',head='head',torso='torso-upper',torso_junction='start')
