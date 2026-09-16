"""Manual artwork survives source builds and can be switched back without data loss."""
from contextlib import redirect_stdout
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from icon_set.scripts.icon_artwork import ArtworkStore, safe_svg, resolve_artwork, baseline, sha, icon_from_graph
from icon_set.scripts.stroke_edits import StrokeEditStore, EditConflict
from icon_set.scripts import build as builder
from icon_set.tests.test_edit_validation import portrait
from icon_set.tests.test_stroke_edits import StrokeEditAPITests

SVG = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48"><path d="M10 10H38V38H10Z" fill="#123456"/></svg>'


class ArtworkTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(); self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.store = ArtworkStore(self.root/'artwork')
        self.edits = StrokeEditStore(self.root/'edits')
        self.icon = portrait()
        self.icon['svg_sha256'] = sha(icon_from_graph(self.icon).to_svg())
        self.data = {'svg_sha256': self.icon['svg_sha256'], 'revision': 0, 'source_mode': 'use_upload', 'svg': SVG, 'filename': 'manual.svg'}

    def test_upload_switch_original_and_restart(self):
        saved = self.store.save(self.icon, self.data, 'jakes', self.edits)
        self.assertEqual(saved['uploaded']['uploaded_by'], 'jakes')
        selected = resolve_artwork(self.icon, saved)
        self.assertEqual(selected['svg_sha256'], sha(selected['svg']))
        self.assertEqual(ArtworkStore(self.store.root).get(self.icon['key']), saved)
        original = self.store.save(self.icon, {'svg_sha256': self.icon['svg_sha256'], 'revision': 1, 'source_mode': 'use_org'}, 'hina', self.edits)
        self.assertIsNone(resolve_artwork(self.icon, original))
        self.assertEqual(original['uploaded'], saved['uploaded'])
        restored = self.store.save(self.icon, {'svg_sha256': self.icon['svg_sha256'], 'revision': 2, 'source_mode': 'use_upload'}, 'hina', self.edits)
        self.assertEqual(resolve_artwork(self.icon, restored)['svg'], selected['svg'])
        with self.assertRaises(EditConflict):
            self.store.save(self.icon, self.data, 'jakes', self.edits)
        with self.assertRaises(EditConflict):
            self.store.save(self.icon, self.data | {'svg_sha256': 'stale'}, 'jakes', self.edits)

    def test_svg_rejects_active_external_empty_or_wrong_canvas(self):
        for content in [SVG.replace('<path ', '<path onclick="alert(1)" '),
                        SVG.replace('<path ', '<image href="https://example.com/x"/><path '),
                        SVG.replace('<path ', '<use href="file:///tmp/private"/><path '),
                        SVG.replace('<path ', '<script>alert(1)</script><path '),
                        SVG.replace('<path ', '<style>@import "https://example.com/x";</style><path '),
                        SVG.replace('fill="#123456"', 'fill="url(https://example.com/x)"'),
                        SVG.replace('0 0 48 48', '0 0 32 32'),
                        '<!DOCTYPE svg>'+SVG,
                        '<svg viewBox="0 0 48 48"/>', '<html/>', 'x'*1048577]:
            with self.subTest(content=content[:100]), self.assertRaises(ValueError):
                safe_svg(content, 48)
        styled = SVG.replace('<path ', '<style>.ink { fill: #123456; opacity: .7; }</style><path class="ink" ')
        self.assertIn('.ink', safe_svg(styled, 48))

    def test_edited_requires_saved_acceptance_and_keeps_snapshot(self):
        request = {'svg_sha256': self.icon['svg_sha256'], 'revision': 0, 'offsets': {}, 'keyshape': 'VRECT_M', 'validate': True}
        edit = self.edits.save(self.icon, request, 'jakes')
        choice = {'svg_sha256': self.icon['svg_sha256'], 'revision': 0, 'source_mode': 'use_edited', 'edit_revision': 1}
        with self.assertRaises(ValueError):
            self.store.save(self.icon, choice, 'jakes', self.edits)
        edit = self.edits.save(self.icon, request | {'revision': 1, 'validation_override': {'reason': 'Visually accepted proportions'}}, 'jakes')
        saved = self.store.save(self.icon, choice | {'edit_revision': 2}, 'jakes', self.edits)
        selected = resolve_artwork(self.icon, saved)
        self.assertEqual(selected['graph']['keyshape'], 'VRECT_M')
        self.assertEqual(selected['automatic_status'], 'fail')
        self.edits.save(self.icon, request | {'revision': 2, 'offsets': {'contour:outline': [1, 0]}, 'validation_override': None}, 'jakes')
        self.assertEqual(resolve_artwork(self.icon, self.store.get(self.icon['key'])), selected)

    def build(self, icon, *, all=False, report=False):
        with patch.object(builder, 'icons_in', return_value=[icon]), \
             patch('icon_set.model.icons.registry.all_icons', return_value=[icon]), \
             patch.object(builder, 'stage_gallery', side_effect=self.gallery), redirect_stdout(io.StringIO()):
            return builder.build(self.root/'dist', self.root/'png', write_png=True, only=['solo'],
                                 report=report, rebuild_all=all, artwork_dir=self.store.root)

    def gallery(self, staging, published, folders):
        target = staging/'gallery'; target.mkdir(exist_ok=True); (target/'index.html').write_text('fixture'); return target

    def test_python_build_exports_selected_svg_png_and_restores_original(self):
        model = icon_from_graph(self.icon)
        saved = self.store.save(self.icon, self.data, 'jakes', self.edits)
        expected = saved['uploaded']['svg']
        for full in (False, True):
            self.assertEqual(self.build(model, all=full, report=True), 0)
            self.assertEqual((self.root/'dist/solo48/editor-experiment.svg').read_text(), expected)
            from PIL import Image
            with Image.open(self.root/'png/solo48/editor-experiment.png') as image:
                self.assertEqual(image.convert('RGB').getpixel((20,20)), (18,52,86))
        record = json.loads((self.root/'dist/solo48/manifest.json').read_text())['icons'][0]
        self.assertEqual(record['artwork_source'], 'use_upload')
        self.assertEqual(record['validation']['status'], 'human-selected')
        self.assertEqual(baseline(record)['primitives'], self.icon['primitives'])
        # Authored geometry changes do not overwrite the explicitly chosen manual artwork.
        model.add_line('extra', (4, 4), (8, 4))
        self.assertEqual(self.build(model), 0)
        self.assertEqual((self.root/'dist/solo48/editor-experiment.svg').read_text(), expected)
        self.store.save(self.icon, self.data | {'revision': 1, 'source_mode': 'use_org'}, 'jakes', self.edits)
        self.assertEqual(self.build(icon_from_graph(self.icon)), 0)
        self.assertEqual((self.root/'dist/solo48/editor-experiment.svg').read_text(), icon_from_graph(self.icon).to_svg())

    def test_python_build_honors_forced_gallery_edit(self):
        self.edits.save(self.icon, {'svg_sha256': self.icon['svg_sha256'], 'revision': 0,
                        'offsets': {}, 'keyshape': 'VRECT_M', 'validation_override': {'reason': 'Intentional proportions'}}, 'jakes')
        saved = self.store.save(self.icon, {'svg_sha256': self.icon['svg_sha256'], 'revision': 0,
                               'source_mode': 'use_edited', 'edit_revision': 1}, 'jakes', self.edits)
        self.assertEqual(self.build(icon_from_graph(self.icon), report=True), 0)
        record = json.loads((self.root/'dist/solo48/manifest.json').read_text())['icons'][0]
        self.assertEqual(record['keyshape'], 'VRECT_M')
        self.assertEqual(record['validation']['automatic_status'], 'fail')
        self.assertTrue(record['validation']['errors'])
        self.assertEqual((self.root/'dist/solo48/editor-experiment.svg').read_text(), resolve_artwork(self.icon,saved)['svg'])


