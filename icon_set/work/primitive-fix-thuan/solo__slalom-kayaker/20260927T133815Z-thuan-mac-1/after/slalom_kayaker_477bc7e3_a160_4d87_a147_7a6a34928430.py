"""slalom-kayaker: Kayaker leaning back in a sharply tilted hull with a diagonal paddle. Head center (32,7), radius 3; shoulder y18 gives exact 4-unit ink clearance. A single torso/grip stroke replaces overlapping arms; blade outlines and water omitted."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '477bc7e3-a160-4d87-a147-7a6a34928430'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__slalom-kayaker/20260927T133815Z-thuan-mac-1/reference/sport kayaking_477bc7e3-a160-4d87-a147-7a6a34928430.svg'
AUTHOR = 'gpt-6'

class SlalomKayaker(Solo48):
    icon_id = 'slalom-kayaker'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'outdoors'
    categories = ('outdoors', 'primitives')
    aliases = ()
    keywords = ('kayaking', 'kayak', 'paddle', 'whitewater', 'sport', 'water', 'slalom', 'outdoors-batch-03')

    def build(self):
        # A paddler sits on a long canoe and grips a diagonal double-ended shaft.
        # His detached head is eight centerline units above the torso junction.
        self.add_arc('head-top', (14, 12), (22, 12), radius_x=4)
        self.add_arc('head-bottom', (22, 12), (14, 12), radius_x=4)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_bezier('torso', (18, 24), ((18, 28), (14, 30), (12, 32)))
        self.add_polyline('arm', (18, 24), (26, 24), (32, 20))
        self.add_polyline('paddle', (40, 8), (32, 20), (24, 32))
        self.add_line('hull-left', (4, 32), (12, 40))
        self.add_line('hull-bottom', (12, 40), (36, 40))
        self.add_arc('hull-bow', (36, 40), (44, 32), radius_x=8, sweep=True)
        self.add_contour('hull', 'hull-left', 'hull-bottom', 'hull-bow')
        self.add_line('gunwale-left', (4, 32), (12, 32))
        self.add_line('gunwale-right', (12, 32), (24, 32))
        self.add_contour('gunwale', 'gunwale-left', 'gunwale-right')
        self.relate('connect', 'torso', 'arm')
        self.relate('connect', 'arm', 'paddle')
        self.relate('connect', 'torso', 'gunwale')
        self.relate('connect', 'paddle', 'gunwale')
        self.relate('connect', 'hull', 'gunwale')
        self.mark_human_figure('paddler', head='head', torso='torso',
                               torso_junction='start')
