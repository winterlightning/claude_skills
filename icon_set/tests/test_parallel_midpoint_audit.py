"""Independent synthetic tests for the unapproved midpoint audit prototype."""
import math
import unittest
from icon_set.model.icons.base import Icon
from icon_set.model.profiles import Profile
from icon_set.model.keyshapes import Keyshape
from icon_set.scripts.audit_parallel_midpoints import analyze


def icon():
    return Icon('audit-fixture',Profile.SOLO48,semantic_role='MAIN',keyshape=Keyshape.SQUARE)


class MidpointAuditTests(unittest.TestCase):
    def test_threshold_and_ink_conversion(self):
        for gap in (7,8,9):
            c=icon();c.add_line('a',(0,0),(20,0));c.add_line('b',(0,gap),(20,gap))
            r=analyze(c.draw());self.assertEqual(r['measured_pair_count'],1)
            self.assertEqual(r['below_minimum_pair_count'],int(gap<8))
            self.assertEqual(r['hits'][0]['ink_gap'],gap-4)

    def test_nearest_both_sides_and_reversed_direction(self):
        c=icon()
        for name,y in [('a',0),('b',7),('c',16),('d',30)]: c.add_line(name,(20,y),(0,y))
        r=analyze(c.draw()); middle=next(x for x in r['runs'] if x['members']==['b'])
        hits=[h for h in r['hits'] if h['source']==middle['id']]
        self.assertEqual(sorted(h['centerline_distance'] for h in hits),[7,9])
        self.assertEqual({h['side'] for h in hits},{-1,1})

    def test_diagonal_is_perpendicular_not_horizontal(self):
        c=icon();c.add_line('a',(0,0),(20,20));c.add_line('b',(-4,4),(16,24))
        h=analyze(c.draw())['hits'][0]
        self.assertAlmostEqual(h['centerline_distance'],math.sqrt(32))
        self.assertAlmostEqual((h['end'][0]-h['start'][0])+(h['end'][1]-h['start'][1]),0)

    def test_finite_segments_and_midpoint_blind_spot(self):
        c=icon();c.add_line('a',(0,0),(10,0));c.add_line('b',(8,7),(18,7))
        r=analyze(c.draw());self.assertEqual(r['hits'],[])
        self.assertEqual(r['unmeasured_overlaps'][0]['reason'],'both-midpoints-miss')
        self.assertTrue(r['unmeasured_overlaps'][0]['below_minimum'])

    def test_midpoint_at_endpoint_is_included_and_labeled(self):
        c=icon();c.add_line('a',(0,0),(10,0));c.add_line('b',(5,8),(15,8))
        r=analyze(c.draw());self.assertTrue(all(h['target_endpoint'] for h in r['hits']))

    def test_collinear_touching_same_path_merge_only(self):
        c=icon();c.add_polyline('p',(0,0),(5,0),(10,0));c.add_line('other',(10,0),(20,0))
        r=analyze(c.draw());self.assertEqual(len(r['runs']),2)
        self.assertIn([5,0],[x['midpoint'] for x in r['runs']]);self.assertFalse(r['hits'])

    def test_collinear_overlap_is_separate_from_zero_distance_hit(self):
        c=icon();c.add_line('a',(0,0),(10,0));c.add_line('b',(2,0),(8,0))
        r=analyze(c.draw());self.assertEqual(len(r['collinear_overlaps']),1);self.assertFalse(r['hits'])

    def test_curves_dots_near_parallel_excluded(self):
        c=icon();c.add_line('a',(0,0),(10,0));c.add_line('b',(0,7),(10,8));c.add_dot('dot',(5,5));c.add_arc('arc',(0,10),(10,10),radius_x=5)
        r=analyze(c.draw());self.assertEqual(r['raw_line_count'],2);self.assertFalse(r['hits'])

    def test_connected_paths_not_silently_exempted(self):
        c=icon();c.add_polyline('u',(0,20),(0,0),(7,0),(7,20));c.relate('connect','u','u')
        self.assertEqual(analyze(c.draw())['below_minimum_pair_count'],1)

    def test_ties_and_determinism(self):
        c=icon();c.add_line('a',(0,0),(10,0));c.add_line('b',(0,8),(10,8));c.add_line('c',(0,8),(10,8))
        r=analyze(c.draw());self.assertEqual(r,analyze(c.draw()))
        source=next(x['id'] for x in r['runs'] if x['members']==['a'])
        self.assertEqual(len([h for h in r['hits'] if h['source']==source]),2)


if __name__=='__main__':unittest.main()
