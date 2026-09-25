"""A closed doorway with round upper corners, right knob and threshold.
VRECT_L (8,4)-(40,44) preserves tall proportions. Source supplies door,
knob and threshold; Lucide door-closed supplies the single clean jamb contour.
Omit the duplicate inset frame to give the right-side knob a 9-unit gap.
Jambs mirror x24; threshold is split at their shared attachment nodes.
"""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID="1e50ca54-66dd-466e-b562-d683c18ad8d4"
SOURCE_PATH="pictographic-primitives/_uncategorized_15/doorway_1e50ca54-66dd-466e-b562-d683c18ad8d4.svg"
AUTHOR="gpt-6"
class Drawing(Solo48):
    icon_id="plain-door-in-broad-rounded-frame"
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases=("Entrance Door with Doorknob",)
    keywords=("door","frame","entrance","knob","threshold","building","closed")
    def build(self):
        self.add_line("left-jamb",(12,44),(12,8))
        self.add_arc("top-left",(12,8),(16,4),radius_x=4)
        self.add_line("lintel",(16,4),(32,4))
        self.add_arc("top-right",(32,4),(36,8),radius_x=4)
        self.add_line("right-jamb",(36,8),(36,44))
        self.add_contour("door","left-jamb","top-left","lintel","top-right","right-jamb")
        self.add_polyline("threshold",(8,44),(12,44),(36,44),(40,44))
        self.relate("connect","door","threshold")
        self.add_dot("knob",(27,26))
