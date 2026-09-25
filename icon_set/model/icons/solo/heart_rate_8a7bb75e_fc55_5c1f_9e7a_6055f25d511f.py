"""A heart outline crossed by a pulse waveform.
Symbol plan and construction: heart-pulse: paired heart lobes and a coherent cardiograph stroke.
Keyshape: SQUARE provides room below the pulse for the heart point.
Omissions: None.
Review: The waveform trough and rising right segment were moved inward to avoid following the lower heart wall too closely. Outline is mirrored; pulse is intentionally asymmetric."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '8a7bb75e-fc55-5c1f-9e7a-6055f25d511f'
SOURCE_PATH = 'pictographic-primitives/health/heart rate_8a7bb75e-fc55-5c1f-9e7a-6055f25d511f.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'heart-rate'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    aliases = ()
    keywords = ('heart rate',)



    def heart(self):
        # Paired nine-unit lobes and mirrored lower shoulders.
        self.add_arc('left-lobe',(24,15),(6,15),radius_x=9,sweep=False)
        self.add_arc('left-shoulder',(6,15),(10,27),radius_x=20,sweep=False)
        self.add_line('point-1',(10,27),(24,42))
        self.add_line('point-2',(24,42),(38,27))
        self.add_arc('right-shoulder',(38,27),(42,15),radius_x=20,sweep=False)
        self.add_arc('right-lobe',(42,15),(24,15),radius_x=9,sweep=False)
        self.add_contour('heart','left-lobe','left-shoulder','point-1','point-2','right-shoulder','right-lobe',closed=True)

    def build(self):
        # Heart outline and one coherent cardiograph stroke joining both sides.
        self.heart()
        self.add_polyline('pulse',(10,27),(16,27),(20,18),(24,30),(28,25),(38,27))
        self.relate('connect','heart','pulse')
