# Variant of vintage-studio-microphone; parent file remains unchanged.
'Vintage studio microphone: independent spacing revision.\n\nTwo grille rows at eight-unit spacing replace three crowded rows; enlarge capsule and foot.\nNative solo family, VRECT_S keyshape. The original model is preserved.\nDirectional and natural asymmetry follows the supplied subject.\nFinal construction review: mic: rounded capsule and a simple stem. Local Lucide originals and atomic-debug renders were inspected.\n'
from __future__ import annotations
from ...keyshapes import Keyshape
from ._base import Solo48
AUTHOR = 'gpt-6'

class VintageStudioMicrophoneVariant3(Solo48):
    """A rounded broadcast microphone capsule on a stem and flat base."""
    icon_id = 'vintage-studio-microphone-v3'
    variant_of = 'vintage-studio-microphone'
    variant_label = 'Roomier spacing — remaining review'
    keyshape = Keyshape.VRECT_S
    category = 'objects/media'
    aliases = ('vintage-microphone', 'studio-microphone', 'broadcast-microphone')
    keywords = ('microphone', 'mic', 'podcast', 'audio', 'recording', 'broadcast', 'voice', 'studio', 'radio')

    def build(self):
        self.add_arc('top-left',(12, 16),(24, 4),radius_x=12,radius_y=12,sweep=True)
        self.add_arc('top-right',(24, 4),(36, 16),radius_x=12,radius_y=12,sweep=True)
        self.add_line('right',(36, 16),(36, 24))
        self.add_arc('bottom-right',(36, 24),(24, 36),radius_x=12,radius_y=12,sweep=True)
        self.add_arc('bottom-left',(24, 36),(12, 24),radius_x=12,radius_y=12,sweep=True)
        self.add_line('left',(12, 24),(12, 16))
        self.add_contour('capsule','top-left','top-right','right','bottom-right','bottom-left','left',closed=True)
        self.add_line('grille-top-left',(12, 16),(20, 16))
        self.add_line('grille-top-right',(28, 16),(36, 16))
        self.add_line('grille-bottom-left',(12, 24),(20, 24))
        self.add_line('grille-bottom-right',(28, 24),(36, 24))
        self.relate('connect','capsule','grille-top-left')
        self.relate('connect','capsule','grille-top-right')
        self.relate('connect','capsule','grille-bottom-left')
        self.relate('connect','capsule','grille-bottom-right')
        self.add_line('stem',(24, 36),(24, 44))
        self.add_polyline('base',(8, 44),(24, 44),(40, 44),closed=False)
        self.relate('connect','capsule','stem')
        self.relate('connect','stem','base')

SOURCE_ICON_ID = None

SOURCE_PATH = None
