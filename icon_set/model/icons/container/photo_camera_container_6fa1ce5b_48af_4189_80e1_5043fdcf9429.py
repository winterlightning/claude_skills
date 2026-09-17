"""Digital Photo Camera: independently authored container.

Construction plan: Rounded body, raised central top and circular lens; preserve the lens as intrinsic detail.
Keyshape HRECT_XL; extremes are the profile's exact keyshape bounds.
Reference: pictographic-primitives/photography/camera_6fa1ce5b-48af-4189-80e1-5043fdcf9429.svg. Lucide camera original and atomic-debug inspected.
No source coordinates or solo geometry were scaled. Native size is 64.

Visible keyshape extremes: (0, 4, 64, 60).
Hosting measured with compose.py: plus does not clear, heart does not clear, check does not clear.
"""
from ...keyshapes import Keyshape
from ._base import Container64
from ._construction import path, rounded_rect as rect, ellipse

SOURCE_ICON_ID = '6fa1ce5b-48af-4189-80e1-5043fdcf9429'
SOURCE_PATH = 'pictographic-primitives/photography/camera_6fa1ce5b-48af-4189-80e1-5043fdcf9429.svg'
AUTHOR = 'gpt-6'


class PhotoCameraContainer(Container64):
    icon_id = 'photo-camera-container'
    keyshape = Keyshape.HRECT_XL
    aliases = ()
    keywords = ('photo', 'camera', 'container')

    def build(self):
        line, poly = self.add_line, self.add_polyline
        def join(a,b): self.relate('connect',a,b)
        path(self,'body',(8,16),[('L',(18,16)),('L',(24,6)),('L',(40,6)),('L',(46,16)),('L',(56,16)),('A',(62,22),6,6,True),('L',(62,52)),('A',(56,58),6,6,True),('L',(8,58)),('A',(2,52),6,6,True),('L',(2,22)),('A',(8,16),6,6,True)],True)
        ellipse(self,'lens',32,36,14)
