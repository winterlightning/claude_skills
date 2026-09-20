"""Compact source composition. User allows stroke and spacing exceptions for the inner characters."""
from ._base import Sub32
from ...keyshapes import Keyshape
SOURCE_ICON_ID='937fbb98-3693-46f2-91da-e8ed80b0bdc3'
SOURCE_PATH='pictographic-primitives/state/circle oxi_937fbb98-3693-46f2-91da-e8ed80b0bdc3.svg'
AUTHOR="gpt-6"
TYPEFACE_GLYPH_IDS=('letter-o-uppercase', 'digit-2')
COMPACT_EXCEPTION = "User requested smaller inner symbols, allowing sub stroke/grid/spacing exceptions instead of enlargement."
class Drawing(Sub32):
    icon_id='oxygen-text-v3'
    variant_of='oxygen-text-v2'
    variant_label="Compact inner symbol"
    keyshape=Keyshape.SQUARE
    STROKE_WIDTH=2
    PATH_STROKE_WIDTHS={"frame":4}
    semantic_role="SUB"
    semantic_kind="modifier"
    category="primitives/mark"
    def build(self):
        self.add_arc('circle-top',(2,16),(30,16),radius_x=14)
        self.add_arc('circle-bottom',(30,16),(2,16),radius_x=14)
        self.add_contour('frame','circle-top','circle-bottom',closed=True)
        self.add_arc('o-top',(7,14),(15,14),radius_x=4)
        self.add_arc('o-bottom',(15,14),(7,14),radius_x=4)
        self.add_contour('o','o-top','o-bottom',closed=True)
        self.add_bezier('two-head',(19,14),((21,12),(24,14),(23,16)))
        self.add_polyline('two-foot',(23,16),(19,21),(24,21))

    def to_record(self):
        record=super().to_record()
        record["style"]["path_stroke_widths"]=dict(self.PATH_STROKE_WIDTHS)
        record["compact_exception"]=COMPACT_EXCEPTION
        return record
