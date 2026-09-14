import unittest

from icon_set.model.icons.base import Icon
from icon_set.model.keyshapes import Keyshape
from icon_set.model.path_repair import repair_paths, transform_paths, _preserves_straight_edges, visible_hole_count
from icon_set.model.primitives import Point
from icon_set.model.profiles import Profile


def fixture():
    i=Icon('repair-test',Profile.SOLO48,semantic_role='MAIN',keyshape=Keyshape.SQUARE)
    i.family='solo';i.semantic_kind='noun'
    i.add_polyline('outline',(6,6),(42,6),(42,42),(6,42),closed=True)
    i.add_line('detail',(10,24),(38,24))
    return i


class PathRepairTests(unittest.TestCase):
    def test_shortens_crowded_inner_path_without_changing_outline(self):
        icon=fixture();before=icon.to_record()
        candidate,qa,log=repair_paths(icon,max_evaluations=180)
        self.assertEqual(qa['status'],'pass',qa['errors'])
        self.assertEqual(candidate.primitives[:-1],icon.primitives[:-1])
        detail=candidate.primitives[-1]
        self.assertGreaterEqual(detail.start.x,14)
        self.assertLessEqual(detail.end.x,34)
        self.assertEqual(icon.to_record(),before)
        self.assertTrue(log['changes'])

    def test_shared_vertices_move_together(self):
        icon=fixture()
        candidate=transform_paths(icon,{'outline-1'},dy=1)
        self.assertEqual(candidate.primitives[0].start,candidate.primitives[3].end)
        self.assertEqual(candidate.primitives[0].end,candidate.primitives[1].start)
        self.assertEqual(icon.primitives[0].start,Point(6,6))

    def test_new_vertex_merges_are_rejected(self):
        icon=fixture();icon.add_dot('dot',(11,24))
        with self.assertRaisesRegex(ValueError,'merge'):
            transform_paths(icon,{'detail'},dx=1)

    def test_partial_movement_cannot_bypass_parallel_rule_by_tilting(self):
        icon=fixture()
        candidate=transform_paths(icon,{'outline-1'},dx=1)
        self.assertFalse(_preserves_straight_edges(icon,candidate))

    def test_zero_budget_preserves_geometry_and_failure(self):
        icon=fixture();candidate,qa,log=repair_paths(icon,max_evaluations=0)
        self.assertEqual(candidate.primitives,icon.primitives)
        self.assertEqual(log['evaluations'],0)
        self.assertEqual(qa['status'],'fail')

    def test_visible_ring_must_not_become_a_solid_dot(self):
        def ring(radius):
            return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48">'
                    f'<circle cx="24" cy="24" r="{radius}" fill="none" stroke="black" stroke-width="4"/></svg>')
        self.assertEqual(visible_hole_count(ring(3)),1)
        self.assertEqual(visible_hole_count(ring(2)),0)


if __name__=='__main__':unittest.main()
