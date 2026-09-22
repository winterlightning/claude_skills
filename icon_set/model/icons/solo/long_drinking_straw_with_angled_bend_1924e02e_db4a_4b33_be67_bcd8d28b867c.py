"""Bent drinking straw, one continuous open stroke with softened elbow.
VRECT_M x10..38/y4..44 allows a clear diagonal silhouette. Source supplies
long stem and short up-right mouth end. Lucide straw search found no match.
Control vectors follow the adjacent lines; no detached detail or tube outline.
"""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = '1924e02e-db4a-4b33-be67-bcd8d28b867c'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_36/straw_1924e02e-db4a-4b33-be67-bcd8d28b867c.svg'
AUTHOR = 'gpt-6-astra'
class LongDrinkingStraw(Solo48):
    icon_id = 'long-drinking-straw-with-angled-bend'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'Uncategorized'
    aliases = ('Bent Drinking Straw',)
    keywords = ('straw','drink','bend','tube','beverage','utensil')
    def build(self):
        self.add_line('stem',(10,44),(20,16))
        self.add_bezier('elbow',(20,16),((21,13.2),(21.2,13.6),(24,12)))
        self.add_line('mouth',(24,12),(38,4))
        self.add_contour('straw','stem','elbow','mouth')
