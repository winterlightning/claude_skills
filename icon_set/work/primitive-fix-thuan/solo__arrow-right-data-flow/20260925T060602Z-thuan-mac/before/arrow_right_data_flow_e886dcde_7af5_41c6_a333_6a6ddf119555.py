"""A right arrow between rows of data ticks and rounded row interruptions.
HRECT_L preserves wide rows at y8/40. Root owns mirrored data rows, each
with three equally spaced ticks and one U, and a central arrow. Reduced
five ticks to three. Source: flow arrangement; Lucide arrow-right original
and atoms: single shaft meeting a two-segment arrowhead at one node.
"""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = "e886dcde-7af5-41c6-a333-6a6ddf119555"
SOURCE_PATH = "pictographic-primitives/_uncategorized_12/coding apps website big data arrow_e886dcde-7af5-41c6-a333-6a6ddf119555.svg"
AUTHOR = "gpt-6-astra"
class Drawing(Solo48):
    icon_id = "arrow-right-data-flow"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "Uncategorized"
    aliases = ["Data Flow Right Arrow"]
    keywords = ["arrow", "right", "data", "flow", "rows", "diagram", "connection"]
    def build(self):
        for side in (-1,1):
            y=lambda d:24+side*d
            prefix="upper" if side<0 else "lower"
            for j,x in enumerate((4,12,20)):
                self.add_line(f"{prefix}-tick-{j}",(x,y(16)),(x,y(12)))
            self.add_line(prefix+"-left",(28,y(16)),(28,y(12)))
            self.add_arc(prefix+"-curve",(28,y(12)),(44,y(12)),radius_x=8,radius_y=4,sweep=side>0)
            self.add_line(prefix+"-right",(44,y(12)),(44,y(16)))
            self.add_contour(prefix+"-u",prefix+"-left",prefix+"-curve",prefix+"-right")
        self.add_line("shaft",(4,24),(28,24))
        self.add_polyline("head",(20,20),(28,24),(20,28))
        self.relate("connect","shaft","head")
