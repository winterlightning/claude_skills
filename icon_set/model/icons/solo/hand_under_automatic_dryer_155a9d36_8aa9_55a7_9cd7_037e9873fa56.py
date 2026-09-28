"An open hand extends palm-up beneath a domed wall dryer. Three short wavy air streams descend from the dryer's flat underside toward the fingers and palm.\n\nConstruction: Domed dryer above a cupped hand; airflow marks and minor creases omitted to give the palm enough depth. Bounds (8,4)-(40,44).\nLucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used."
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '155a9d36-8aa9-55a7-9cd7-037e9873fa56'
SOURCE_PATH = 'pictographic-primitives/wayfinding/automatic hand dryer_155a9d36-8aa9-55a7-9cd7-037e9873fa56.svg'
AUTHOR = 'gpt-6'

class HandUnderAutomaticDryer(Solo48):
    icon_id = 'hand-under-automatic-dryer'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'wayfinding'
    categories = ('wayfinding', 'primitives')
    aliases = ()
    keywords = ('hand', 'dryer', 'automatic', 'hygiene', 'washroom', 'air')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_arc('dome-left', (8, 16), (20, 4), radius_x=12, radius_y=12, large_arc=False, sweep=True)
        self.add_line('dome-top', (20, 4), (28, 4))
        self.add_arc('dome-right', (28, 4), (40, 16), radius_x=12, radius_y=12, large_arc=False, sweep=True)
        self.add_line('dryer-base', (40, 16), (8, 16))
        self.add_line('hand-top-1', (8, 34), (16, 28))
        self.add_line('hand-top-2', (16, 28), (24, 28))
        self.add_line('hand-top-3', (24, 28), (30, 25))
        self.add_line('hand-top-4', (30, 25), (35, 25))
        self.add_arc('finger-upper', (35, 25), (40, 30), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('finger-lower', (40, 30), (38, 34), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('palm-1', (38, 34), (24, 44))
        self.add_line('palm-2', (24, 44), (8, 44))
        self.add_line('thumb', (24, 28), (30, 33))
        self.add_contour('dryer', 'dome-left', 'dome-top', 'dome-right', 'dryer-base', closed=True)
        self.add_contour('hand', 'hand-top-1', 'hand-top-2', 'hand-top-3', 'hand-top-4', 'finger-upper', 'finger-lower', 'palm-1', 'palm-2', closed=False)
        self.relate('connect', 'thumb', 'hand')
