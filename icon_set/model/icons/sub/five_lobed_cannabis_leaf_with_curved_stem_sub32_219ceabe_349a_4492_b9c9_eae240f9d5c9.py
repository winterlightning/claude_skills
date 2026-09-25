"""Seven Pointed Cannabis Leaf: user-requested grid-fitted 32px version of five-lobed-cannabis-leaf-with-curved-stem.
Plan: retain source primitive/contour topology and fit SQUARE ink (0, 0, 32, 32).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID='219ceabe-349a-4492-b9c9-eae240f9d5c9'
SOURCE_PATH='pictographic-primitives/cannabis/cannabis_219ceabe-349a-4492-b9c9-eae240f9d5c9.svg'
SOLO_SOURCE_ICON_ID='five-lobed-cannabis-leaf-with-curved-stem'
AUTHOR='gpt-6'
class Drawing(Sub32):
    icon_id='five-lobed-cannabis-leaf-with-curved-stem-sub32'
    keyshape=Keyshape.SQUARE
    semantic_role='SUB'
    semantic_kind='modifier'
    category = 'cannabis'
    categories = ('primitives', 'cannabis')
    tags=('sub icon',)
    keywords=('sub icon', 'grid fitted', 'seven pointed cannabis leaf')
    def build(self):
        self.add_bezier('leaf-0', (16, 2), ((19, 7), (20, 11), (19, 14)))
        self.add_bezier('leaf-1', (19, 14), ((22, 11), (25, 8), (28, 8)))
        self.add_bezier('leaf-2', (28, 8), ((28, 13), (25, 17), (22, 19)))
        self.add_bezier('leaf-3', (22, 19), ((25, 19), (28, 21), (30, 22)))
        self.add_bezier('leaf-4', (30, 22), ((28, 24), (26, 25), (24, 25)))
        self.add_bezier('leaf-5', (24, 25), ((20, 27), (18, 25), (16, 24)))
        self.add_bezier('leaf-6', (16, 24), ((14, 25), (12, 27), (8, 25)))
        self.add_bezier('leaf-7', (8, 25), ((6, 25), (4, 24), (2, 22)))
        self.add_bezier('leaf-8', (2, 22), ((4, 21), (7, 19), (10, 19)))
        self.add_bezier('leaf-9', (10, 19), ((7, 17), (4, 13), (4, 8)))
        self.add_bezier('leaf-10', (4, 8), ((7, 8), (10, 11), (13, 14)))
        self.add_bezier('leaf-11', (13, 14), ((12, 11), (13, 7), (16, 2)))
        self.add_bezier('stem-0', (16, 24), ((16, 27), (15, 28), (13, 30)))
        self.add_contour('leaf', 'leaf-0', 'leaf-1', 'leaf-2', 'leaf-3', 'leaf-4', 'leaf-5', 'leaf-6', 'leaf-7', 'leaf-8', 'leaf-9', 'leaf-10', 'leaf-11', closed=True)
        self.add_contour('stem', 'stem-0', closed=False)
        self.relate('connect', 'leaf', 'stem')
        self.add_anchor('center',(16, 16))
