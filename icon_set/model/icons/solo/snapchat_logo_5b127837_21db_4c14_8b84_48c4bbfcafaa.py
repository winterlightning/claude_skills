"""Domed ghost silhouette with paired arm flares and a scalloped lower hem. Lucide ghost informs the smooth dome and coherent hem; retain the source face-free silhouette."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5b127837-21db-4c14-8b84-48c4bbfcafaa'
SOURCE_PATH = 'pictographic-primitives/logos/snapchat logo_5b127837-21db-4c14-8b84-48c4bbfcafaa.svg'
AUTHOR = 'gpt-6'

class SnapchatLogo(Solo48):
    icon_id = 'snapchat-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'brands/logos'
    aliases = ()
    keywords = ('snapchat', 'ghost', 'social', 'messaging', 'logo', 'brand', 'camera')

    def build(self):
        # Plan: Domed ghost silhouette with paired arm flares and a scalloped lower hem. Lucide ghost informs the smooth dome and coherent hem; retain the source face-free silhouette.
        # Exact keyshape ink extremes are owned by Keyshape.SQUARE on SOLO48.

        self.add_line('left-neck',(12,24),(12,18))
        self.add_arc('dome',(12,18),(36,18),radius_x=12)
        self.add_line('right-neck',(36,18),(36,24))
        self.add_bezier('right-side',(36,24),((36,30),(38,32),(42,34)),((42,37),(34,35),(34,38)),((34,40),(30,40),(28,42)))
        self.add_line('hem',(28,42),(20,42))
        self.add_bezier('left-side',(20,42),((18,40),(14,40),(14,38)),((14,35),(6,37),(6,34)),((10,32),(12,30),(12,24)))
        self.add_contour('ghost','left-neck','dome','right-neck','right-side','hem','left-side',closed=True)

