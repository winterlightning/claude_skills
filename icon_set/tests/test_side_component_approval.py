"""Side pages approve exact drawings and show saved edits without a rebuild."""
import json
from icon_set.tests.test_stroke_edits import StrokeEditAPITests
from icon_set.tests.test_edit_validation import portrait
from icon_set.scripts.icon_artwork import icon_from_graph, sha
from icon_set.scripts.side_components import _drawing
from icon_set.scripts.gallery import failed_editor_graph


class SideApprovalTests(StrokeEditAPITests):
    def fixture(self):
        icon = portrait()
        icon.update(svg_sha256=sha(icon_from_graph(icon).to_svg()), build_failed=True,
                    status='fail', errors=['spacing: intentionally close'], preview_url='../failed/example.svg')
        self.write_icon(icon)
        item = {'id': 'source', 'concept': 'Example', 'drawings': [_drawing(icon, True)], 'uses': 1}
        (self.dist/'gallery/side-components.json').write_text(json.dumps({
            'mains': [item], 'subs': [], 'counts': {'main': {}, 'sub': {}}, 'generated_at': '2026-09-25'}))
        return icon

    def write_icon(self, icon):
        (self.dist/'gallery/icons.json').write_text(json.dumps({'icons': [], 'failed_icons': [icon]}))

    def test_exception_survives_restart_but_not_changed_drawing(self):
        icon = self.fixture()
        payload = {'icon': icon['key'], 'svg_sha256': icon['svg_sha256'], 'revision': 0,
                   'source_mode': 'use_org', 'approve_exception': True}
        self.assertEqual(self.call('POST', '/api/icon-artwork', dict(payload, svg_sha256='stale'))[0], 409)
        review = {'icon': icon['key'], 'svg_sha256': icon['svg_sha256']}
        self.assertEqual(self.call('POST', '/api/reviews', dict(review, status='rejected'))[0], 201)
        self.assertEqual(self.call('POST', '/api/reject-combination/restore', review)[0], 200)
        code, result = self.call('POST', '/api/icon-artwork', payload)
        self.assertEqual(code, 200, result)
        self.assertEqual(result['record']['review_status'], 'approve')
        self.assertEqual(result['record']['validation']['automatic_status'], 'fail')
        self.server.shutdown(); self.server.server_close(); self.start()
        for route in ('/api/side-components', '/gallery/side-components.json'):
            code, data = self.call('GET', route)
            self.assertEqual(code, 200, data)
            drawing = data['mains'][0]['drawings'][0]
            self.assertEqual(drawing['status'], 'pass')
            self.assertEqual(drawing['exception']['svg_sha256'], icon['svg_sha256'])
            self.assertEqual(drawing['errors'], icon['errors'])
            self.assertEqual(data['counts']['main']['failing'], 0)
        catalog = self.call('GET', '/gallery/icons.json')[1]
        self.assertEqual(len(catalog['icons']), 1)
        self.assertEqual(catalog['failed_icons'], [])
        # An updated export does not inherit an old human exception.
        icon['svg_sha256'] = 'new-drawing'
        self.write_icon(icon)
        drawing = self.call('GET', '/api/side-components')[1]['mains'][0]['drawings'][0]
        self.assertEqual(drawing['status'], 'fail')
        self.assertFalse(drawing['exception'])

    def test_selected_browser_edit_replaces_failed_original_live(self):
        icon = self.fixture()
        edit = self.server.stroke_edits.save(icon, {
            'svg_sha256': icon['svg_sha256'], 'revision': 0, 'offsets': {'contour:outline': [1, 0]}, 'keyshape': 'VRECT_M',
            'validation_override': {'reason': 'Visually reviewed'},
        }, 'jakes')
        payload = {'icon': icon['key'], 'svg_sha256': icon['svg_sha256'], 'revision': 0,
                   'source_mode': 'use_edited', 'edit_revision': edit['revision']}
        code, result = self.call('POST', '/api/icon-artwork', payload)
        self.assertEqual(code, 200, result)
        drawing = self.call('GET', '/api/side-components')[1]['mains'][0]['drawings'][0]
        self.assertEqual(drawing['status'], 'pass')
        self.assertTrue(drawing['exception'])
        self.assertEqual(drawing['svg_sha256'], result['record']['svg_sha256'])
        self.assertNotEqual(drawing['svg_sha256'], icon['svg_sha256'])
        self.assertIn('/api/icon-artwork/svg?', drawing['preview_url'])
        self.assertEqual(self.call('GET', '/api/reviews')[1][icon['key']], 'approve')

    def test_exception_rejects_wrong_stroke_and_checker_errors(self):
        icon = self.fixture()
        for change in ({'style': dict(icon['style'], stroke_width=3)}, {'status': 'error'}):
            invalid = dict(icon, **change)
            invalid['svg_sha256'] = sha(icon_from_graph(invalid).to_svg())
            self.write_icon(invalid)
            code, result = self.call('POST', '/api/icon-artwork', {
                'icon': icon['key'], 'svg_sha256': invalid['svg_sha256'], 'revision': 0,
                'source_mode': 'use_org', 'approve_exception': True})
            self.assertEqual(code, 400, result)
            self.assertIsNone(self.server.artwork.get(icon['key']))

    def test_sub32_exception_uses_the_same_approval_path(self):
        from icon_set.model.icons.base import Icon
        from icon_set.model.profiles import Profile
        from icon_set.model.keyshapes import Keyshape
        model = Icon('sub-example', Profile.SUB32, semantic_role='MODIFIER', keyshape=Keyshape.CIRCLE)
        model.family = 'sub'
        model.add_polyline('outline', (4, 4), (28, 4), (28, 28), (4, 28), closed=True)
        icon = model.to_record() | {'key': 'sub/sub-example'}
        icon.update(svg_sha256=sha(icon_from_graph(icon).to_svg()), build_failed=True, status='fail')
        self.write_icon(icon)
        code, result = self.call('POST', '/api/icon-artwork', {
            'icon': icon['key'], 'svg_sha256': icon['svg_sha256'], 'revision': 0,
            'source_mode': 'use_org', 'approve_exception': True})
        self.assertEqual(code, 200, result)
        self.assertEqual(result['record']['validation']['status'], 'human-selected')
        self.assertEqual(result['record']['canvas_size'], 32)

    def test_editor_graph_never_describes_a_different_export(self):
        icon = self.fixture()
        factory = lambda: icon_from_graph(icon)
        self.assertTrue(failed_editor_graph(factory, icon)['primitives'])
        self.assertEqual(failed_editor_graph(factory, dict(icon, svg_sha256='stale')), {})
