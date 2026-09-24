"""A browser page containing a skull.
Symbol plan and construction: app-window and skull: browser header, curved cranium and narrowed open jaw.
Keyshape: SQUARE preserves the full page and centered skull.
Omissions: Middle tooth removed; cranium, eye pair and jaw retained.
Review: Blocked: skull/frame gap is 6 and eye/skull gaps are 5.52732, below 8. Skull remains crowded at native size. Human reference user.svg checked for head vocabulary; no detached head/body pair applies."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID='9ab7c5fa-7d54-4c5c-8f9e-b01743e34909'
SOURCE_PATH = 'pictographic-primitives/other/ui webpage skull_9ab7c5fa-7d54-4c5c-8f9e-b01743e34909.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='ui-webpage-skull'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/general"
    aliases=()
    keywords=('ui', 'webpage', 'skull')






    def build(self):
        self.add_polyline('browser',(6,14),(6,6),(42,6),(42,14),(42,42),(6,42),closed=True)
        self.add_line('chrome',(6,14),(42,14));self.relate('connect','browser','chrome')
        self.add_arc('skull-top',(14,30),(34,30),radius_x=10)
        self.add_bezier('skull-right',(34,30),((34,34),(29,34),(29,36)))
        self.add_bezier('skull-left',(19,36),((19,34),(14,34),(14,30)))
        self.add_contour('skull','skull-left','skull-top','skull-right')
        for x in (20,28):self.add_dot(f'eye-{x}',(x,28))
