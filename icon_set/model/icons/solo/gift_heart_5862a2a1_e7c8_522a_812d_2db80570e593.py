"""A ribbon-tied gift box with a heart hanging over its front.
Lucide gift: joined lid/body structure and mirrored bow loops; supplied reference adds the heart.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5862a2a1-e7c8-522a-812d-2db80570e593'
SOURCE_PATH = 'icon_set/work/todo-references/gift heart_5862a2a1-e7c8-522a-812d-2db80570e593.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'gift-heart'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('gift', 'heart')
    def build(self):

        # Plan: bilateral bow above the lid; central ribbon ends at the heart.
        # VRECT_L visible extrema (6,2)-(42,46), centerlines (8,4)-(40,44).
        axis=24
        self.add_bezier('bow-left',(axis,16),((19,4),(12,1),(12,7)),((12,12),(18,14),(axis,16)))
        self.add_bezier('bow-right',(axis,16),((29,4),(36,1),(36,7)),((36,12),(30,14),(axis,16)))
        self.add_polyline('lid',(8,16),(40,16),(40,24),(8,24),closed=True)
        self.add_polyline('box-left',(10,24),(10,40),(18,40))
        self.add_polyline('box-right',(38,24),(38,40),(30,40))
        self.add_line('ribbon',(24,16),(24,30))
        self.add_bezier('heart',(24,30),((13,23),(9,34),(24,44)),((39,34),(35,23),(24,30)))
        self.add_contour('heart-outline','heart',closed=True)
        for part in ('bow-left','bow-right','box-left','box-right','ribbon'):
            self.relate('connect',part,'lid')
        self.relate('connect','bow-left','bow-right')
        self.relate('connect','ribbon','heart-outline')
