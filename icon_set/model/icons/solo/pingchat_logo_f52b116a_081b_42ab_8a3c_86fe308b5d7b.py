"""Two offset brand lobes: lower-left three-quarter disc and upper-right speech D, with their diagonal arrangement. Omit the exclamation because the bubble cannot contain it at legal spacing."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f52b116a-081b-42ab-8a3c-86fe308b5d7b'
SOURCE_PATH = 'pictographic-primitives/logos/pingchat logo_f52b116a-081b-42ab-8a3c-86fe308b5d7b.svg'
AUTHOR = 'gpt-6'

class PingchatLogo(Solo48):
    icon_id = 'pingchat-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    categories = ('logos', 'primitives')
    aliases = ()
    keywords = ('pingchat', 'chat', 'alert', 'exclamation', 'logo', 'brand', 'messaging')

    def build(self):
        # Plan: Two offset brand lobes: lower-left three-quarter disc and upper-right speech D, with their diagonal arrangement. Omit the exclamation because the bubble cannot contain it at legal spacing.
        # Exact keyshape ink extremes are owned by Keyshape.SQUARE on SOLO48.

        self.add_arc('pie',(17,20),(28,31),radius_x=11,large_arc=True,sweep=False)
        self.add_line('pie-notch-1',(28,31),(17,31))
        self.add_line('pie-notch-2',(17,31),(17,20))
        self.add_contour('pie-shape','pie','pie-notch-1','pie-notch-2',closed=True)
        self.add_line('bubble-left',(27,22),(27,6))
        self.add_arc('bubble-round',(27,6),(27,22),radius_x=15,radius_y=8)
        self.add_contour('bubble','bubble-left','bubble-round',closed=True)

