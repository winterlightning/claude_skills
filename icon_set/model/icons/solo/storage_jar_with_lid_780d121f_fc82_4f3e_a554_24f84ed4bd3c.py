"""A rounded storage body under a broad lid and raised rear handle.

SQUARE extrema (6,6)-(42,42). The wide bar and centered raised tab are
separate attached symbols. Lucide archive informs the lid/body construction;
the shallow front curve comes from the source.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "780d121f-fc82-4f3e-a554-24f84ed4bd3c"
SOURCE_PATH = "pictographic-primitives/_uncategorized_12/content typing machine 2_780d121f-fc82-4f3e-a554-24f84ed4bd3c.svg"
AUTHOR = "gpt-6"


class StorageJarWithLid(Solo48):
    icon_id = "storage-jar-with-lid"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/storage"
    aliases = ("lidded jar", "typewriter-like container")
    keywords = ("lid", "wide bar", "rounded body", "front opening")

    def build(self) -> None:
        self.add_line("rear-left",(12,16),(12,10))
        self.add_arc("rear-nw",(12,10),(16,6),radius_x=4,radius_y=4,sweep=True)
        self.add_line("rear-top",(16,6),(32,6))
        self.add_arc("rear-ne",(32,6),(36,10),radius_x=4,radius_y=4,sweep=True)
        self.add_line("rear-right",(36,10),(36,16))
        self.add_contour("raised-tab","rear-left","rear-nw","rear-top","rear-ne","rear-right")
        self.add_polyline("lid",(6,16),(42,16),(42,24),(6,24),closed=True)
        self.add_line("body-left",(8,24),(8,38))
        self.add_arc("body-sw",(8,38),(12,42),radius_x=4,radius_y=4,sweep=False)
        self.add_line("body-bottom",(12,42),(36,42))
        self.add_arc("body-se",(36,42),(40,38),radius_x=4,radius_y=4,sweep=False)
        self.add_line("body-right",(40,38),(40,24))
        self.add_contour("body","body-left","body-sw","body-bottom","body-se","body-right")
        self.add_bezier("front-curve",(17,33),((20,34),(28,34),(31,33)))
        self.relate("connect","raised-tab","lid")
        self.relate("connect","body","lid")
