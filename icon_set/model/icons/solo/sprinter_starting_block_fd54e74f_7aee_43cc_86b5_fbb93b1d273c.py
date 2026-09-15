# Repair: End the calf at the starting-block contact rather than drawing through it. Remove the redundant ground stroke beneath the shoe.
"""Sprinter starting block, authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='fd54e74f-7aee-43cc-86b5-fbb93b1d273c'
SOURCE_PATH='pictographic-primitives/sports/running ready starting block_fd54e74f-7aee-43cc-86b5-fbb93b1d273c.svg'
AUTHOR = 'gpt-6'

class SprinterStartingBlock(Solo48):
    icon_id='sprinter-starting-block'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/sports'
    aliases=()
    keywords=('sprinter', 'starting', 'block')
    def build(self):
        from ._symmetry_curves import path, ellipse, line, poly, contacts

        poly(self,'leg',(24,8),(35,15),(39,20),(39,29))
        poly(self,'shoe',(4,15),(11,21),(13,31),(9,37),(13,40),(23,40))
        poly(self,'block',(23,40),(39,29),(44,40),closed=True)
        contacts(self)
