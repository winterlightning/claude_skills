"""Independent 32px profile of plant-nature.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '5b473017-90a0-4c45-ac0d-3352cf57b3e6'
SOURCE_PATH = 'pictographic-primitives/nature/plant_5b473017-90a0-4c45-ac0d-3352cf57b3e6.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('5b473017-90a0-4c45-ac0d-3352cf57b3e6', 'pictographic-primitives/nature/plant_5b473017-90a0-4c45-ac0d-3352cf57b3e6.svg'), ('61cad875-dd4d-4009-aa91-d68670ce5e63', 'pictographic-primitives/nature/plant_61cad875-dd4d-4009-aa91-d68670ce5e63.svg'), ('93a59e45-5521-49b0-9911-63d35bb7f98a', 'pictographic-primitives/nature/plant_93a59e45-5521-49b0-9911-63d35bb7f98a.svg'), ('f082c27d-7bed-48d6-b2f0-6148f3fd74a2', 'pictographic-primitives/nature/plant_f082c27d-7bed-48d6-b2f0-6148f3fd74a2.svg'))
PROFILE_SOURCE_KEYS = ('solo/plant-nature', 'solo/plant-61cad875', 'solo/plant-93a59e45', 'solo/plant-f082c27d')
SOLO_SOURCE_ICON_IDS = ('plant-nature', 'plant-61cad875', 'plant-93a59e45', 'plant-f082c27d')
REFERENCE_EXPORT_SHA256 = 'b36ee79394e42de4854ee7e704a9687adb6fd3bbb039c39dd32f33540a021d6f'

class DrawingContainerSymbol(Sub32):
    icon_id = 'plant-nature-sub32-symbol'
    related_origin_icon_id = 'plant-nature-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/plant-nature-sub32'
    counterpart_icon_id = 'plant-nature-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'nature'
    categories = ('nature', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (16, 25), ((8, 25), (2, 20), (2, 13)))
        self.add_bezier('p1-r1-2', (2, 13), ((7, 14), (10, 15), (11, 18)))
        self.add_bezier('p1-r1-3', (11, 18), ((11, 16), (11, 15), (11, 14)))
        self.add_bezier('p1-r1-4', (11, 14), ((11, 9), (13, 5), (16, 2)))
        self.add_bezier('p1-r1-5', (16, 2), ((19, 5), (21, 9), (21, 14)))
        self.add_bezier('p1-r1-6', (21, 14), ((21, 15), (21, 16), (21, 18)))
        self.add_bezier('p1-r1-7', (21, 18), ((22, 15), (25, 14), (30, 13)))
        self.add_bezier('p1-r1-8', (30, 13), ((30, 20), (24, 25), (16, 25)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
        self.add_line('p2-r1-1', (16, 25), (16, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-8', 'p2-r1-1')
