'Droplet: mirrored smooth shoulders and a tangent-continuous round bowl, preserving the pointed tip and curved highlight.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6eeb8b64-353f-4d55-afc4-cee5edb7104e'
SOURCE_PATH = 'pictographic-primitives/smileys/drop_6eeb8b64-353f-4d55-afc4-cee5edb7104e.svg'
AUTHOR = 'gpt-6'

class DropSmileys(Solo48):
    icon_id = 'drop-smileys'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    categories = ('smileys', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('drop', 'smileys')

    def build(self) -> None:
        # Lucide droplet: continuous rounded bowl; retain the deliberate pointed apex.
        # VRECT_L centerline extremes (8,4)-(40,44).
        self.add_bezier('left',(24,4),((18,11),(8,21),(8,28)))
        self.add_bezier('bowl-left',(8,28),((8,37),(15,44),(24,44)))
        self.add_bezier('bowl-right',(24,44),((33,44),(40,37),(40,28)))
        self.add_bezier('right',(40,28),((40,21),(30,11),(24,4)))
        self.add_contour('outline','left','bowl-left','bowl-right','right',closed=True)
        self.add_arc('highlight',(24,34),(30,28),radius_x=6,sweep=False)
