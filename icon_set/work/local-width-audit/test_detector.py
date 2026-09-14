from pathlib import Path
import sys,unittest,math
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from detector import analyze
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.registry import create

class Probe(Solo48):
 icon_id='width-probe';keyshape=Keyshape.SQUARE
 def build(self):pass

def poly(points):
 p=Probe();p.add_polyline('test',*points);return p

class WidthTests(unittest.TestCase):
 def test_right_angle(self):self.assertEqual(analyze(poly([(6,30),(6,6),(30,6)]))['status'],'pass')
 def test_open_diagonal(self):self.assertEqual(analyze(poly([(6,6),(24,24),(42,6)]))['status'],'pass')
 def test_narrow_strip(self):self.assertEqual(analyze(poly([(6,6),(6,30),(12,30),(12,6)]))['status'],'review')
 def test_roomy_strip(self):self.assertEqual(analyze(poly([(6,6),(6,30),(16,30),(16,6)]))['status'],'pass')
 def test_clean_curve(self):
  p=Probe();p.add_arc('round',(6,24),(24,6),radius_x=18);p.add_line('top',(24,6),(42,6));p.add_contour('test','round','top');self.assertEqual(analyze(p)['status'],'pass')
 def test_subdivision_invariance(self):
  a=analyze(poly([(6,6),(6,30),(12,30),(12,6)]));b=analyze(poly([(6,6),(6,18),(6,30),(9,30),(12,30),(12,18),(12,6)]))
  self.assertEqual(a['status'],b['status']);self.assertEqual([f['ink_gap'] for f in a['findings']],[f['ink_gap'] for f in b['findings']])
 def test_four_reported_defects(self):
  for n in ['anteater-v5','winged-totem-pole','hooded-cobra-v2','hatching-dinosaur-egg-v2']:
   with self.subTest(icon=n):self.assertEqual(analyze(create(n))['status'],'review')
 def test_resolution_stability(self):
  for n in ['anteater-v5','winged-totem-pole','hooded-cobra-v2','hatching-dinosaur-egg-v2']:
   with self.subTest(icon=n):self.assertEqual(analyze(create(n),step=.125)['status'],analyze(create(n),step=.25)['status'])

if __name__=='__main__':unittest.main()
