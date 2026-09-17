"""Horizontal Double Ended Wrench.
Plan: A horizontal grip joins two mirrored open wrench jaws with broad curved crowns. Ink (2,8)-(46,40).
Reference construction: wrench.
Reduction: Round both jaw crowns symmetrically and preserve the rectangular inner recesses.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd63b4e68-3e3c-4320-ad5b-85484116fc79'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/wrench_d63b4e68-3e3c-4320-ad5b-85484116fc79.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'horizontal-double-ended-wrench'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface-essential'
    aliases = ()
    keywords = ('horizontal', 'double', 'ended', 'wrench')
    def build(self):

        for label,flip in [('left',False),('right',True)]:
         def pt(x,y):return (48-x,y) if flip else (x,y)
         self.add_bezier(label+'-upper-a',pt(4,18),(pt(4,14),pt(6,10),pt(10,10)))
         self.add_bezier(label+'-upper-b',pt(10,10),(pt(16,10),pt(16,18),pt(20,18)))
         self.add_bezier(label+'-lower-a',pt(20,30),(pt(16,30),pt(16,38),pt(10,38)))
         self.add_bezier(label+'-lower-b',pt(10,38),(pt(6,38),pt(4,34),pt(4,30)))
         self.add_polyline(label+'-mouth',pt(4,30),pt(12,30),pt(12,18),pt(4,18))
         self.add_contour(label+'-upper',label+'-upper-a',label+'-upper-b')
         self.add_contour(label+'-lower',label+'-lower-a',label+'-lower-b')
         self.relate('connect',label+'-upper',label+'-mouth');self.relate('connect',label+'-lower',label+'-mouth')
        self.add_line('top-grip',(20,18),(28,18));self.add_line('bottom-grip',(20,30),(28,30))
        for label in ['left','right']:
         self.relate('connect','top-grip',label+'-upper');self.relate('connect','bottom-grip',label+'-lower')
