"""Concentric rings nest around a small central ring, each outer ring broken by a gap at the lower left like a spiral.

Plan: Concentric radii 2,11,20; matching lower-left openings.
Keyshape: CIRCLE; exact SOLO48 envelope from the contract.
Construction reference: Previously inspected cast: concentric broadcast arcs.
Simplification: One intermediate ring removed to preserve clearance.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '729b11ac-a0d7-441b-bab4-9e259f612553'
SOURCE_PATH = 'pictographic-primitives/logos/ibeacon logo_729b11ac-a0d7-441b-bab4-9e259f612553.svg'
AUTHOR = 'gpt-6'


class IbeaconLogo(Solo48):
    icon_id = 'ibeacon-logo'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    aliases = ()
    keywords = ('ibeacon', 'apple', 'bluetooth', 'beacon', 'logo', 'brand', 'proximity')

    def build(self):
        self.add_arc('center',(26,24),(22,24),radius_x=2)
        self.add_arc('center2',(22,24),(26,24),radius_x=2)
        self.add_contour('ring','center','center2',closed=True)
        for r in (11,20):
         self.add_arc(f'a{r}',(24-r,24),(24+r,24),radius_x=r)
         self.add_arc(f'b{r}',(24+r,24),(24,24+r),radius_x=r)
         self.add_contour(f'wave{r}',f'a{r}',f'b{r}')
