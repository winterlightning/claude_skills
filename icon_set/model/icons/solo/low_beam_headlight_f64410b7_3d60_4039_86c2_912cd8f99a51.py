"""A D-shaped headlamp with two horizontal light rays; broad keyshape preserves the source direction. No useful exact Lucide match; a semicircular lens preserves the source, with no extra detail."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f64410b7-3d60-4039-86c2-912cd8f99a51'
SOURCE_PATH = 'pictographic-primitives/transportation/car dashboard lights_f64410b7-3d60-4039-86c2-912cd8f99a51.svg'
SOURCE_REFERENCES = (('f64410b7-3d60-4039-86c2-912cd8f99a51', 'pictographic-primitives/transportation/car dashboard lights_f64410b7-3d60-4039-86c2-912cd8f99a51.svg'),)
AUTHOR = 'gpt-6'

class LowBeamHeadlight(Solo48):
    icon_id = 'low-beam-headlight'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('headlight', 'low beam', 'dipped beam', 'lamp', 'car', 'dashboard', 'lighting', 'indicator')

    def build(self) -> None:
        self.add_line('flat',(28,8),(28,40))
        self.add_arc('lens',(28,40),(28,8),radius_x=16,sweep=False)
        self.add_contour('lamp','flat','lens',closed=True)
        for y in (16,32):
            self.add_line(f'beam-{y}',(4,y),(18,y))
