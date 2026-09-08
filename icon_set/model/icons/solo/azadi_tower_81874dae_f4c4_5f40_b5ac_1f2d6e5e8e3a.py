"""Azadi Tower with smooth flared shoulders and two nested pointed arches."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '81874dae-f4c4-5f40-b5ac-1f2d6e5e8e3a'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-02/azadi tower iran_81874dae-f4c4-5f40-b5ac-1f2d6e5e8e3a.svg'
AUTHOR = 'gpt-6'


class AzadiTower(Solo48):
    icon_id = 'azadi-tower'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "places/landmarks"
    aliases = ()
    keywords = ('azadi', 'tower', 'iran', 'tehran', 'monument', 'arch', 'landmark', 'gate', 'architecture')

    def build(self) -> None:
        # HRECT_XL centerline extremes: (2,5)-(46,43); mirror around x=24.
        self.add_line('crown',(14,5),(34,5))
        self.add_line('right-neck',(34,5),(35,16))
        self.add_arc('right-shoulder',(35,16),(40,33),radius_x=34,sweep=False)
        self.add_line('right-flare',(40,33),(46,43))
        self.add_line('right-foot',(46,43),(34,43))
        self.add_line('right-opening-leg',(34,43),(32,33))
        self.add_arc('right-pointed-arch',(32,33),(24,16),radius_x=27,sweep=False)
        self.add_arc('left-pointed-arch',(24,16),(16,33),radius_x=27,sweep=False)
        self.add_line('left-opening-leg',(16,33),(14,43))
        self.add_line('left-foot',(14,43),(2,43))
        self.add_line('left-flare',(2,43),(8,33))
        self.add_arc('left-shoulder',(8,33),(13,16),radius_x=34,sweep=False)
        self.add_line('left-neck',(13,16),(14,5))
        self.add_contour('monument','crown','right-neck','right-shoulder','right-flare','right-foot','right-opening-leg','right-pointed-arch','left-pointed-arch','left-opening-leg','left-foot','left-flare','left-shoulder','left-neck',closed=True)
        self.add_arc('lower-arch-left',(16,33),(24,27),radius_x=10,sweep=True)
        self.add_arc('lower-arch-right',(24,27),(32,33),radius_x=10,sweep=True)
        self.add_contour('lower-arch','lower-arch-left','lower-arch-right')
        self.relate('connect','lower-arch','monument')
