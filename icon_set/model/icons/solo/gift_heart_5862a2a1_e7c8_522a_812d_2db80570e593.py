"""A ribbon-tied gift box with a heart hanging over its front.
Lucide gift: joined lid/body structure and mirrored bow loops; supplied reference adds the heart.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5862a2a1-e7c8-522a-812d-2db80570e593'
SOURCE_PATH = 'pictographic-primitives/rewards/gift heart_5862a2a1-e7c8-522a-812d-2db80570e593.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'gift-heart'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('gift', 'heart')
    def build(self):
        # Symmetric gift: taller bow loops, full-width box sides and smaller heart.
        self.add_arc('bow-left',(12,14),(24,14),radius_x=6,radius_y=8)
        self.add_arc('bow-right',(24,14),(36,14),radius_x=6,radius_y=8)
        self.add_polyline('lid',(6,14),(12,14),(24,14),(36,14),(42,14),(42,22),(24,22),(6,22),closed=True)
        self.add_polyline('box-left',(6,22),(6,38),(20,38))
        self.add_polyline('box-right',(42,22),(42,38),(28,38))
        self.add_line('ribbon',(24,14),(24,22))
        self.add_arc('heart-left',(24,34),(16,34),radius_x=4,sweep=False)
        self.add_line('heart-sides-1',(16,34),(20,38))
        self.add_line('heart-sides-1b',(20,38),(24,42))
        self.add_line('heart-sides-2',(24,42),(28,38))
        self.add_line('heart-sides-2b',(28,38),(32,34))
        self.add_arc('heart-right',(32,34),(24,34),radius_x=4,sweep=False)
        self.add_contour('heart','heart-left','heart-sides-1','heart-sides-1b','heart-sides-2','heart-sides-2b','heart-right',closed=True)
        for n in ('bow-left','bow-right','box-left','box-right','ribbon'):self.relate('connect',n,'lid')
        self.relate('connect','bow-left','bow-right')
        self.relate('connect','box-left','heart-sides-1','heart-sides-1b')
        self.relate('connect','box-right','heart-sides-2','heart-sides-2b')

# Final repair review: A gift box with two bow loops and a heart at its lower edge.
# SQUARE redistributes width to clear the lower heart.
# Changes: Enlarged bow openings; simplified heart; omitted the lower vertical ribbon segment. Box edge joins the heart at shared nodes.
# validate_icon: valid; build gate: pass with zero errors and zero warnings.
