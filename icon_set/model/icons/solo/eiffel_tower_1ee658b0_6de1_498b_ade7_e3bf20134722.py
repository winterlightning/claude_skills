"""Eiffel Tower: flared legs, two decks and an open base arch; latticework omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1ee658b0-6de1-498b-ade7-e3bf20134722'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-02/eiffel tower_1ee658b0-6de1-498b-ade7-e3bf20134722.svg'
AUTHOR = 'gpt-6'


class EiffelTower(Solo48):
    icon_id = 'eiffel-tower'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "places/landmarks"
    aliases = ()
    keywords = ('eiffel tower', 'paris', 'france', 'tower', 'landmark', 'monument', 'travel', 'architecture')

    def build(self) -> None:
        # Centerline extremes: (5,2)-(43,46); shared axis x=24.
        self.add_arc('left-foot', (5,46), (13,32), radius_x=65, sweep=False)
        self.add_arc('left-middle', (13,32), (18,21), radius_x=65, sweep=False)
        self.add_arc('left-neck', (18,21), (20,10), radius_x=65, sweep=False)
        self.add_arc('crown', (20,10), (28,10), radius_x=4, sweep=True)
        self.add_arc('right-neck', (28,10), (30,21), radius_x=65, sweep=False)
        self.add_arc('right-middle', (30,21), (35,32), radius_x=65, sweep=False)
        self.add_arc('right-foot', (35,32), (43,46), radius_x=65, sweep=False)
        self.add_contour('tower','left-foot','left-middle','left-neck','crown','right-neck','right-middle','right-foot')
        self.add_line('spire',(24,2),(24,6))
        self.relate('connect','spire','tower')
        self.add_polyline('upper-deck',(16,21),(18,21),(30,21),(32,21))
        self.relate('connect','upper-deck','tower')
        self.add_polyline('lower-deck',(10,32),(13,32),(35,32),(38,32))
        self.relate('connect','lower-deck','tower')
        self.add_arc('base-arch',(17,46),(31,46),radius_x=7,sweep=True)
