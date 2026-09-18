import unittest,json,io,xml.etree.ElementTree as ET
from pathlib import Path
from svgpathtools import Document,Arc
ROOT=Path(__file__).resolve().parents[2]
class BicycleRepairTests(unittest.TestCase):
 def test_shared_wheel_geometry_and_connections(self):
  records=json.loads((ROOT/'icon_set/data/sub-icon-repairs.json').read_text())
  for key,r in records.items():
   if 'bicycle' not in key:continue
   with self.subTest(icon=key):
    doc=(ROOT/r['repair_svg']).read_text();root=ET.fromstring(doc)
    wheels=root.findall('{*}circle');self.assertEqual(len(wheels),2)
    cx=[float(w.get('cx')) for w in wheels];cy=[float(w.get('cy')) for w in wheels];rad=[float(w.get('r')) for w in wheels]
    self.assertEqual(rad,[5,5]);self.assertEqual(cy[0],cy[1]);self.assertEqual(cx[1]-cx[0]-sum(rad)-4,4)
    for p in Document(io.StringIO(doc)).paths()[:2]:
     arcs=[s for s in p if isinstance(s,Arc)]
     for arc in arcs:self.assertAlmostEqual(abs(arc.center-arcs[0].center),0)
    paths={p.get('id'):p.get('d') for p in root.findall('{*}path')}
    if 'angled' in key:
     self.assertTrue(paths['frame'].startswith('M7 17'))
     self.assertTrue(paths['frame'].endswith('L25 17'))
    else:
     self.assertTrue(paths['rear-fork'].endswith('L7 20'))
     self.assertTrue(paths['front-fork'].endswith('L25 20'))
    self.assertEqual(root.get('stroke-width'),'4');self.assertEqual(r['ink32']['ink_width'],32)
    manifest=json.loads((ROOT/'icon_set/data/combination-sub32.json').read_text())
    self.assertEqual((ROOT/manifest[key.split('/')[1]]['svg']).read_text(),doc)
