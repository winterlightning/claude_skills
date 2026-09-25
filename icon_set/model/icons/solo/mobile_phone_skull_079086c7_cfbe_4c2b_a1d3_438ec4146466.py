"""mobile phone skull: complete SOLO48 repair.
Retained a frontal skull with rounded cranium, paired eye sockets and open lower jaw. Enlarged the sockets and merged their outlines into the cranium; removed the middle tooth and phone divider.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '079086c7-cfbe-4c2b-a1d3-438ec4146466'
SOURCE_PATH = 'pictographic-primitives/other/mobile phone skull_079086c7-cfbe-4c2b-a1d3-438ec4146466.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'mobile-phone-skull'
    keyshape = Keyshape.VRECT_L
    # Visible ink extrema: (6, 2, 42, 46).
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('mobile', 'phone', 'skull')


    def build(self):
        self.add_polyline('phone',(8,4),(40,4),(40,44),(8,44),closed=True)
        self.add_arc('cranium-left',(17,21),(24,13),radius_x=7,radius_y=8)
        self.add_arc('cranium-right',(24,13),(31,21),radius_x=7,radius_y=8)
        self.add_bezier('eye-right-base',(31,21),((31,25),(24,25),(24,21)))
        self.add_bezier('eye-left-base',(24,21),((24,25),(17,25),(17,21)))
        self.add_contour('cranium','cranium-left','cranium-right','eye-right-base','eye-left-base',closed=True)
        self.add_line('bridge',(24,13),(24,21))
        self.relate('connect','cranium','bridge')
        self.add_polyline('jaw-left',(17,21),(16,24),(16,28),(20,32),(20,34))
        self.add_polyline('jaw-right',(31,21),(32,24),(32,28),(28,32),(28,34))
        self.relate('connect','cranium','jaw-left')
        self.relate('connect','cranium','jaw-right')
