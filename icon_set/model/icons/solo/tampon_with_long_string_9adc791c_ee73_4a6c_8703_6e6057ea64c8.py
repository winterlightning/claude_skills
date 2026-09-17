"""Tampon with Long String.

Plan: Domed tampon owns a central groove; long looping string attaches at base midpoint. Drop tiny lower tab. Bounds (8,4)-(40,44). Lucide pill informs tangent cap.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9adc791c-ee73-4a6c-8703-6e6057ea64c8'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/tampon 1_9adc791c-ee73-4a6c-8703-6e6057ea64c8.svg'
AUTHOR = 'gpt-6'


class TamponWithLongString(Solo48):
    icon_id = 'tampon-with-long-string'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/health'
    aliases = ()
    keywords = ('tampon', 'with', 'long', 'string')

    def build(self):
        self.add_arc('dome',(8,14),(28,14),radius_x=10)
        self.add_line('right',(28,14),(28,28))
        self.add_arc('br',(28,28),(24,32),radius_x=4)
        self.add_line('base-right',(24,32),(18,32))
        self.add_line('base-left',(18,32),(12,32))
        self.add_arc('bl',(12,32),(8,28),radius_x=4)
        self.add_line('left',(8,28),(8,14))
        self.add_contour('tampon','dome','right','br','base-right','base-left','bl','left',closed=True)
        self.add_line('string-start',(18,32),(18,33))
        self.add_arc('string-loop',(18,33),(40,33),radius_x=11,sweep=False)
        self.add_line('string-rise',(40,33),(40,20))
        self.add_contour('string','string-start','string-loop','string-rise')
        self.relate('connect','tampon','string')
        self.add_line('groove',(18,14),(18,32))
        self.relate('connect','groove','tampon')
        self.relate('connect','groove','string')
