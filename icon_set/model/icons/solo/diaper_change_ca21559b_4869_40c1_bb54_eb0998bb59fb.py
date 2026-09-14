"""Rebuilt the bending adult and supine baby with circular heads, a single arm/leg and separated changing surface. Covers all three older versions.

Keyshape SQUARE: visible bounds (4, 4, 44, 44).
Reference: human_ref/full_body_ref.png: bending action, circular heads and round limbs.
"""
# Independent repair of diaper-change-v3; parent preserved.
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'ca21559b-4869-40c1-bb54-eb0998bb59fb'
SOURCE_PATH = 'pictographic-primitives/babies/family baby change diaper_ca21559b-4869-40c1-bb54-eb0998bb59fb.svg'
AUTHOR = 'gpt-6'

class DiaperChange(Solo48):
    icon_id = 'diaper-change'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'people/babies'
    aliases = ()
    keywords = ('diaper', 'change', 'infant', 'nursery')

    def build(self) -> None:
        # SQUARE centerlines (6,6)-(42,42). Shared human reference:
        # icon_set/references/human_ref/full_body_ref.png (bending action).
        # Adult head radius 5, baby head radius 3; each head has exactly
        # eight centerline units / four ink units to its own body.
        # Side pose is asymmetric; a single arm/leg retains the changing action.
        self.add_arc('adult-head-top',(13,11),(23,11),radius_x=5)
        self.add_arc('adult-head-bottom',(23,11),(13,11),radius_x=5)
        self.add_contour('adult-head','adult-head-top','adult-head-bottom',closed=True)
        self.add_polyline('adult-back',(18,24),(10,30),(6,42))
        self.add_polyline('adult-arm',(18,24),(24,34),(28,34))
        self.relate('connect','adult-back','adult-arm')
        self.add_polyline('baby-body',(23,26),(28,34),(28,28))
        self.relate('connect','adult-arm','baby-body')
        self.add_arc('baby-head-top',(36,28),(42,28),radius_x=3)
        self.add_arc('baby-head-bottom',(42,28),(36,28),radius_x=3)
        self.add_contour('baby-head','baby-head-top','baby-head-bottom',closed=True)
        self.add_line('surface',(23,42),(42,42))
