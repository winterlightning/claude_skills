"""Single-pair recombination uses current artwork and persists only its own result."""
import http.client
import json
from unittest.mock import patch
from icon_set.tests.test_stroke_edits import StrokeEditAPITests
from icon_set.scripts import combination_layouts
from icon_set.scripts.icon_artwork import icon_from_graph


class RecombineTests(StrokeEditAPITests):
    def fixture_pair(self):
        self.server.production = True
        gallery = self.dist / 'gallery'
        item = {'icon': 'example', 'family': 'sub', 'model_key': 'sub/example',
                'sha256': 'snapshot', 'document': 'OLD', 'bounds': [2, 2, 28, 28], 'canvas': 32,
                'engine_document': 'OLD ENGINE', 'ink32': {'ink_width': 28}, 'sizing_kind': 'symbol'}
        row = {'id': 'pair-a', 'position': 'br', 'mains': [item], 'subs': [item]}
        (gallery / 'experiment-combination.json').write_text(json.dumps({'rows': [row, dict(row, id='pair-b')]}))
        (gallery / 'experiment-combination-results.json').write_text(json.dumps({'results': {}}))
        combination_layouts.save(dict(row, id='pair-b'), 'example', 'example', None, {'svg': '<svg>other</svg>'})
        return {'pair_id': 'pair-a', 'main': 'example', 'sub': 'example'}

    def test_one_pair_uses_selected_edit_and_survives_restart(self):
        data = self.fixture_pair()
        route = '/api/combinations/side/recombine'
        self.assertEqual(self.call('POST', route, data)[0], 401)
        self.call('POST', '/api/auth/login', {'username': 'jakes', 'password': '1'})
        self.assertEqual(self.call('POST', route, data, origin='https://foreign.example')[0], 403)
        svg = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><path d="M4 4 L28 28"/></svg>'
        other = combination_layouts.load()['pair-b']
        measured = {'icon': 'custom', 'document': svg, 'canvas': 32, 'bounds': [2, 2, 28, 28]}
        result = {'svg': '<svg xmlns="http://www.w3.org/2000/svg">new</svg>',
                  'placements': [{'role': r, 'icon': 'example'} for r in ('main', 'sub')]}
        with patch('icon_set.scripts.deploy.resolve_artwork', return_value={'svg': svg}), \
             patch('icon_set.scripts.side_recombine.custom_item', return_value=measured) as measure, \
             patch('icon_set.scripts.side_recombine.render', return_value=result) as render:
            code, response = self.call('POST', route, data)
        self.assertEqual(code, 200, response)
        self.assertEqual(measure.call_count, 2)
        current = render.call_args.kwargs['row']
        self.assertEqual(current['mains'][0]['document'], svg)
        self.assertNotIn('engine_document', current['mains'][0])
        self.assertEqual(combination_layouts.load()['pair-b'], other)
        self.server.shutdown(); self.server.server_close(); self.start()
        c = http.client.HTTPConnection('127.0.0.1', self.server.server_port)
        c.request('GET', '/gallery/combination-previews/pair-a.svg')
        response = c.getresponse()
        self.assertEqual(response.status, 200)
        self.assertEqual(response.read().decode(), result['svg']); c.close()
        merged = self.call('GET', '/gallery/experiment-combination-results.json')[1]
        self.assertEqual(merged['results']['pair-a']['result'], result)

    def test_invalid_pair_and_failed_render_preserve_saved_results(self):
        data = self.fixture_pair()
        self.call('POST', '/api/auth/login', {'username': 'jakes', 'password': '1'})
        previous = combination_layouts.path().read_bytes()
        route = '/api/combinations/side/recombine'
        self.assertEqual(self.call('POST', route, dict(data, main='wrong'))[0], 422)
        with patch('icon_set.scripts.deploy.GalleryHandler.side_current_document', return_value='OLD'), \
             patch('icon_set.scripts.side_recombine.render', side_effect=ValueError('Cannot render')):
            self.assertEqual(self.call('POST', route, data)[0], 422)
        self.assertEqual(combination_layouts.path().read_bytes(), previous)
