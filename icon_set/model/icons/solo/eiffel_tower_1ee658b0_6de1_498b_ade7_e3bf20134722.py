"""Eiffel Tower: flared legs, two decks and an open base arch; latticework omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1ee658b0-6de1-498b-ade7-e3bf20134722'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-02/eiffel tower_1ee658b0-6de1-498b-ade7-e3bf20134722.svg'
AUTHOR = 'gpt-6'


class EiffelTower(Solo48):
    icon_id = 'eiffel-tower'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "landmarks"
    aliases = ()
    keywords = ('eiffel tower', 'paris', 'france', 'tower', 'landmark', 'monument', 'travel', 'architecture')

    def build(self) -> None:
        # Centerline extremes: (8,4)-(40,44); shared axis x=24.
        self.add_arc('left-foot', (8,44), (14,29), radius_x=65, sweep=False)
        self.add_arc('left-middle', (14,29), (18,21), radius_x=65, sweep=False)
        self.add_arc('left-neck', (18,21), (20,10), radius_x=65, sweep=False)
        self.add_arc('crown', (20,10), (28,10), radius_x=4, sweep=True)
        self.add_arc('right-neck', (28,10), (30,21), radius_x=65, sweep=False)
        self.add_arc('right-middle', (30,21), (34,29), radius_x=65, sweep=False)
        self.add_arc('right-foot', (34,29), (40,44), radius_x=65, sweep=False)
        self.add_contour('tower','left-foot','left-middle','left-neck','crown','right-neck','right-middle','right-foot')
        self.add_line('spire',(24,4),(24,6))
        self.relate('connect','spire','tower')
        self.add_polyline('upper-deck',(16,21),(18,21),(30,21),(32,21))
        self.relate('connect','upper-deck','tower')
        self.add_polyline('lower-deck',(11,29),(14,29),(34,29),(37,29))
        self.relate('connect','lower-deck','tower')
        self.add_arc('base-arch',(18,44),(30,44),radius_x=6,radius_y=4,sweep=True)
