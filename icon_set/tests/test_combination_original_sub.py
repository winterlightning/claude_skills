import unittest
import xml.etree.ElementTree as ET
from icon_set.scripts.combination_experiment import restore_original_sub

class OriginalSubTests(unittest.TestCase):
    def test_curves_are_copied_without_flattening_and_main_is_unchanged(self):
        original='<svg xmlns="http://www.w3.org/2000/svg" stroke="currentColor" stroke-width="4" fill="none"><path id="curve" d="M2 16 A14 14 0 0 1 30 16 C30 24 24 30 16 30"/><circle cx="16" cy="16" r="2"/></svg>'
        merged='<svg xmlns="http://www.w3.org/2000/svg"><g id="main-icon-clipped"><path d="M1 1L2 2"/></g><g id="state-icon"><path d="M0 0L1 1M1 1L2 2"/></g></svg>'
        out=ET.fromstring(restore_original_sub(merged,{'document':original,'bounds':[2,2,30,30]}, {'painted_box':{'x':30,'y':30,'w':32,'h':32}}))
        main,sub=list(out);self.assertEqual(ET.tostring(main),ET.tostring(list(ET.fromstring(merged))[0]))
        self.assertEqual(list(sub)[0].get('d'),list(ET.fromstring(original))[0].get('d'))
        self.assertEqual(sub.get('transform'),'translate(30 30) scale(1)')
        self.assertEqual(list(sub)[1].get('r'),'2');self.assertEqual(len(list(sub)),2)
    def test_explicit_resize_is_a_transform_not_rewritten_geometry(self):
        src='<svg xmlns="http://www.w3.org/2000/svg" stroke-width="4"><path d="M2 2Q16 30 30 2"/></svg>'
        dst='<svg xmlns="http://www.w3.org/2000/svg"><g id="state-icon"/></svg>'
        out=ET.fromstring(restore_original_sub(dst,{'document':src,'bounds':[2,2,30,30]},{'painted_box':{'x':0,'y':0,'w':18,'h':18}}))
        group=list(out)[0];self.assertEqual(group.get('transform'),'translate(1 1) scale(0.5)');self.assertEqual(list(group)[0].get('d'),'M2 2Q16 30 30 2');self.assertIsNone(list(group)[0].get('vector-effect'));self.assertEqual(float(group.get('stroke-width'))*.5,4)
