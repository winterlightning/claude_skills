'A wide rectangular barrier panel stands below two circular reflectors mounted on short poles. The panel has three short vertical markings, while each reflector is bisected by its supporting pole.\n\nConstruction: Wide barrier with two pole-mounted round reflectors; panel markings reduced to one division. Bounds (4,8)-(44,40).\nLucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '22dae701-3743-4304-b4be-5b434e6b5789'
SOURCE_PATH = 'pictographic-primitives/wayfinding/safety board_22dae701-3743-4304-b4be-5b434e6b5789.svg'
AUTHOR = 'gpt-6'

class RoadSafetyBarrier(Solo48):
    icon_id = 'road-safety-barrier'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/wayfinding'
    aliases = ()
    keywords = ('barrier', 'road', 'safety', 'reflector', 'construction', 'traffic')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_line('panel-0-joint-1', (7, 26), (14, 26))
        self.add_line('panel-0-joint-2', (14, 26), (24, 26))
        self.add_line('panel-0-joint-3', (24, 26), (34, 26))
        self.add_line('panel-0-joint-4', (34, 26), (41, 26))
        self.add_arc('panel-1', (41, 26), (44, 29), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('panel-2', (44, 29), (44, 37))
        self.add_arc('panel-3', (44, 37), (41, 40), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('panel-4-joint-1', (41, 40), (24, 40))
        self.add_line('panel-4-joint-2', (24, 40), (7, 40))
        self.add_arc('panel-5', (7, 40), (4, 37), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('panel-6', (4, 37), (4, 29))
        self.add_arc('panel-7', (4, 29), (7, 26), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('reflector-14-top', (9, 13), (19, 13), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('reflector-14-bottom-joint-1', (19, 13), (14, 18), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('reflector-14-bottom-joint-2', (14, 18), (9, 13), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('pole-14-1', (14, 18), (14, 26))
        self.add_arc('reflector-34-top', (29, 13), (39, 13), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('reflector-34-bottom-joint-1', (39, 13), (34, 18), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('reflector-34-bottom-joint-2', (34, 18), (29, 13), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('pole-34-1', (34, 18), (34, 26))
        self.add_line('stripe', (24, 26), (24, 40))
        self.add_contour('panel', 'panel-0-joint-1', 'panel-0-joint-2', 'panel-0-joint-3', 'panel-0-joint-4', 'panel-1', 'panel-2', 'panel-3', 'panel-4-joint-1', 'panel-4-joint-2', 'panel-5', 'panel-6', 'panel-7', closed=True)
        self.add_contour('reflector-14', 'reflector-14-top', 'reflector-14-bottom-joint-1', 'reflector-14-bottom-joint-2', closed=True)
        self.add_contour('pole-14', 'pole-14-1', closed=False)
        self.add_contour('reflector-34', 'reflector-34-top', 'reflector-34-bottom-joint-1', 'reflector-34-bottom-joint-2', closed=True)
        self.add_contour('pole-34', 'pole-34-1', closed=False)
        self.relate('connect', 'pole-14', 'reflector-14')
        self.relate('connect', 'pole-14', 'panel')
        self.relate('connect', 'pole-34', 'reflector-34')
        self.relate('connect', 'pole-34', 'panel')
        self.relate('connect', 'stripe', 'panel')
