"""Shallow crescent sausage with forked casing ties.
HRECT_M: ends and ties reach (4,10)-(44,38). Body owns a mirrored
four-run casing; shared upper corners own the two forks. Reference supplies
crescent and tied tips; tiny cap rounding omitted. Lucide sausage: no match.
"""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = "b014012a-ab85-4245-8dbd-a66dc5a899be"
SOURCE_PATH = "pictographic-primitives/_uncategorized_08/bratwurst_b014012a-ab85-4245-8dbd-a66dc5a899be.svg"
AUTHOR = "gpt-6-astra"
class Drawing(Solo48):
    icon_id = "curved-sausage-with-tied-ends"
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "Uncategorized"
    aliases = ["Curved Bratwurst Sausage"]
    keywords = ["sausage", "bratwurst", "food", "meat", "casing", "curved", "cooking"]
    def build(self):
        self.add_bezier("casing-top", (8,18), ((14,18),(14,25),(24,25)), ((34,25),(34,18),(40,18)))
        self.add_bezier("casing-right", (40,18), ((43,18),(44,21),(44,24)), ((44,30),(33,38),(24,38)))
        self.add_bezier("casing-left", (24,38), ((15,38),(4,30),(4,24)), ((4,21),(5,18),(8,18)))
        self.add_contour("casing", "casing-top", "casing-right", "casing-left", closed=True)
        for side in (-1,1):
            x=lambda a:24+side*a
            name="tie-left" if side<0 else "tie-right"
            self.add_polyline(name,(x(20),12),(x(16),18),(x(14),10))
            self.relate("connect",name,"casing")
