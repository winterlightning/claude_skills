"""Left-facing elephant with heavy body, hanging trunk and a broad ear; two visible legs replace four crowded legs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5c76e262-54ad-5610-ab09-79dc0d015364'
SOURCE_PATH = 'pictographic-primitives/animals/elephant_5c76e262-54ad-5610-ab09-79dc0d015364.svg'
AUTHOR = 'gpt-6'


class StandingElephant(Solo48):
    icon_id = 'standing-elephant'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/animals"
    aliases = ()
    keywords = ('standing', 'elephant')

    def build(self) -> None:
        # Visible keyshape bounds: (0, 6, 48, 42); centerlines inset by 2.
        self.add_arc('brow', (2, 20), (14, 8), radius_x=12, radius_y=12, sweep=True)
        self.add_line('crown', (14, 8), (27, 8))
        self.add_arc('ear', (27, 8), (17, 24), radius_x=16, radius_y=16, sweep=True)
        self.add_contour('head', 'brow', 'crown', 'ear')
        self.add_line('trunk-outer', (2, 20), (2, 34))
        self.add_arc('trunk-tip', (2, 34), (10, 34), radius_x=4, radius_y=4, sweep=False)
        self.add_line('trunk-inner', (10, 34), (10, 26))
        self.add_contour('trunk', 'trunk-outer', 'trunk-tip', 'trunk-inner')
        self.relate("connect", 'head', 'trunk')
        self.add_line('shoulder', (27, 14), (34, 14))
        self.add_arc('back', (34, 14), (46, 26), radius_x=12, radius_y=12, sweep=True)
        self.add_line('hind', (46, 26), (46, 40))
        self.add_line('rear-foot', (46, 40), (36, 40))
        self.add_line('rear-leg', (36, 40), (36, 31))
        self.add_line('belly', (36, 31), (23, 31))
        self.add_line('fore-leg', (23, 31), (23, 40))
        self.add_line('fore-foot', (23, 40), (15, 40))
        self.add_line('chest', (15, 40), (15, 26))
        self.add_contour('body', 'shoulder', 'back', 'hind', 'rear-foot', 'rear-leg', 'belly', 'fore-leg', 'fore-foot', 'chest')
        self.relate("connect", 'head', 'body')
