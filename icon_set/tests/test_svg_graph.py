import unittest

from icon_set.scripts.stroke_edits import normalized_geometry
from icon_set.scripts.svg_graph import graph_from_svg

HEADPHONES = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 54 54" fill="none" stroke="currentColor" stroke-width="4">
  <rect width="54" height="54" fill="white" stroke="none" />
  <g id="band"><path d="M26 6L26 18" /></g>
  <g id="cup">
    <circle cx="26" cy="26" r="8" />
    <circle cx="26" cy="26" r="2" fill="currentColor" stroke="none" />
  </g>
  <g id="marks" fill="currentColor" stroke="none">
    <rect x="4" y="44" width="4" height="4" />
    <rect x="10" y="44" width="12" height="4" />
    <circle cx="40" cy="46" r="3" />
    <circle cx="10" cy="10" r="6" />
  </g>
</svg>'''


class SvgGraphTests(unittest.TestCase):
    def graph(self):
        return graph_from_svg(HEADPHONES, canvas=54, family='main-54', profile='MAIN-5454')

    def test_filled_shapes_are_read_as_the_strokes_that_paint_them(self):
        by_id = {p['element_id']: p for p in self.graph()['primitives']}
        self.assertEqual(by_id['cup.fill-1'], {'kind': 'line', 'element_id': 'cup.fill-1', 'start': [26, 26], 'end': [26, 26]})
        self.assertEqual((by_id['marks.fill-1']['start'], by_id['marks.fill-1']['end']), ([6, 46], [6, 46]))
        self.assertEqual((by_id['marks.fill-2']['start'], by_id['marks.fill-2']['end']), ([12, 46], [20, 46]))
        self.assertEqual((by_id['marks.fill-3']['kind'], by_id['marks.fill-3']['radius_x']), ('arc', 1))
        # The white background and a filled disc wider than two strokes have no stroke that paints them.
        self.assertEqual(sorted(by_id), ['band-1', 'cup-1', 'cup-2', 'cup.fill-1', 'marks.fill-1', 'marks.fill-2',
                                         'marks.fill-3', 'marks.fill-4'])

    def test_a_dot_contour_is_open_so_its_round_caps_paint(self):
        contours = {c['contour_id']: c for c in self.graph()['contours']}
        self.assertEqual(contours['cup.fill-1'], {'contour_id': 'cup.fill-1', 'members': ['cup.fill-1'], 'closed': False})
        self.assertTrue(contours['cup-1']['closed'])

    def test_geometry_saved_before_dots_were_read_keeps_the_base_dots(self):
        graph = self.graph()
        saved = [p for p in graph['primitives'] if '.fill-' not in p['element_id']]
        saved[0] = dict(saved[0], start=[26, 4])
        aligned = normalized_geometry(graph, saved)
        self.assertEqual([p['element_id'] for p in aligned], [p['element_id'] for p in graph['primitives']])
        self.assertEqual(aligned[0]['start'], [26, 4])
        with self.assertRaises(ValueError):  # a missing stroke is still refused
            normalized_geometry(graph, saved[1:])


if __name__ == '__main__':
    unittest.main()
