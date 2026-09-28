"""A diagonal telephone handset with two curved ringing arcs above/right. Retain both arcs and the full handset as one call symbol.

Plan: Diagonal handset with two separated quarter-circle signal arcs. Bounds (2,2)-(30,30).
Construction reference: Lucide phone-call: coherent bent handset and two spaced quarter-circle ringing arcs."""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '75f76bb5-f6c5-4feb-80ea-54e38ec9dbe4'
SOURCE_PATH = 'pictographic-primitives/state/phone with electric waves_75f76bb5-f6c5-4feb-80ea-54e38ec9dbe4.svg'
SOURCE_ICON_IDS = ('75f76bb5-f6c5-4feb-80ea-54e38ec9dbe4',)
AUTHOR = 'gpt-6'

class RingingTelephoneHandsetSub(Sub32):
    icon_id = 'ringing-telephone-handset-sub'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    categories = ('state',)
    aliases = ()
    keywords = ('ringing', 'telephone', 'handset', 'sub')

    def build(self) -> None:
        self.add_polyline('ear',(2,6),(6,2),(12,8),(8,12))
        self.add_bezier('inside',(8,12),((10,17),(15,22),(20,24)))
        self.add_polyline('mouth',(20,24),(24,20),(30,26),(26,30))
        self.add_bezier('outside',(26,30),((8,30),(2,24),(2,6)))
        self.add_contour('handset',*[f'ear-{i}' for i in range(1,4)],'inside',*[f'mouth-{i}' for i in range(1,4)],'outside',closed=True)
        self.contours=[c for c in self.contours if c.contour_id not in ('ear','mouth')]
        self.add_arc('ring-outer',(18,2),(30,14),radius_x=12)
        self.add_arc('ring-inner',(18,9),(23,14),radius_x=5)
