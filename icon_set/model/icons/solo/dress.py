"""Widened both straps, inset the hem, and retained the scoop neck and flared skirt.

Keyshape VRECT_L: visible bounds (6, 2, 42, 46).
Reference: No useful exact match.
"""
# Independent repair of dress; parent preserved.
from __future__ import annotations
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = None
SOURCE_PATH = 'icon_set/model/icons/solo/dress.py'
AUTHOR = 'gpt-6'

class Dress(Solo48):
    icon_id = 'dress'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/clothing'
    aliases = ('sleeveless-dress', 'a-line-dress', 'sleeveless-woman-dress')
    keywords = ('dress', 'clothing', 'fashion', 'garment', 'apparel', 'womenswear', 'skirt', 'sleeveless')

    def build(self) -> None:
        # VRECT_L centerlines (8,4)-(40,44). Shared axis, eight-unit straps,
        # coherent scoop, fitted waist and two straight flared skirt sides.
        axis = 24
        self.add_polyline('left-strap',(12,14),(12,4),(20,4),(20,10))
        self.add_arc('neck',(20,10),(28,10),radius_x=4,sweep=False)
        self.add_polyline('right-strap',(28,10),(28,4),(36,4),(36,14))
        self.add_polyline('right-body',(36,14),(31,24),(40,42))
        self.add_arc('hem',(40,42),(8,42),radius_x=16,radius_y=2)
        self.add_polyline('left-body',(8,42),(17,24),(12,14))
        members = tuple(member for contour in self.contours for member in contour.members)
        self.contours.clear()
        self.add_contour('outline', *members[:3], 'neck', *members[3:8], 'hem', *members[8:], closed=True)
        self.add_line('waist',(17,24),(31,24))
        self.relate('connect','outline','waist')
