"""Explicit, user-requested container-content size variants.

The ordinary SYMBOL32 profile is unchanged. Resize models author literal grid
geometry in their own declared ink rectangle, with the same 4-unit stroke and
clearance checks. They must be placed at native size and checked against each
container; a passing standalone model does not certify a combination.
"""
from ._base import Symbol32
from ...keyshapes import Keyshape


class ResizeSymbol(Symbol32):
    sizing_mode = 'container-content-resize'
    canvas_width = 24
    canvas_height = 24
    keyshape = Keyshape.SQUARE

    def place_family_anchors(self):
        self.add_anchor('center', (self.canvas_width // 2, self.canvas_height // 2))

    def keyshape_bounds(self):
        return (0, 0, self.canvas_width, self.canvas_height)

    def to_record(self):
        record = super().to_record()
        record.update(sizing_mode=self.sizing_mode, canvas_width=self.canvas_width,
                      canvas_height=self.canvas_height, native_size_only=True)
        return record


def resize_dimensions(icon):
    width, height = icon.canvas_width, icon.canvas_height
    if any(type(v) is not int or not 4 <= v <= 60 for v in (width, height)):
        raise ValueError('Container resize dimensions must be integer units from 4 to 60')
    return width, height
