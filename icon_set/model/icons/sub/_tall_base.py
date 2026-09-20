"""User-approved source-proportionate side-only canvas exceptions.

Use SourceFaithfulSideSub when the complete original needs a larger canvas.
SideSub32Exception retains the earlier one-axis32 contract.
Keep SUB32's 4px stroke, grid and clearance rules. TallSideSub32 preserves the
previously approved 32×48 records. Square container slots remain separate.
"""
import sys
from ._base import Sub32

APPROVED_SOURCES = frozenset({
    '8d317b81-2d88-4d5c-9090-0c063df565b3',
    '3ebbbe60-66ff-4346-a1c8-9367527d9ea9',
    '1b6ce2a0-ce30-49ce-99cf-a772bb04245d',
    'd540aa9a-0088-4ba3-b31e-9f6965432001',
})


class SourceFaithfulSideSub(Sub32):
    """Larger source-proportionate side artwork, preserving the fixed 4px stroke."""
    canvas_width = 32
    canvas_height = 48
    sizing_mode = "side-source-fit"

    def __init__(self):
        w, h = self.canvas_width, self.canvas_height
        if type(w) is not int or type(h) is not int or min(w, h) < 32:
            raise ValueError("Source-faithful side artwork requires integer dimensions >= 32")
        super().__init__()

    def place_family_anchors(self):
        self.add_anchor("center", (self.canvas_width // 2, self.canvas_height // 2))

    def keyshape_bounds(self):
        return (0, 0, self.canvas_width, self.canvas_height)

    def to_record(self):
        record = super().to_record()
        record.update(sizing_mode=self.sizing_mode, canvas_width=self.canvas_width,
                      canvas_height=self.canvas_height, side_only=True)
        return record


class SideSub32Exception(SourceFaithfulSideSub):
    """Earlier one-axis32 exception; preserve its explicit dimension contract."""
    sizing_mode = "side-one-axis32"

    def __init__(self):
        if 32 not in (self.canvas_width, self.canvas_height):
            raise ValueError("Side exception requires one 32px side")
        super().__init__()


class TallSideSub32(SideSub32Exception):
    sizing_mode = 'side-32x48'

    def place_family_anchors(self):
        self.add_anchor('center', (16, 24))

    def __init__(self):
        source = getattr(sys.modules[type(self).__module__], 'SOURCE_ICON_ID', None)
        if source not in APPROVED_SOURCES:
            raise ValueError('32×48 side exception requires an approved source')
        super().__init__()

    def keyshape_bounds(self):
        return (0, 0, 32, 48)

    def to_record(self):
        record = super().to_record()
        record.update(sizing_mode=self.sizing_mode, canvas_width=32,
                      canvas_height=48, side_only=True)
        return record
