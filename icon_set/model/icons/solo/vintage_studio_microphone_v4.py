"""Widened the foot and capsule; replaced three crowded grille rows with two equally spaced rows.

VRECT_L: visible ink (6, 2, 42, 46). Upright envelope accommodates the object’s vertical construction.
Lucide mic: tangent capsule corners and shared stand attachment.
"""
# Independent revision; parent models preserved.
from __future__ import annotations
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = None
SOURCE_PATH = 'icon_set/model/icons/solo/vintage_studio_microphone.py'
AUTHOR = 'gpt-6'

class VintageStudioMicrophoneVariant4(Solo48):
    icon_id = 'vintage-studio-microphone-v4'
    variant_of = 'vintage-studio-microphone'
    variant_label = 'Exact keyshape envelope and clear spacing'
    keyshape = Keyshape.VRECT_L
    category = 'objects/media'
    aliases = ('vintage-microphone', 'studio-microphone', 'broadcast-microphone')
    keywords = ('microphone', 'mic', 'podcast', 'audio', 'recording', 'broadcast', 'voice', 'studio', 'radio')

    def build(self) -> None:
        # VRECT_L (8,4)-(40,44). Capsule and broad foot share x=24.
        # Two grille rows replace three crowded rows; paired half-bars repeat.
        cx,left,right=24,14,34
        self.add_arc('nw',(left,14),(cx,4),radius_x=10)
        self.add_arc('ne',(cx,4),(right,14),radius_x=10)
        self.add_line('right',(right,14),(right,22))
        self.add_arc('se',(right,22),(cx,32),radius_x=10)
        self.add_arc('sw',(cx,32),(left,22),radius_x=10)
        self.add_line('left',(left,22),(left,14))
        self.add_contour('capsule','nw','ne','right','se','sw','left',closed=True)
        for y in (14,22):
            for side,a,b in [('left',left,20),('right',28,right)]:
                name=f'grille-{side}-{y}'
                self.add_line(name,(a,y),(b,y))
                self.relate('connect','capsule',name)
        self.add_line('stem',(cx,32),(cx,44))
        self.add_polyline('base',(8,44),(cx,44),(40,44))
        self.relate('connect','capsule','stem')
        self.relate('connect','stem','base')
