"""An empty wedding canopy with a triangular roof, a horizontal lintel, two slender posts and short ground feet. Retain the diagonal corner braces and exclude the hanging heart. Do not add draped curtains.

Plan: Triangular canopy with paired uprights, straight corner braces, and ground feet. Bounds (2,2)-(62,62).
Hosting at the standard slot: add-sub32: valid, heart-state-63: review, check-mark: valid.
Construction reference: Lucide tent: straight structural roof; source supplies curved braces and upright posts."""
from ...keyshapes import Keyshape
from ._base import Container64

SOURCE_ICON_ID = '14f3d7ad-90fa-56e6-bb5a-4e1cd8a1bf20'
SOURCE_PATH = 'pictographic-primitives/romance/wedding altar_14f3d7ad-90fa-56e6-bb5a-4e1cd8a1bf20.svg'
SOURCE_ICON_IDS = ('14f3d7ad-90fa-56e6-bb5a-4e1cd8a1bf20',)
AUTHOR = 'gpt-6'

class StraightCanopyArchContainer(Container64):
    icon_id = 'straight-canopy-arch-container'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'romance'
    aliases = ()
    keywords = ('straight', 'canopy', 'arch', 'container')

    def build(self) -> None:
        self.add_polyline('roof',(2,22),(32,2),(62,22),closed=True)
        for sign,name in ((1,'left'),(-1,'right')):
            x=32+sign*(6-32)
            self.add_line(name+'-post',(x,22),(x,62))
            self.add_line(name+'-foot',(x-4,62),(x+4,62))
            self.add_line(name+'-brace',(x,40),(32+sign*(22-32),22))
            self.relate('connect','roof',name+'-post')
            self.relate('connect','roof',name+'-brace')
            self.relate('connect',name+'-post',name+'-brace')
            self.relate('connect',name+'-post',name+'-foot')