class ArtworkAPITests(StrokeEditAPITests):
    def test_upload_api_auth_storage_and_live_catalog(self):
        icon = portrait()
        (self.dist/'gallery/icons.json').write_text(json.dumps({'icons':[icon]}))
        route = '/api/icon-artwork'
        data = {'icon': icon['key'], 'svg_sha256':'fixture', 'revision':0, 'source_mode':'use_upload', 'svg':SVG}
        self.assertEqual(self.call('POST',route,data)[0],401)
        self.call('POST','/api/auth/login',{'username':'jakes','password':'1'})
        self.assertEqual(self.call('POST',route,data,origin='https://foreign.example')[0],403)
        status, saved = self.call('POST',route,data)
        self.assertEqual(status,200,saved)
        self.assertEqual(saved['choice']['source_mode'],'use_upload')
        row = self.call('GET','/gallery/icons.json')[1]['icons'][0]
        self.assertEqual(row['artwork_source'],'use_upload')
        self.assertNotEqual(row['svg_sha256'], 'fixture')
        self.assertEqual(row['generated_svg_sha256'],'fixture')
        import http.client
        connection = http.client.HTTPConnection('127.0.0.1',self.server.server_port)
        connection.request('GET','/api/icon-artwork/svg?icon=solo/editor-experiment')
        response = connection.getresponse()
        self.assertEqual(response.status,200)
        self.assertIn('sandbox',response.getheader('Content-Security-Policy'))
        self.assertEqual(response.read().decode(),saved['choice']['uploaded']['svg'])
        connection.close()

        self.assertEqual(self.call('GET','/api/stroke-edits?icon=solo/editor-experiment')[1]['svg_sha256'],'fixture')
        self.assertEqual(self.call('POST',route,data)[0],409)
        self.assertFalse(list(self.dist.rglob('artwork.json')))
        self.server.shutdown();self.server.server_close();self.start()
        row = self.call('GET','/gallery/icons.json')[1]['icons'][0]
        self.assertEqual(row['artwork_source'],'use_upload')


if __name__=='__main__':
    unittest.main()
