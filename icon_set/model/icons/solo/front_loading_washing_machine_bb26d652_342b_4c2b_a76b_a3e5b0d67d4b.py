'A square washing machine has a large circular door centred on its front. A short horizontal control and a small round indicator sit near the top inside softly rounded cabinet corners.\n\nConstruction: Rounded appliance cabinet with a circular front door and two small controls; omitted laundry swirl. Bounds (8,4)-(40,44).\nLucide: washing-machine: rounded cabinet and round front-loading door.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bb26d652-342b-4c2b-a76b-a3e5b0d67d4b'
SOURCE_PATH = 'pictographic-primitives/wayfinding/laundry machine_bb26d652-342b-4c2b-a76b-a3e5b0d67d4b.svg'
AUTHOR = 'gpt-6'

class FrontLoadingWashingMachine(Solo48):
    icon_id = 'front-loading-washing-machine'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/wayfinding'
    aliases = ()
    keywords = ('washer', 'washing', 'machine', 'laundry', 'appliance', 'door')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_line('cabinet-0', (12, 4), (36, 4))
        self.add_arc('cabinet-1', (36, 4), (40, 8), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('cabinet-2', (40, 8), (40, 40))
        self.add_arc('cabinet-3', (40, 40), (36, 44), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('cabinet-4', (36, 44), (12, 44))
        self.add_arc('cabinet-5', (12, 44), (8, 40), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('cabinet-6', (8, 40), (8, 8))
        self.add_arc('cabinet-7', (8, 8), (12, 4), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('door-top', (17, 28), (31, 28), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_arc('door-bottom', (31, 28), (17, 28), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_line('control', (18, 13), (18, 13))
        self.add_line('control-right', (30, 13), (30, 13))
        self.add_contour('cabinet', 'cabinet-0', 'cabinet-1', 'cabinet-2', 'cabinet-3', 'cabinet-4', 'cabinet-5', 'cabinet-6', 'cabinet-7', closed=True)
        self.add_contour('door', 'door-top', 'door-bottom', closed=True)
