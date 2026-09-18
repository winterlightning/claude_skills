"""User-authorized sub text layout: 32-unit ink height and natural grid width.

This explicit specialization does not change square SUB32 symbol dimensions.
Letter geometry is snapshotted from existing typeface reuse exports.
"""
from ._base import Sub32


class Text32Mixin:
    text_canvas_width = 32
    text_ink_bounds = (0, 0, 32, 32)
    sizing_mode = 'text-height32'

    def keyshape_bounds(self):
        return tuple(self.text_ink_bounds)

    def to_record(self):
        record = super().to_record()
        record.update(sizing_mode=self.sizing_mode, canvas_width=self.text_canvas_width,
                      canvas_height=32)
        return record


class TextSub32(Text32Mixin, Sub32):
    pass


def canvas_dimensions(icon):
    if isinstance(icon, Text32Mixin):
        width=icon.text_canvas_width
        if type(width) is not int or width < 4:
            raise ValueError('Text sub width must be a positive grid width of at least 4')
        return width, 32
    size=icon.profile.spec.canvas_size
    return size, size


def is_height32_dot_text(icon):
    """A point-only glyph scales its round caps to reach the requested ink height."""
    from ...primitives import Line
    primitives = icon.draw().primitives
    return (isinstance(icon, Text32Mixin) and icon.STROKE_WIDTH == 32
            and bool(primitives) and all(isinstance(p, Line) and p.is_dot for p in primitives))
