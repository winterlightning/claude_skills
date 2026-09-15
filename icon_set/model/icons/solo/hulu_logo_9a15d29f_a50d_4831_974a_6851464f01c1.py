"""The lowercase wordmark hulu in rounded geometric letters of equal height.

Plan: Two rows hu then lu, shared bowls with radius 6.
Keyshape: SQUARE; exact SOLO48 envelope from the contract.
Construction reference: No useful single-letter Lucide match; geometric stems and circular bowls.
Simplification: Wordmark arranged as hu / lu to preserve all four letters.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9a15d29f-a50d-4831-974a-6851464f01c1'
SOURCE_PATH = 'pictographic-primitives/logos/hulu live tv logo_9a15d29f-a50d-4831-974a-6851464f01c1.svg'
AUTHOR = 'gpt-6'


class HuluLogo(Solo48):
    icon_id = 'hulu-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    aliases = ()
    keywords = ('hulu', 'streaming', 'tv', 'wordmark', 'logo', 'brand', 'video')

    def build(self):
        self.add_line('hupper',(6,6),(6,14))
        self.add_line('hlower',(6,14),(6,20))
        self.add_contour('hstem','hupper','hlower')
        self.add_arc('harch',(6,14),(18,14),radius_x=6)
        self.add_line('hleg',(18,14),(18,20))
        self.add_contour('hbow','harch','hleg')
        self.relate('connect','hstem','hbow')
        for name,y in [('u1',14),('u2',36)]:
         self.add_line(name+'left',(30,y-4),(30,y))
         self.add_arc(name+'curve',(30,y),(42,y),radius_x=6,sweep=False)
         self.add_line(name+'right',(42,y),(42,y-4))
         self.add_contour(name,name+'left',name+'curve',name+'right')
        self.add_line('l',(12,29),(12,42))
