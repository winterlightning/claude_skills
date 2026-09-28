"""Stomach.

Plan: Two continuous walls form esophagus, pouch and outlet. Arc extrema own broad right pouch and left inlet bend. Bounds (8,4)-(40,44). No useful Lucide organ match.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b1f8150e-25ff-55be-bec0-f5a8f35ade81'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/specialty stomach_b1f8150e-25ff-55be-bec0-f5a8f35ade81.svg'
AUTHOR = 'gpt-6'


class Stomach(Solo48):
    icon_id = 'stomach'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/health'
    aliases = ()
    keywords = ('stomach',)

    def build(self):
        self.add_line('inlet-left',(18,4),(18,12))
        self.add_arc('inlet-bend',(18,12),(22,22),radius_x=4,radius_y=10,sweep=False)
        self.add_arc('inner-bend',(22,22),(12,30),radius_x=10,radius_y=8)
        self.add_arc('outlet-outer',(12,30),(8,34),radius_x=4,sweep=False)
        self.add_line('outlet-left',(8,34),(8,44))
        self.add_contour('inner-wall','inlet-left','inlet-bend','inner-bend','outlet-outer','outlet-left')
        self.add_line('inlet-right',(28,4),(28,10))
        self.add_arc('inlet-round',(28,10),(32,14),radius_x=4,sweep=False)
        self.add_arc('pouch-upper',(32,14),(40,22),radius_x=8)
        self.add_arc('pouch-lower',(40,22),(24,38),radius_x=16)
        self.add_line('outlet-top',(24,38),(20,38))
        self.add_arc('outlet-inner',(20,38),(18,40),radius_x=2,sweep=False)
        self.add_line('outlet-right',(18,40),(18,44))
        self.add_contour('outer-wall','inlet-right','inlet-round','pouch-upper','pouch-lower','outlet-top','outlet-inner','outlet-right')
