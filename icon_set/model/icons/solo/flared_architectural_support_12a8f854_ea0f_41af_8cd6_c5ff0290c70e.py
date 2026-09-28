"""Flared Architectural Support.

Symbol plan: Mirrored flared support sides share a central split and level top cap. Keep four sweeping legs; remove secondary ribs and the short top notch.
HRECT_L centerline extremes (4,8)-(44,40); envelope follows the subject's proportions.
Construction reference: No useful Lucide subject match; mirrored tangent elliptical sweeps preserve flared architectural support.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '12a8f854-ea0f-41af-8cd6-c5ff0290c70e'
SOURCE_PATH = 'pictographic-primitives/building/modern architecture top_12a8f854-ea0f-41af-8cd6-c5ff0290c70e.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'flared-architectural-support'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'building'
    categories = ('building', 'primitives')
    aliases = ()
    keywords = ('flared', 'architectural', 'support')

    def build(self) -> None:

        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,ry=None,s=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=s)
        def connect(a,b): self.relate('connect',a,b)

        # Shared cap and four equal-height flares preserve mirror symmetry.
        arc('outer-left',(12,8),(4,40),8,32)
        line('cap-left',(12,8),(24,8))
        line('cap-right',(24,8),(36,8))
        arc('outer-right',(44,40),(36,8),8,32)
        arc('inner-left',(24,8),(14,40),10,32)
        arc('inner-right',(34,40),(24,8),10,32)
        connect('outer-left','cap-left');connect('cap-left','cap-right')
        connect('cap-right','outer-right');connect('cap-left','inner-left');connect('cap-left','inner-right')
        connect('cap-right','inner-left');connect('cap-right','inner-right');connect('inner-left','inner-right')
