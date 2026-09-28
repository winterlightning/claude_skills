"""A curled horn has a broad lower-left bell and narrow upper-right mouthpiece. VRECT_L extremes (8,6)-(40,42). No useful local Lucide instrument match found; use a coherent rounded tube and flared bell, preserving the source’s deliberately asymmetric S-shaped silhouette."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a0d79a66-6868-4e26-b83d-e5a2df3d0530'
SOURCE_PATH = 'pictographic-primitives/symbol/horn 1_a0d79a66-6868-4e26-b83d-e5a2df3d0530.svg'
AUTHOR = 'gpt-6'


class HornCurled(Solo48):
    icon_id = 'horn-curled'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbol"
    categories = ("symbol",)
    aliases = ()
    keywords = ('horn', 'instrument', 'music', 'brass', 'curled', 'bugle', 'sound', 'wind')

    def build(self) -> None:
        # Preserve interior detail sizes; move only the outer edge bands to the exact envelope.
        # Curves reaching an edge use bounded cubic controls, with shared endpoints retained.
        self.add_line('bell-top',(8, 25),(22, 21))
        self.add_line('neck-left',(22, 21),(22, 12))
        self.add_bezier('crown-left',(22, 12),*(((22.93412832, 6.96800053), (26.25786848, 4), (30, 4)),))
        self.add_bezier('crown-right',(30, 4),*(((33.74213152, 4), (37.06587168, 6.96800053), (38, 12)),))
        self.add_line('mouth-top',(38, 12),(40, 20))
        self.add_line('mouth-bottom',(40, 20),(33, 16))
        self.add_arc('neck-inner',(33, 16),(31, 20),radius_x=3,radius_y=3,large_arc=False,sweep=False)
        self.add_line('tube-inner',(31, 20),(34, 30))
        self.add_bezier('tube-bottom',(34, 30),*(((33.14143325, 37.67789755), (28.01186196, 44), (22, 44)),))
        self.add_bezier('bell-bottom',(22, 44),*(((14.98616105, 44), (9.00166121, 37.67789755), (8, 30)),))
        self.add_line('bell-left',(8, 30),(8, 25))
        self.add_bezier('bell-divider',(22, 21),*(((23.80533989, 23.44747873), (24.87277046, 27.34894638), (24.87277046, 31.5)), ((24.87277046, 36.06381703), (23.80533989, 40.94065158), (22, 44))))
        self.add_contour('horn',*('bell-top', 'neck-left', 'crown-left', 'crown-right', 'mouth-top', 'mouth-bottom', 'neck-inner', 'tube-inner', 'tube-bottom', 'bell-bottom', 'bell-left'),closed=True)
        self.relate('connect',*('horn', 'bell-divider'))
