"""Broadened the drop with mirrored curved shoulders and an elliptical bowl; kept the open hook.

VRECT_L: visible ink (6, 2, 42, 46). Upright envelope accommodates the object’s vertical construction.
No useful exact local Lucide match; retained the inspected parent silhouette.
"""
# Independent revision; parent models preserved.
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'bdcf8f0c-b460-5564-8495-792c693562c8'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-05/earring_bdcf8f0c-b460-5564-8495-792c693562c8.svg'
AUTHOR = 'gpt-6'

class TeardropEarring(Solo48):
    icon_id = 'teardrop-earring'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/accessories'
    aliases = ()
    keywords = ('earring', 'teardrop', 'drop', 'hook', 'jewellery', 'jewelry', 'pendant', 'accessory')

    def build(self) -> None:
        # VRECT_L (8,4)-(40,44). Shared axis, circular hook and paired
        # smooth shoulders tangent to the lower elliptical bowl.
        x=24
        self.add_arc('hook',(18,10),(30,10),radius_x=6)
        self.add_arc('hook-return',(30,10),(x,16),radius_x=6)
        self.add_line('post',(x,16),(x,20))
        self.add_contour('earwire','hook','hook-return','post')
        self.add_bezier('drop-left',(x,20),((16,24),(8,28),(8,32)))
        self.add_arc('drop-bottom',(8,32),(40,32),radius_x=16,radius_y=12,sweep=False)
        self.add_bezier('drop-right',(40,32),((40,28),(32,24),(x,20)))
        self.add_contour('pendant','drop-left','drop-bottom','drop-right',closed=True)
        self.relate('connect','earwire','pendant')
