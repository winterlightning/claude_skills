"""A diamond outline folds over itself like a ribbon, with a small inner diamond opening near its centre.

Plan: Diamond ribbon surrounding a small diamond opening.
Keyshape: SQUARE; exact SOLO48 envelope from the contract.
Construction reference: Previously inspected diamond: centered matching diagonal edges.
Simplification: Fold seams omitted for a clean ribbon band.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0697abc9-3868-4637-8bea-f5804a5c6af5'
SOURCE_PATH = 'pictographic-primitives/logos/jira software logo_0697abc9-3868-4637-8bea-f5804a5c6af5.svg'
AUTHOR = 'gpt-6'


class JiraSoftwareLogo(Solo48):
    icon_id = 'jira-software-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    categories = ("logos", "primitives")
    aliases = ()
    keywords = ('jira-software', 'jira', 'atlassian', 'diamond', 'logo', 'brand', 'agile')

    def build(self):
        self.add_polyline('outer',(24,6),(42,24),(24,42),(6,24),closed=True)
        self.add_polyline('inner',(24,18),(30,24),(24,30),(18,24),closed=True)
