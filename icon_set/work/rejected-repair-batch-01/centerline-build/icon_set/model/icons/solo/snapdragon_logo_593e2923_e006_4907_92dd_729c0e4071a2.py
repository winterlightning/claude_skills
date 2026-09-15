"""Circular badge split by a sweeping flame-like S. Keep the primary divider and omit the smaller escaping hook to avoid a narrow secondary pocket."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '593e2923-e006-4907-92dd-729c0e4071a2'
SOURCE_PATH = 'pictographic-primitives/logos/snapdragon logo_593e2923-e006-4907-92dd-729c0e4071a2.svg'
AUTHOR = 'gpt-6'

class SnapdragonLogo(Solo48):
    icon_id = 'snapdragon-logo'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'brands/logos'
    aliases = ()
    keywords = ('snapdragon', 'qualcomm', 'processor', 'chip', 'logo', 'brand', 'mobile')

    def build(self):
        # Plan: Circular badge split by a sweeping flame-like S. Keep the primary divider and omit the smaller escaping hook to avoid a narrow secondary pocket.
        # Exact keyshape ink extremes are owned by Keyshape.CIRCLE on SOLO48.

        nodes=[(24,4),(44,24),(24,44),(4,24)]
        for j,a in enumerate(nodes):self.add_arc('rim-'+str(j),a,nodes[(j+1)%4],radius_x=20)
        self.add_contour('rim',*[f'rim-{j}' for j in range(4)],closed=True)
        self.add_bezier('flame',(24,4),((14,18),(30,20),(30,28)),((30,36),(26,40),(24,44)))
        self.relate('connect','flame','rim')

