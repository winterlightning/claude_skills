'Human construction repair. Reposition head over the anatomical shoulder. Set head-outline to shoulder centerline separation to exactly 8u. Align the upper torso tangent with its own head center.\nShared reference: icon_set/references/human_ref/full_body_ref.png; busts use human_ref/user.svg.\nLucide person-standing original and atomic-debug inform shared limb junctions. Preserve intentional action-pose asymmetry.\n'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4ed29164-79b1-5c31-a787-c6eaf3105619'
SOURCE_PATH = 'pictographic-primitives/sports/skiing cross country_4ed29164-79b1-5c31-a787-c6eaf3105619.svg'
AUTHOR = 'gpt-6'
HUMAN_CONSTRUCTION = 'stick-figure'

class CrossCountrySkierVariant2(Solo48):
    icon_id = 'cross-country-skier-v2'
    variant_of = 'cross-country-skier'
    variant_label = 'Correct human head and torso construction'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/sports'
    aliases = ()
    keywords = ('ski', 'cross-country', 'skier', 'pole', 'winter', 'stride')

    def build(self):
        self.add_arc('head-a', (20, 6), (20, 12), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('head-b', (20, 12), (20, 6), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('arms-1', (6, 22), (20, 20))
        self.add_line('arms-2', (20, 20), (28, 24))
        self.add_line('arms-3', (28, 24), (40, 19))
        self.add_line('torso-1', (20, 20), (20, 28))
        self.add_line('torso-2', (20, 28), (29, 34))
        self.add_line('torso-3', (29, 34), (27, 42))
        self.add_line('rear-leg-1', (20, 28), (13, 34))
        self.add_line('rear-leg-2', (13, 34), (6, 34))
        self.add_line('pole-1', (40, 12), (40, 19))
        self.add_line('pole-2', (40, 19), (38, 35))
        self.add_line('ski-1', (9, 42), (27, 42))
        self.add_line('ski-2', (27, 42), (39, 42))
        self.add_line('ski-3', (39, 42), (42, 38))
        self.add_contour('head', *('head-a', 'head-b'), closed=True)
        self.add_contour('arms', *('arms-1', 'arms-2', 'arms-3'), closed=False)
        self.add_contour('torso', *('torso-1', 'torso-2', 'torso-3'), closed=False)
        self.add_contour('rear-leg', *('rear-leg-1', 'rear-leg-2'), closed=False)
        self.add_contour('pole', *('pole-1', 'pole-2'), closed=False)
        self.add_contour('ski', *('ski-1', 'ski-2', 'ski-3'), closed=False)
        self.relate('connect', *('arms', 'torso'))
        self.relate('connect', *('torso', 'rear-leg'))
        self.relate('connect', *('pole', 'arms'))
        self.relate('connect', *('ski', 'torso'))
        self.mark_human_figure('person-1', head='head', torso='torso-1', torso_junction='start')
