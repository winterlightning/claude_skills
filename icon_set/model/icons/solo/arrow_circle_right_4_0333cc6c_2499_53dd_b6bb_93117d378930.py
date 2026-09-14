"""Use an exact circle, straight attached shaft, and mirrored arrowhead. User explicitly authorized the complete framed icon. Lucide construction: straight runs, mirrored chevrons, tangent equal-radius corners."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '0333cc6c-2499-53dd-b6bb-93117d378930'
SOURCE_PATH = 'icons-json/arrows/arrow circle right 4_0333cc6c-2499-53dd-b6bb-93117d378930.json'
AUTHOR = 'gpt-6'

class ArrowCircleRight4(Solo48):
    icon_id = 'arrow-circle-right-4'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'circle', 'right', 'arrows')

    def build(self):
        center, radius = (24, 20)
        left, top, right, bottom = ((center - radius, center), (center, center - radius), (center + radius, center), (center, center + radius))
        for name, a, b in [('top-left', left, top), ('top-right', top, right), ('bottom-right', right, bottom), ('bottom-left', bottom, left)]:
            self.add_arc(name, a, b, radius_x=radius, sweep=True)
        self.add_contour('ring', 'top-left', 'top-right', 'bottom-right', 'bottom-left', closed=True)
        tip = (34, center)
        self.add_line('shaft', left, tip)
        self.add_line('head-top', (26, center - 8), tip)
        self.add_line('head-bottom', tip, (26, center + 8))
        self.add_contour('head', 'head-top', 'head-bottom')
        self.relate('connect', 'ring', 'shaft')
        self.relate('connect', 'shaft', 'head')
