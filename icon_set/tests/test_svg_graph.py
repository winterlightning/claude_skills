import unittest
from copy import deepcopy
import xml.etree.ElementTree as ET

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
    def test_custom_family_saved_edit_renders_in_pick_and_selected_artwork(self):
        from cloud.graphics.server import render
        from icon_set.scripts.icon_artwork import resolve_artwork, sha
        from icon_set.scripts.edit_validation import svg_from_graph, icon_from_graph
        from icon_set.scripts.stroke_edits import graph_sha256

        for family, canvas, profile in [
            ('solo-64', 64, 'SOLO-6464'), ('icon-72', 72, 'ICON-7272'), ('container-72', 72, 'CONTAINER-7272'),
            ('main-54', 54, 'MAIN-5454'), ('sub-36', 36, 'SUB-3636'), ('symbol-36', 36, 'SYMBOL-3636'),
            ('side_combination64', 64, 'SIDE_COMBINATION64'), ('combination-72', 72, 'SIDE_COMBINATION72'),
            ('container_combination64', 64, 'CONTAINER_COMBINATION64'),
            ('container-combination-72', 72, 'CONTAINER_COMBINATION72'), ('text', 64, 'TEXT_COMBINATION64'),
            ('custom', 74, 'CUSTOM74'),
        ]:
            with self.subTest(family=family):
                graph = graph_from_svg(HEADPHONES, canvas=canvas, family=family, profile=profile, icon_id='saved-edit')
                graph['primitives'][0]['start'] = [26, 4]  # saved edit differs from the original
                before = deepcopy(graph)
                preview = render(graph)
                root = ET.fromstring(preview['svg'])
                self.assertEqual(root.get('viewBox'), f'0 0 {canvas} {canvas}')
                self.assertEqual(root.get('stroke-width'), '4')
                paths = {p.get('id'): p.get('d') for p in root.findall('{http://www.w3.org/2000/svg}path')}
                self.assertEqual(paths['band-1'], 'M26 4L26 18')
                self.assertEqual(paths['cup.fill-1'], 'M26 26L26 26')
                self.assertTrue(paths['cup-1'].endswith('Z'))
                self.assertEqual(preview['svg_sha256'], sha(preview['svg']))
                choice = {'source_mode': 'use_edited', 'edited': {'edited_graph': graph,
                          'validation': {'status': 'pass', 'graph_sha256': graph_sha256(graph)}}}
                self.assertEqual(resolve_artwork(graph, choice)['svg'], preview['svg'])
                self.assertEqual(graph, before)
                # Previewing does not silently give custom families a build-validation profile.
                with self.assertRaises(KeyError):
                    icon_from_graph(graph)
                choice['edited']['validation']['status'] = 'not-run'
                with self.assertRaises(ValueError):
                    resolve_artwork(graph, choice)

        # Built-in profiles retain byte-identical SVGs and hashes.
        from icon_set.tests.test_edit_validation import portrait
        built = portrait()
        self.assertEqual(svg_from_graph(built), icon_from_graph(built).to_svg())

    def test_preview_keeps_loose_strokes_when_a_contour_reuses_their_id(self):
        from icon_set.scripts.edit_validation import svg_from_graph
        graph = self.graph()
        graph['contours'] = [c for c in graph['contours'] if c['contour_id'] != 'band-1']
        graph['contours'][0]['contour_id'] = 'band-1'
        before = deepcopy(graph)
        root = ET.fromstring(svg_from_graph(graph))
        paths = root.findall('{http://www.w3.org/2000/svg}path')
        ids = [p.get('id') for p in paths]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertIn('band-1', ids)
        self.assertIn('contour-band-1', ids)
        self.assertEqual(graph, before)

    def test_custom_graph_rejects_invalid_canvas_and_stroke_width(self):
        from icon_set.scripts.edit_validation import svg_from_graph
        graph = self.graph()
        for canvas in [None, 0, 257, 64.5, '64', True]:
            with self.subTest(canvas=canvas), self.assertRaises(ValueError):
                svg_from_graph(graph | {'canvas_size': canvas})
        for width in [0, -1, float('nan'), float('inf'), '4', True]:
            with self.subTest(width=width), self.assertRaises(ValueError):
                svg_from_graph(graph | {'style': {'stroke_width': width}})

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
