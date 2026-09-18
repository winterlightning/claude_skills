"""Fresh Carrot Vegetable: user-requested grid-fitted 32px version of carrot-with-two-pointed-leaves.
Plan: retain source primitive/contour topology and fit VRECT_XL ink (2, 0, 30, 32).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID='6175b21e-96a2-4503-a4cc-6b0bc36376c0'
SOURCE_PATH='pictographic-primitives/food/carrot_6175b21e-96a2-4503-a4cc-6b0bc36376c0.svg'
SOLO_SOURCE_ICON_ID='carrot-with-two-pointed-leaves'
AUTHOR='gpt-6'
class Drawing(Sub32):
    icon_id='carrot-with-two-pointed-leaves-sub32'
    keyshape=Keyshape.VRECT_XL
    semantic_role='SUB'
    semantic_kind='modifier'
    category='objects/food'
    tags=('sub icon',)
    keywords=('sub icon', 'grid fitted', 'fresh carrot vegetable')
    def build(self):
        self.add_bezier('root', (16, 12), ((12, 10), (8, 13), (8, 16)), ((8, 21), (14, 30), (16, 30)), ((18, 30), (24, 21), (24, 16)), ((24, 13), (20, 10), (16, 12)))
        self.add_bezier('leaf--1', (16, 12), ((12, 12), (4, 9), (4, 2)), ((10, 3), (16, 6), (16, 12)))
        self.add_bezier('leaf-1', (16, 12), ((20, 12), (28, 9), (28, 2)), ((22, 3), (16, 6), (16, 12)))
        self.add_contour('carrot', 'root', closed=True)
        self.add_contour('leaf-shape--1', 'leaf--1', closed=True)
        self.add_contour('leaf-shape-1', 'leaf-1', closed=True)
        self.relate('connect', 'leaf-shape--1', 'carrot')
        self.relate('connect', 'leaf-shape-1', 'carrot')
        self.relate('connect', 'leaf-shape--1', 'leaf-shape-1')
        self.add_anchor('center',(16, 16))
