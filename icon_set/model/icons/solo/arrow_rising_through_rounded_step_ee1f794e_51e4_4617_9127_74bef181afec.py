"""Arrow Rising Through Rounded Step. Wide envelope; continuous rounded step owns two equal six-unit quarter-circle bends with exact tangent joins. Shared right-pointing tip; no identity-carrying details omitted.
Reference supplies silhouette and direction; Lucide arrow-up-right supplies
shared shaft/head junction construction. Rebuilt on SOLO48; no traced coordinates.
"""
from ._base import Solo48
from ...keyshapes import Keyshape

SOURCE_ICON_ID = 'ee1f794e-51e4-4617-9127-74bef181afec'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_14/diagram dash up steady_ee1f794e-51e4-4617-9127-74bef181afec.svg'
AUTHOR = "gpt-6-astra"

class Drawing(Solo48):
    icon_id = 'arrow-rising-through-rounded-step'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ('Stepped Upward Right Arrow',)
    keywords = ('arrow', 'step', 'rise', 'right', 'curve', 'path', 'direction')

    def build(self):
        radius=6
        self.add_line('base',(4,40),(14,40))
        self.add_arc('lower-bend',(14,40),(20,34),radius_x=radius,sweep=False)
        self.add_line('rise',(20,34),(20,22))
        self.add_arc('upper-bend',(20,22),(26,16),radius_x=radius,sweep=True)
        tip=(44,16)
        self.add_line('terminal',(26,16),tip)
        self.add_contour('shaft','base','lower-bend','rise','upper-bend','terminal')
        self.add_polyline('head',(36,8),tip,(36,24))
        self.relate('connect','shaft','head')
