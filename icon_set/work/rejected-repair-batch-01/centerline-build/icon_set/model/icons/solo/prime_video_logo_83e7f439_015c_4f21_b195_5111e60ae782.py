"""Video play mark above the Amazon smile-arrow. Use the app-symbol interpretation because five wordmark letters cannot fit at this stroke and clearance; omit prime text."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '83e7f439-015c-4f21-b195-5111e60ae782'
SOURCE_PATH = 'pictographic-primitives/logos/prime video logo_83e7f439-015c-4f21-b195-5111e60ae782.svg'
AUTHOR = 'gpt-6'

class PrimeVideoLogo(Solo48):
    icon_id = 'prime-video-logo'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'brands/logos'
    aliases = ()
    keywords = ('prime-video', 'amazon', 'streaming', 'wordmark', 'logo', 'brand', 'video')

    def build(self):
        # Plan: Video play mark above the Amazon smile-arrow. Use the app-symbol interpretation because five wordmark letters cannot fit at this stroke and clearance; omit prime text.
        # Exact keyshape ink extremes are owned by Keyshape.HRECT_L on SOLO48.

        self.add_polyline('play',(18,8),(32,16),(18,24),closed=True)
        self.add_bezier('smile',(4,31),((14,43),(31,43),(44,31)))
        self.add_polyline('arrow',(34,30),(44,31),(42,40))
        self.relate('connect','smile','arrow')

