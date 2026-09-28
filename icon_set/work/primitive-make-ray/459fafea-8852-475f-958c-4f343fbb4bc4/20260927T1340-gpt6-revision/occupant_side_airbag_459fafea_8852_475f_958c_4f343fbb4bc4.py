# Repair: Lift the rear shoulder edge to open clearance above the diagonal seatbelt.
"""occupant-side-airbag: reconstructed from the supplied transportation reference."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '459fafea-8852-475f-958c-4f343fbb4bc4'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__occupant-side-airbag/20260927T133654Z-thuan-mac-1/reference/side airbag_459fafea-8852-475f-958c-4f343fbb4bc4.svg'
AUTHOR = 'gpt-6'

class OccupantSideAirbag(Solo48):
    icon_id = 'occupant-side-airbag'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    categories = ('transportation', 'primitives')
    aliases = ()
    keywords = ('side airbag', 'airbag', 'safety', 'occupant', 'seat belt', 'car', 'dashboard', 'srs')

    def build(self) -> None:
        self.add_arc('head-top', (13, 7), (19, 7), radius_x=3)
        self.add_arc('head-bottom', (19, 7), (13, 7), radius_x=3)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        # The two shoulder curves restore the rounded seated silhouette.
        self.add_line('back-lower', (8, 44), (8, 34))
        self.add_line('back-upper', (8, 34), (8, 23))
        self.add_bezier('shoulder-left', (8, 23), ((10, 20), (13, 18), (16, 18)))
        self.add_bezier('shoulder-right', (16, 18), ((20, 18), (22, 22), (22, 25)))
        self.add_line('front-upper', (22, 25), (22, 34))
        self.add_line('front-lower', (22, 34), (22, 44))
        self.add_contour('body', 'back-lower', 'back-upper', 'shoulder-left',
                         'shoulder-right', 'front-upper', 'front-lower')
        self.add_line('belt', (8, 34), (22, 25))
        self.add_line('seat', (8, 34), (22, 34))
        self.relate('connect', 'belt', 'body')
        self.relate('connect', 'seat', 'body')
        self.relate('connect', 'belt', 'seat')
        self.add_arc('airbag-top', (30, 15), (40, 15), radius_x=5, radius_y=10)
        self.add_arc('airbag-bottom', (40, 15), (30, 15), radius_x=5, radius_y=10)
        self.add_contour('airbag', 'airbag-top', 'airbag-bottom', closed=True)
        self.mark_human_figure('person', head='head', torso='shoulder-right', torso_junction='start')
