'Droplet: mirrored smooth shoulders and a tangent-continuous round bowl, preserving the pointed tip and curved highlight.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a1bd3645-c186-44d1-a3a2-2ec8e3d10a1b'
SOURCE_PATH = 'icons-json/smileys/drop_a1bd3645-c186-44d1-a3a2-2ec8e3d10a1b.json'
AUTHOR = 'gpt-6'

class DropA1bd3645(Solo48):
    icon_id = 'drop-a1bd3645'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
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
