"""A six-blade camera aperture. CIRCLE radius20 centerline, ink radius22. Lucide aperture informs the segmented circular rim and six intersecting straight blades. Use opposed integer-grid blade pairs and enlarge the central opening."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0cb953cf-9714-40a8-af67-7ea79c576259'
SOURCE_PATH = 'pictographic-primitives/symbol/lens shutter_0cb953cf-9714-40a8-af67-7ea79c576259.svg'
AUTHOR = 'gpt-6'


class ApertureShutter(Solo48):
    icon_id = 'aperture-shutter'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/symbols"
    aliases = ()
    keywords = ('aperture', 'shutter', 'camera', 'lens', 'photography', 'iris', 'focus', 'photo')

    def build(self) -> None:
        rim=[(40,12),(40,36),(24,42),(8,36),(8,12),(24,6)]
        for i,p in enumerate(rim):
            self.add_arc(f'rim-{i}',p,rim[(i+1)%6],radius_x=20)
        self.add_contour('rim',*(f'rim-{i}' for i in range(6)),closed=True)
        blades=[[(40,12),(28,12),(20,12)],[(40,36),(34,24),(28,12)],[(24,42),(28,36),(34,24)],[(8,36),(20,36),(28,36)],[(8,12),(14,24),(20,36)],[(24,6),(20,12),(14,24)]]
        for i,points in enumerate(blades):
            self.add_polyline(f'blade-{i}',*points)
            self.relate('connect','rim',f'blade-{i}')
        for i in range(6):
            self.relate('connect',f'blade-{i}',f'blade-{(i+1)%6}')
