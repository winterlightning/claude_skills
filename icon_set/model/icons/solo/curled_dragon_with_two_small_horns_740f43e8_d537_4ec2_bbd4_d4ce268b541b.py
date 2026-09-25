"""Serpentine dragon, blunt right snout, two horns and curling raised tail. SQUARE x6..42 y6..42. Deliberate asymmetry; outlined head and open serpentine body, horn attachments are real endpoints. No useful Lucide dragon match; source provides coil. Omit scales and facial detail; simplify the narrow body outline into a continuous curved stroke to preserve its coil without pinches."""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = '740f43e8-d537-4ec2-bbd4-d4ce268b541b'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_15/dragon_740f43e8-d537-4ec2-bbd4-d4ce268b541b.svg'
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id = 'curled-dragon-with-two-small-horns'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ['Curled Dragon with Two Small Horns']
    keywords = ['dragon', 'serpent', 'horns', 'creature', 'tail', 'mythical', 'coil']
    def build(self):
        self.add_bezier('crown-left',(18,10),((21,10),(24,10),(26,11)))
        self.add_bezier('crown-right',(26,11),((28,12),(29,13),(30,14)))
        self.add_line('snout-top',(30,14),(42,14))
        self.add_bezier('snout-tip',(42,14),((42,20),(42,22),(38,22)))
        self.add_line('jaw',(38,22),(22,22))
        self.add_bezier('head-back',(22,22),((10,22),(10,10),(18,10)))
        self.add_contour('head','crown-left','crown-right','snout-top','snout-tip','jaw','head-back',closed=True)
        self.add_bezier('serpentine-body',(22,22),((22,27),(36,28),(36,34)),((36,40),(30,42),(24,42)),((14,42),(6,42),(6,34)),((6,29),(10,28),(10,26)))
        self.relate('connect','head','serpentine-body')
        self.add_line('horn-left',(18,10),(12,6))
        self.add_line('horn-right',(26,11),(26,6))
        self.relate('connect','head','horn-left')
        self.relate('connect','head','horn-right')
