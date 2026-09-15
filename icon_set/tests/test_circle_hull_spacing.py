"""Exact detached head clearances; never approve a subminimum gap."""
import unittest
from icon_set.validation.path_commands import Command
from icon_set.validation.stroke_distance import analyze_paths

def scene(points,center=(29,11),radius=5,curve=False):
 x,y=center;r=radius
 return [{'id':'head','commands':[Command('M',[(x-r,y)]),Command('A',[(x+r,y)],(r,r,0,0,1)),Command('A',[(x-r,y)],(r,r,0,0,1)),Command('Z',[])]},
         {'id':'body','commands':[Command('M',[points[0]])]+([Command('C',points[1:])] if curve else [Command('L',[p]) for p in points[1:]])}]

class CircleHullSpacingTests(unittest.TestCase):
 def test_diagonal_exact_gap(self):
  q=analyze_paths(scene([(24,23),(19,35)]));self.assertEqual(q['status'],'pass');self.assertEqual(q['pairs'][0]['lowerBound'],8)
 def test_curved_torso_and_raised_arm_exact(self):
  for points,curve in [([(24,23),(22,27),(20,29),(19,35)],True), ([(24,23),(37,29),(44,12)],False)]:
   self.assertEqual(analyze_paths(scene(points,curve=curve))['status'],'pass')
 def test_narrower_diagonal_gap_never_passes(self):
  for offset in (.1,.001,.000001):
   self.assertNotEqual(analyze_paths(scene([(24,23-offset),(19,35)]))['status'],'pass')
 def test_control_hull_bulge_toward_head_not_ignored(self):
  self.assertNotEqual(analyze_paths(scene([(24,23),(29,10),(29,10),(40,30)],curve=True))['status'],'pass')
 def test_center_inside_hull_proves_nothing(self):
  self.assertNotEqual(analyze_paths(scene([(10,10),(40,10),(40,30),(10,30)],center=(24,20)))['status'],'pass')
 def test_unsupported_arc_does_not_get_circle_hull_proof(self):
  paths=scene([(24,23),(19,35)])
  paths[1]['commands'][1]=Command('A',[(19,35)],(13,13,0,0,1))
  result=analyze_paths(paths)
  self.assertFalse(any('circle/control-hull' in p['reason'] for p in result['pairs']))
 def test_interior_shape_is_not_exterior_clearance(self):
  self.assertNotEqual(analyze_paths(scene([(23,20),(25,20)],center=(24,20),radius=7))['status'],'pass')
 def test_retraced_semicircle_is_not_recognized_as_circle(self):
  paths=scene([(24,23),(19,35)])
  paths[0]['commands'][2]=Command('A',[(24,11)],(5,5,0,0,0))
  result=analyze_paths(paths)
  self.assertFalse(any('circle/control-hull' in p['reason'] for p in result['pairs']))
if __name__=='__main__':unittest.main()
