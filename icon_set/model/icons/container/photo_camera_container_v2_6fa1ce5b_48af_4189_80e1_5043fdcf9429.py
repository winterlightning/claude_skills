"""Enlarge the lens and camera body while preserving the raised top housing.
Construction: shared body/attachment coordinates, integer grid, 4-unit stroke.
Lucide originals and atomic-debug references inspected for enclosure, handle and rounded-join construction.
"""
from ...keyshapes import Keyshape
from ._base import Container64
from ._construction import path, rounded_rect as rect, ellipse
SOURCE_ICON_ID = '6fa1ce5b-48af-4189-80e1-5043fdcf9429'
SOURCE_PATH = 'pictographic-primitives/photography/camera_6fa1ce5b-48af-4189-80e1-5043fdcf9429.svg'
AUTHOR = 'gpt-6'

class PhotoCameraContainerVariant2(Container64):
    icon_id = 'photo-camera-container-v2'
    variant_of = 'photo-camera-container'
    variant_label = "Room for native 32-unit sub-icons"
    keyshape = Keyshape.SQUARE
    aliases = ()
    keywords = ()

    def build(self):
        line, poly = self.add_line, self.add_polyline
        def join(a,b): self.relate("connect",a,b)
        path(self,'body',(8,6),[('L',(18,6)),('L',(24,2)),('L',(40,2)),('L',(46,6)),('L',(56,6)),('A',(62,12),6,6,True),('L',(62,56)),('A',(56,62),6,6,True),('L',(8,62)),('A',(2,56),6,6,True),('L',(2,12)),('A',(8,6),6,6,True)],True)
        ellipse(self,'lens',32,34,21)
