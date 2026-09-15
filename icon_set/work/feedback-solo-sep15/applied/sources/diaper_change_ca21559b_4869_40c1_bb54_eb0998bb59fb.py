"""Separate the mother’s hand from the baby by eight centerline units (four visible units). Applied to the original icon identity."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'ca21559b-4869-40c1-bb54-eb0998bb59fb'
SOURCE_PATH = 'pictographic-primitives/babies/family baby change diaper_ca21559b-4869-40c1-bb54-eb0998bb59fb.svg'
AUTHOR = 'gpt-6'
HUMAN_CONSTRUCTION = 'mixed-adult-infant'

class DiaperChange(Solo48):
    icon_id = 'diaper-change'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'people/babies'
    aliases = ()
    keywords = ('diaper', 'change', 'infant', 'nursery')

    def build(self):
        """Symbol plan: Separate the mother’s hand from the baby by eight centerline units (four visible units). Reference: icon_set/references/human_ref/full_body_ref.png: circular head, coherent limbs, exact 4-unit detached head-to-torso gap."""
        self.add_arc('adult-head-top', (13, 11), (23, 11), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('adult-head-bottom', (23, 11), (13, 11), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_bezier('adult-back-1', (18, 24), *(((18.0, 27.25), (12.0, 28.5), (10, 30)),))
        self.add_line('adult-back-2', (10, 30), (6, 42))
        self.add_line('adult-arm-1', (18, 24), (18, 33))
        self.add_line('adult-arm-2', (18, 33), (20, 33))
        self.add_line('baby-body-1', (28, 22), (28, 34))
        self.add_line('baby-body-2', (28, 34), (28, 28))
        self.add_arc('baby-head-top', (36, 28), (42, 28), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('baby-head-bottom', (42, 28), (36, 28), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('surface', (23, 42), (42, 42))
        self.add_contour('adult-head', *('adult-head-top', 'adult-head-bottom'), closed=True)
        self.add_contour('adult-back', *('adult-back-1', 'adult-back-2'), closed=False)
        self.add_contour('adult-arm', *('adult-arm-1', 'adult-arm-2'), closed=False)
        self.add_contour('baby-body', *('baby-body-1', 'baby-body-2'), closed=False)
        self.add_contour('baby-head', *('baby-head-top', 'baby-head-bottom'), closed=True)
        self.relate('connect', *('adult-back', 'adult-arm'))
        self.mark_human_figure('person-1', head='adult-head', torso='adult-back-1', torso_junction='start')
