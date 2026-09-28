"""Longship with a curved sail and three oars.
Square envelope (6,6)-(42,42). Sail and hull own continuous contours;
three oars repeat at 12-unit horizontal intervals. Lucide sailboat informs
closed hull contour and mast attachment, source provides curved sail and oars.
"""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = "a795a20f-a600-407a-afe4-25fbc99203fd"
SOURCE_PATH = "pictographic-primitives/_uncategorized_26/longboat_a795a20f-a600-407a-afe4-25fbc99203fd.svg"
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id = "longship-with-curved-sail-and-three-oars"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ("Viking Longship with Sail and Oars",)
    keywords = ("longship", "ship", "sail", "oars", "hull", "boat", "viking")
    def build(self):
        self.add_line("sail-top",(14,6),(32,6))
        self.add_bezier("sail-right",(32,6),((38,10),(38,14),(32,18)))
        self.add_line("sail-bottom-r",(32,18),(24,18))
        self.add_line("sail-bottom-l",(24,18),(14,18))
        self.add_bezier("sail-left",(14,18),((18,14),(18,10),(14,6)))
        self.add_contour("sail","sail-top","sail-right","sail-bottom-r","sail-bottom-l","sail-left",closed=True)
        self.add_line("mast",(24,18),(24,26))
        self.relate("connect","mast","sail-bottom-r","sail-bottom-l")
        self.add_line("rim-1",(6,26),(24,26))
        self.add_line("rim-2",(24,26),(42,26))
        self.relate("connect","mast","rim-1","rim-2")
        self.add_bezier("hull-right",(42,26),((42,32),(40,34),(36,34)))
        self.add_line("base-r",(36,34),(24,34))
        self.add_line("base-l",(24,34),(12,34))
        self.add_bezier("hull-left",(12,34),((8,34),(6,32),(6,26)))
        self.add_contour("hull","rim-1","rim-2","hull-right","base-r","base-l","hull-left",closed=True)
        for i,x in enumerate((12,24,36)):
            self.add_line(f"oar-{i}",(x,34),(x-6,42))
        self.relate("connect","oar-0","base-l","hull-left")
        self.relate("connect","oar-1","base-l","base-r")
        self.relate("connect","oar-2","base-r","hull-right")
