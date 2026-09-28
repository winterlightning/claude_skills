"""Complete reference redraw on SUB32; earlier incomplete variant preserved.
Source parts: frame, spine, upper, lower.
Construction: native 32px layout, 4px strokes, integer nodes; complete source comparison.

"""
from icon_set.model.icons.sub._base import Sub32
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = '58c80690-dc34-4d48-a622-ec4aa12c8598'
SOURCE_PATH = 'pictographic-primitives/state/radiology xray_58c80690-dc34-4d48-a622-ec4aa12c8598.svg'
AUTHOR = 'gpt-6'
class CompleteReferenceRedraw(Sub32):
    icon_id = 'rib-cage-diagram-v2'
    variant_of = 'rib-cage-diagram'
    variant_label = 'Complete reference redraw'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    categories = ('state',)
    def build(self):
        self.add_line('frame-0-0', (5, 2), (27, 2))
        self.add_arc('frame-0-1', (27, 2), (30, 5), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('frame-0-2', (30, 5), (30, 27))
        self.add_arc('frame-0-3', (30, 27), (27, 30), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('frame-0-4', (27, 30), (5, 30))
        self.add_arc('frame-0-5', (5, 30), (2, 27), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('frame-0-6', (2, 27), (2, 5))
        self.add_arc('frame-0-7', (2, 5), (5, 2), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('frame-0', 'frame-0-0', 'frame-0-1', 'frame-0-2', 'frame-0-3', 'frame-0-4', 'frame-0-5', 'frame-0-6', 'frame-0-7', closed=True)
        self.add_line('spine-0-0', (16, 9), (16, 22))
        self.add_line('spine-1-0', (12, 22), (20, 22))
        self.add_bezier('upper-0-0', (9, 11), ((12.0, 8.0), (20.0, 8.0), (23, 11)))
        self.add_bezier('lower-0-0', (9, 18), ((12.0, 15.0), (20.0, 15.0), (23, 18)))
        self.relate('connect', 'spine-0-0', 'lower-0-0')
        self.relate('connect', 'spine-0-0', 'spine-1-0')
        self.relate('connect', 'spine-0-0', 'upper-0-0')
        self.relate('connect', 'spine-1-0', 'lower-0-0')
        self.relate('connect', 'spine-1-0', 'upper-0-0')
