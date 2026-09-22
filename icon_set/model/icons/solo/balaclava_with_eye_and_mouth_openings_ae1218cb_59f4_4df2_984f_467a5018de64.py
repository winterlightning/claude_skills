"""Balaclava garment with broad eye aperture, small mouth hole and flared hem.
VRECT_L fits the tall hood. Mirror about x24; paired crown radii10 and eye radii4.
Crown/hem form one outline, openings are child loops. Eye pinch is simplified
into a capsule; mouth is circular to preserve a measurable small opening.
Source establishes garment silhouette; no local Lucide balaclava match.
"""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = "ae1218cb-59f4-4df2-984f-467a5018de64"
SOURCE_PATH = "pictographic-primitives/_uncategorized_05/balaclava_ae1218cb-59f4-4df2-984f-467a5018de64.svg"
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id = "balaclava-with-eye-and-mouth-openings"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "Uncategorized"
    aliases = ["Balaclava Face Mask"]
    keywords = ["balaclava", "mask", "hood", "eyes", "mouth", "clothing", "headwear"]
    def build(self):
        axis=24
        self.add_line("crown",(18,4),(2*axis-18,4))
        self.add_arc("crown-right",(30,4),(40,14),radius_x=10)
        self.add_line("side-right",(40,14),(40,28))
        self.add_bezier("neck-right",(40,28),((40,33),(36,35),(38,38)),((39,39),(40,40),(40,40)))
        self.add_bezier("hem-right",(40,40),((36,44),(28,44),(24,44)))
        self.add_bezier("hem-left",(24,44),((20,44),(12,44),(8,40)))
        self.add_bezier("neck-left",(8,40),((8,40),(9,39),(10,38)),((12,35),(8,33),(8,28)))
        self.add_line("side-left",(8,28),(8,14))
        self.add_arc("crown-left",(8,14),(18,4),radius_x=10)
        self.add_contour("hood","crown","crown-right","side-right","neck-right","hem-right","hem-left","neck-left","side-left","crown-left",closed=True)
        self.add_line("eyes-top",(21,13),(27,13))
        self.add_arc("eyes-right",(27,13),(27,21),radius_x=4)
        self.add_line("eyes-bottom",(27,21),(21,21))
        self.add_arc("eyes-left",(21,21),(21,13),radius_x=4)
        self.add_contour("eyes","eyes-top","eyes-right","eyes-bottom","eyes-left",closed=True)
        self.add_arc("mouth-bottom",(21,32),(27,32),radius_x=3,sweep=False)
        self.add_arc("mouth-top",(27,32),(21,32),radius_x=3,sweep=False)
        self.add_contour("mouth","mouth-bottom","mouth-top",closed=True)
