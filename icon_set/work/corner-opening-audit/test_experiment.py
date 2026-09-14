from pathlib import Path
import sys,unittest,numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parents[3]))
from experiment import analyze,get_arms
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
class Probe(Solo48):
 icon_id='corner-probe';keyshape=Keyshape.SQUARE
 def build(self):pass

def make(pts):
 p=Probe();p.add_polyline('test',*pts);return p
class Tests(unittest.TestCase):
 def test_right_angle(self):
  r=analyze(make([(0,24),(0,0),(24,0)]));self.assertEqual(r[0]['measurements']['16']['status'],'clear');self.assertAlmostEqual(r[0]['measurements']['16']['centerline_distance'],16)
 def test_thirty_degrees(self):
  # Floating-point geometry is allowed only in this mathematical test fixture.
  r=analyze(make([(24,0),(0,0),(24*np.cos(np.pi/6),24*np.sin(np.pi/6))]));self.assertAlmostEqual(r[0]['measurements']['16']['centerline_distance'],8,places=3);self.assertEqual(r[0]['measurements']['16']['status'],'clear');self.assertEqual(r[0]['measurements']['8']['status'],'narrow')
 def test_short(self):self.assertEqual(analyze(make([(0,3),(0,0),(5,0)]))[0]['measurements']['16']['status'],'short-narrow')
 def test_split(self):
  a=analyze(make([(0,24),(0,0),(24,0)]));b=analyze(make([(0,24),(0,12),(0,0),(12,0),(24,0)]));self.assertEqual(a[0]['measurements'],b[0]['measurements']);self.assertEqual(len(b),1)
 def test_smooth_join(self):
  p=Probe();p.add_arc('curve',(0,10),(10,0),radius_x=10);p.add_line('straight',(10,0),(24,0));p.add_contour('path','curve','straight');self.assertEqual(analyze(p),[])
if __name__=='__main__':unittest.main()
