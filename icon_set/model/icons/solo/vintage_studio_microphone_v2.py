# Variant of vintage-studio-microphone; parent file remains unchanged.
"""Retro studio microphone with one split grille row. VRECT_S retains the narrow capsule and stand; top and bottom grille pairs removed."""
from __future__ import annotations
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = None
SOURCE_PATH = None
AUTHOR = 'gpt-6'

class VintageStudioMicrophoneVariant2(Solo48):
    """A rounded broadcast microphone capsule on a stem and flat base."""
    icon_id = 'vintage-studio-microphone-v2'
    variant_of = 'vintage-studio-microphone'
    variant_label = 'Reduced grille'
    keyshape = Keyshape.VRECT_S
    category = 'objects/media'
    aliases = ('vintage-microphone', 'studio-microphone', 'broadcast-microphone')
    keywords = ('microphone', 'mic', 'podcast', 'audio', 'recording', 'broadcast', 'voice', 'studio', 'radio')

    def build(self) -> None:
        self.add_arc('capsule-top-left', (16, 10), (24, 2), radius_x=8)
        self.add_arc('capsule-top-right', (24, 2), (32, 10), radius_x=8)
        self.add_line('capsule-right-upper', (32, 10), (32, 16))
        self.add_line('capsule-right-lower', (32, 16), (32, 22))
        self.add_arc('capsule-bottom-right', (32, 22), (24, 30), radius_x=8)
        self.add_arc('capsule-bottom-left', (24, 30), (16, 22), radius_x=8)
        self.add_line('capsule-left-lower', (16, 22), (16, 16))
        self.add_line('capsule-left-upper', (16, 16), (16, 10))
        self.add_contour('capsule', 'capsule-top-left', 'capsule-top-right', 'capsule-right-upper', 'capsule-right-lower', 'capsule-bottom-right', 'capsule-bottom-left', 'capsule-left-lower', 'capsule-left-upper', closed=True)
        for row, y in (('middle', 16),):
            left = f'grille-{row}-left'
            right = f'grille-{row}-right'
            self.add_line(left, (16, y), (20, y))
            self.add_line(right, (28, y), (32, y))
            self.relate('connect', 'capsule', left)
            self.relate('connect', 'capsule', right)
        self.add_line('stem', (24, 30), (24, 46))
        self.add_line('base-left', (14, 46), (24, 46))
        self.add_line('base-right', (24, 46), (34, 46))
        self.add_contour('base', 'base-left', 'base-right')
        self.relate('connect', 'capsule', 'stem')
        self.relate('connect', 'stem', 'base')
