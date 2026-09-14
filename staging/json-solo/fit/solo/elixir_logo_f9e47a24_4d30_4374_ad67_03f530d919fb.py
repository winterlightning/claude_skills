"""Elixir logo (logos), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f9e47a24-4d30-4374-ad67-03f530d919fb'
SOURCE_PATH = 'icons-json/logos/elixir logo_f9e47a24-4d30-4374-ad67-03f530d919fb.json'
AUTHOR = 'json_to_solo'

class ElixirLogoLogos(Solo48):
    icon_id = 'elixir-logo-logos'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('elixir', 'logo', 'logos')

    def build(self):
        self.add_line('e0', (36, 22), (30, 18))
        self.add_arc('e1-1', (30, 18), (25, 4), radius_x=14)
        self.add_arc('e1-2', (25, 4), (8, 30), radius_x=36, sweep=False)
        self.add_arc('e1-3', (8, 30), (13, 40), radius_x=13, sweep=False)
        self.add_arc('e1-4', (13, 40), (18, 43), radius_x=18, sweep=False)
        self.add_line('e1-5', (18, 43), (24, 44))
        self.add_line('e1-6', (24, 44), (33, 42))
        self.add_arc('e1-7', (33, 42), (39, 36), radius_x=16, sweep=False)
        self.add_line('e1-8', (39, 36), (40, 31))
        self.add_arc('e1-9', (40, 31), (36, 22), radius_x=13, sweep=False)
        self.add_contour('c0', 'e0', 'e1-1', 'e1-2', 'e1-3', 'e1-4', 'e1-5', 'e1-6', 'e1-7', 'e1-8', 'e1-9', closed=True)
