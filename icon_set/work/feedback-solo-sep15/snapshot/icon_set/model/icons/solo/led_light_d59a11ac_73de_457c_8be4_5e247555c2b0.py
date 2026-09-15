"""led-light: geometric reconstruction on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd59a11ac-73de-457c-8be4-5e247555c2b0'
SOURCE_PATH = 'pictographic-primitives/electronics/led light_d59a11ac-73de-457c-8be4-5e247555c2b0.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class LedLight(Solo48):
    icon_id = 'led-light'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'electronics'
    aliases = ()
    keywords = ('led', 'light', 'electronics')

    def build(self):
        # Plan: VRECT_L; one semicircular dome, paired leads, and shared filament junction.
        # Reference: Geometric capsule construction.
        self.add_line('left-wall',(10,28),(10,18))
        self.add_arc('dome',(10,18),(38,18),radius_x=14)
        self.add_line('right-wall',(38,18),(38,28))
        self.add_contour('housing','left-wall','dome','right-wall')
        self.add_line('flange',(8,28),(40,28))
        self.relate('connect','housing','flange')
        for name,x in [('left',17),('right',31)]:
            self.add_line(name+'-lead',(x,28),(x,44))
            self.relate('connect',name+'-lead','flange')
        self.add_polyline('filament',(20,18),(24,20),(28,18))
        self.add_line('filament-stem',(24,20),(24,28))
        self.relate('connect','filament-stem','filament')
        self.relate('connect','filament-stem','flange')
