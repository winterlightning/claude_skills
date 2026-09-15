# Repair: Lift the rear shoulder edge to open clearance above the diagonal seatbelt.
"""occupant-side-airbag: reconstructed from the supplied transportation reference."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '459fafea-8852-475f-958c-4f343fbb4bc4'
SOURCE_PATH = 'pictographic-primitives/transportation/side airbag_459fafea-8852-475f-958c-4f343fbb4bc4.svg'
AUTHOR = 'gpt-6'

class OccupantSideAirbag(Solo48):
    icon_id = 'occupant-side-airbag'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('side airbag', 'airbag', 'safety', 'occupant', 'seat belt', 'car', 'dashboard', 'srs')

    def build(self) -> None:
        self.add_arc('head-top', (13, 7), (19, 7), radius_x=3)
        self.add_arc('head-bottom', (19, 7), (13, 7), radius_x=3)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_polyline('body', (8, 44), (8, 34), (8, 23), (16, 18), (22, 25), (22, 34), (22, 44))
        self.add_line('belt', (8, 34), (22, 25))
        self.add_line('seat', (8, 34), (22, 34))
        for part in ['body-1', 'body-2', 'body-4', 'body-5']:
            self.relate('connect', 'belt', part)
        for part in ['body-1', 'body-2', 'body-5', 'body-6']:
            self.relate('connect', 'seat', part)
        self.relate('connect', 'belt', 'seat')
        self.add_arc('airbag-top', (30, 15), (40, 15), radius_x=5, radius_y=10)
        self.add_arc('airbag-bottom', (40, 15), (30, 15), radius_x=5, radius_y=10)
        self.add_contour('airbag', 'airbag-top', 'airbag-bottom', closed=True)
        self.mark_human_figure('person', head='head', torso='body-3', torso_junction='end')
