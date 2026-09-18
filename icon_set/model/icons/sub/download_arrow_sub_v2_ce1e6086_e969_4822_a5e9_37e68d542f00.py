"""Complete reference redraw on SUB32; earlier incomplete variant preserved.
Source parts: frame, arrow, tray.
Construction: native 32px layout, 4px strokes, integer nodes; complete source comparison.

"""
from icon_set.model.icons.sub._base import Sub32
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = 'ce1e6086-e969-4822-a5e9-37e68d542f00'
SOURCE_PATH = 'pictographic-primitives/state/circle download_ce1e6086-e969-4822-a5e9-37e68d542f00.svg'
AUTHOR = 'gpt-6'
class CompleteReferenceRedraw(Sub32):
    icon_id = 'download-arrow-sub-v2'
    variant_of = 'download-arrow-sub'
    variant_label = 'Complete reference redraw'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    def build(self):
        self.add_arc('frame-0-0', (2, 16), (30, 16), radius_x=14, radius_y=14, large_arc=True, sweep=True)
        self.add_arc('frame-0-1', (30, 16), (2, 16), radius_x=14, radius_y=14, large_arc=True, sweep=True)
        self.add_contour('frame-0', 'frame-0-0', 'frame-0-1', closed=True)
        self.add_line('arrow-0-0', (16, 9), (16, 15))
        self.add_line('arrow-1-0', (12, 11), (16, 15))
        self.add_line('arrow-1-1', (16, 15), (20, 11))
        self.add_contour('arrow-1', 'arrow-1-0', 'arrow-1-1', closed=False)
        self.add_line('tray-0-0', (11, 20), (11, 22))
        self.add_line('tray-0-1', (11, 22), (21, 22))
        self.add_line('tray-0-2', (21, 22), (21, 20))
        self.add_contour('tray-0', 'tray-0-0', 'tray-0-1', 'tray-0-2', closed=False)
        self.relate('connect', 'arrow-0-0', 'arrow-1')
