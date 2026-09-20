"""Diagonal paper airplane.

Construction reference: send.
Omitted tiny lower flap to keep the two principal wings legible.
SOLO48 explicitly requested for this source main by the user.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._side_main50_geometry import box, circle, path

SOURCE_ICON_ID = '4f05b839-b3a3-4cf1-805a-ced56d04a370'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_29/paper plane_4f05b839-b3a3-4cf1-805a-ced56d04a370.svg'
AUTHOR = 'gpt-6'


class SourceMain(Solo48):
    icon_id = 'diagonal-paper-airplane-solo-4f05b839'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ('diagonal-paper-airplane',)
    keywords = ('diagonal', 'paper', 'airplane')

    def build(self):
        # Two wings share the central fold; the diagonal points intentionally northeast.
        self.add_polyline('wings',(6,24),(42,6),(30,42),(20,32),(6,24),closed=True)
        self.add_line('fold',(20,32),(42,6))
        self.relate('connect','wings','fold')
