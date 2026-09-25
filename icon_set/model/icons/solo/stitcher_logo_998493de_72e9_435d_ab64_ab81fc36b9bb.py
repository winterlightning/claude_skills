"""Segmented horizontal body with one full-height separator and a short trailing bar. Preserve the two left partitions as real shared wall junctions; omit the narrow right slot."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '998493de-72e9-435d-ab64-ab81fc36b9bb'
SOURCE_PATH = 'pictographic-primitives/logos/stitcher logo_998493de-72e9-435d-ab64-ab81fc36b9bb.svg'
AUTHOR = 'gpt-6'

class StitcherLogo(Solo48):
    icon_id = 'stitcher-logo'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('stitcher', 'podcast', 'bars', 'audio', 'logo', 'brand', 'radio')

    def build(self):
        # Plan: Segmented horizontal body with one full-height separator and a short trailing bar. Preserve the two left partitions as real shared wall junctions; omit the narrow right slot.
        # Exact keyshape ink extremes are owned by Keyshape.HRECT_L on SOLO48.

        nodes=[(4,16),(12,16),(24,16),(24,32),(12,32),(4,32)]
        for j,a in enumerate(nodes):self.add_line('rim-'+str(j),a,nodes[(j+1)%len(nodes)])
        self.add_contour('body',*[f'rim-{j}' for j in range(len(nodes))],closed=True)
        self.add_line('division',(12,16),(12,32));self.relate('connect','body','division')
        self.add_line('separator',(34,8),(34,40))
        self.add_line('end',(44,16),(44,32))

