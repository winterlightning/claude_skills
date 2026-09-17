"""New SVG uploads enter the existing version-bound review workflow."""
import http.client
import json
import sqlite3
import unittest
from icon_set.tests import test_review_workflow as fixture
from icon_set.scripts.icon_artwork import resolve_artwork


class IconUploadTests(unittest.TestCase):
    setUp = fixture.ReviewWorkflowTests.setUp
    start = fixture.ReviewWorkflowTests.start
    call = fixture.ReviewWorkflowTests.call
    login = fixture.ReviewWorkflowTests.login
    svg = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48"><circle cx="24" cy="24" r="16"/></svg>'

    def upload(self, **overrides):
        return self.call('POST', '/api/icons/upload', dict(name='Test upload', family='solo', svg=self.svg, **overrides))

    def test_upload_review_restart_and_rebuild(self):
        self.login()
        status, result = self.upload()
        self.assertEqual(status, 201, result)
        icon = result['record']
        key = icon['key']
        self.assertEqual(result['status'], 'ready')
        self.assertEqual(icon['author'], 'jakes')
        self.assertEqual(self.call('GET', '/api/reviews')[1][key], 'ready')
        catalog = self.call('GET', '/gallery/icons.json')[1]['icons']
        self.assertIn(key, [row['key'] for row in catalog])
        self.assertNotIn('uploaded_svg', catalog[-1])
        connection = http.client.HTTPConnection('127.0.0.1', self.server.server_port)
        connection.request('GET', '/api/icon-artwork/svg?icon='+key)
        response = connection.getresponse()
        self.assertEqual(response.status, 200)
        self.assertIn(b'circle', response.read())
        connection.close()
        review = dict(icon=key, svg_sha256=icon['svg_sha256'], status='approve')
        self.assertEqual(self.call('POST', '/api/reviews', dict(review, svg_sha256='stale'))[0], 409)
        self.assertEqual(self.call('POST', '/api/reviews', review)[0], 201)
        self.assertEqual(self.call('GET', '/api/reviews')[1][key], 'approve')
        self.assertEqual(self.call('POST', '/api/reviews', dict(review, status='disapprove', reason='meaning'))[0], 201)
        self.assertEqual(self.call('GET', '/api/reviews')[1][key], 'pending')
        self.assertEqual(self.call('GET', '/api/feedback?icon='+key)[1][0]['reason'], 'meaning')
        # A gallery rebuild may replace its catalog; uploads live beside reviews.
        (self.dist/'gallery/icons.json').write_text(json.dumps({'icons': []}))
        self.server.shutdown()
        self.start()
        self.assertEqual(self.call('GET', '/api/reviews')[1][key], 'pending')
        self.assertEqual(self.call('GET', '/gallery/icons.json')[1]['icons'][0]['key'], key)

    def test_invalid_svg_never_creates_an_icon(self):
        self.login()
        invalid = [self.svg.replace('48 48', '32 32'), self.svg.replace('<circle', '<script/> <circle'),
                   '<svg viewBox="0 0 48 48"/>', '<not-svg/>', 'x'*(1024*1024+1)]
        for svg in invalid:
            status, result = self.call('POST', '/api/icons/upload', dict(name='Unsafe',family='solo',svg=svg))
            self.assertEqual(status, 400, result)
        for extra in ({'name':''}, {'family':'bad'}, {'family':[]}, {'category':[]}):
            data = dict(name='Test', family='solo',svg=self.svg)
            data.update(extra)
            self.assertEqual(self.call('POST','/api/icons/upload',data)[0],400)
        with sqlite3.connect(self.database) as db:
            self.assertEqual(db.execute('SELECT count(*) FROM uploaded_icons').fetchone()[0],0)

    def test_same_names_create_independent_icons_and_original_is_preserved(self):
        self.login()
        first = self.upload()[1]['record']
        second = self.upload()[1]['record']
        self.assertNotEqual(first['key'], second['key'])
        with sqlite3.connect(self.database) as db:
            record, svg = db.execute('SELECT record,svg FROM uploaded_icons WHERE icon=?',(first['key'],)).fetchone()
        original = dict(json.loads(record), uploaded_svg=svg)
        self.assertEqual(resolve_artwork(original, None)['svg'],svg)
        self.assertEqual(resolve_artwork(original, None, variant='use_org')['svg'],svg)
        # Manual replacement remains available for fixing uploaded icons.
        payload = dict(icon=first['key'],svg_sha256=first['svg_sha256'],revision=0,source_mode='use_org',
                       action='upload',svg=self.svg.replace('r="16"','r="12"'))
        status, saved = self.call('POST','/api/icon-artwork',payload)
        self.assertEqual(status,200,saved)
        self.assertEqual(self.call('GET','/api/reviews')[1][first['key']],'ready')

        status, picked = self.call('POST', '/api/icon-artwork', dict(icon=first['key'],
            svg_sha256=first['svg_sha256'], revision=1, source_mode='use_upload'))
        self.assertEqual(status, 200, picked)
        self.assertNotEqual(picked['record']['svg_sha256'],first['svg_sha256'])
        status, restored = self.call('POST', '/api/icon-artwork', dict(icon=first['key'],
            svg_sha256=first['svg_sha256'], revision=2, source_mode='use_org'))
        self.assertEqual(status, 200, restored)
        self.assertEqual(restored['record']['svg_sha256'],first['svg_sha256'])

    def test_all_family_canvases_and_cross_origin_protection(self):
        self.login()
        for family, size in [('sub',32),('solo',48),('container',64)]:
            data = dict(name='Canvas', family=family, svg=self.svg.replace('48 48',f'{size} {size}'))
            self.assertEqual(self.call('POST','/api/icons/upload',data,origin='https://example.com')[0],403)
            status, result = self.call('POST','/api/icons/upload',data)
            self.assertEqual(status,201,result)
            self.assertEqual(result['record']['canvas_size'],size)

    def test_category_default_and_uploaded_type_with_custom_category(self):
        self.login()
        keys = []
        for payload, expected in [({}, 'manual_upload'), ({'category': ''}, 'manual_upload'),
                                  ({'category': '   '}, 'manual_upload'), ({'category': ' Animals '}, 'Animals')]:
            status, result = self.upload(**payload)
            self.assertEqual(status, 201, result)
            record = result['record']
            keys.append(record['key'])
            self.assertEqual(record['category'], expected)
            self.assertEqual(record['icon_type'], 'uploaded')
            self.assertEqual(result['status'], 'ready')
            saved_type = self.call('GET', '/api/icon-type?icon='+record['key'])[1]
            self.assertEqual(saved_type['icon_type'], 'uploaded')
            self.assertEqual(saved_type['updated_by'], 'jakes')
        listed = self.call('GET', '/api/icon-types?type=uploaded&status=ready')[1]['icons']
        self.assertEqual({row['icon'] for row in listed}, set(keys))
        catalog = self.call('GET', '/gallery/icons.json')[1]['icons']
        self.assertEqual([row['category'] for row in catalog if row['key'] in keys],
                         ['manual_upload', 'manual_upload', 'manual_upload', 'Animals'])

    def test_anonymous_upload_is_ready_but_review_still_requires_login(self):
        status, result = self.upload()
        self.assertEqual(status, 201, result)
        icon = result['record']
        self.assertEqual(icon['author'], 'anonymous')
        self.assertEqual(icon['category'], 'manual_upload')
        self.assertEqual(icon['icon_type'], 'uploaded')
        self.assertEqual(self.call('GET', '/api/reviews')[1][icon['key']], 'ready')
        review = dict(icon=icon['key'], svg_sha256=icon['svg_sha256'], status='approve')
        self.assertEqual(self.call('POST', '/api/reviews', review)[0], 401)
        self.login()
        self.assertEqual(self.call('POST', '/api/reviews', review)[0], 201)

    def test_optional_validation_default_types_and_failures(self):
        from unittest.mock import patch
        with patch('icon_set.validation.library_qa.measure_negative_space') as checker:
            status, result = self.upload()
            self.assertEqual(status, 201)
            self.assertTrue(result['record']['bypass_validation'])
            self.assertEqual(result['record']['validation']['status'], 'not-run')
            checker.assert_not_called()
        for value in ('false', 0, 1, None, [], {}):
            self.assertEqual(self.upload(bypass_validation=value)[0], 400)
        ring = self.svg.replace('r="16"', 'r="16" fill="none" stroke="black" stroke-width="4"')
        status, result = self.call('POST', '/api/icons/upload', dict(name='Ring',family='solo',svg=ring,bypass_validation=False))
        self.assertEqual(status, 201, result)
        self.assertEqual(result['record']['validation']['status'], 'pass')
        self.assertIn('holes/pinches',result['record']['validation']['checks_run'])
        self.assertEqual(result['status'], 'ready')
        with sqlite3.connect(self.database) as db:
            before = db.execute('SELECT count(*) FROM uploaded_icons').fetchone()[0]
        tiny = ring.replace('r="16"', 'r="2.5"')
        status, result = self.call('POST', '/api/icons/upload', dict(name='Tiny hole',family='solo',svg=tiny,bypass_validation=False))
        self.assertEqual(status, 422, result)
        self.assertEqual(result['validation']['status'], 'fail')
        with patch('icon_set.validation.library_qa.measure_negative_space', side_effect=RuntimeError('checker offline')):
            status, result = self.upload(bypass_validation=False)
            self.assertEqual(status, 503, result)
            self.assertEqual(result['validation']['status'], 'error')
        with sqlite3.connect(self.database) as db:
            self.assertEqual(db.execute('SELECT count(*) FROM uploaded_icons').fetchone()[0], before)
        # Bypassing optional QA never bypasses static SVG safety checks.
        for bypass in (True,False):
            status, _ = self.call('POST','/api/icons/upload',dict(name='Unsafe',family='solo',
                svg=self.svg.replace('<circle','<script/> <circle'),bypass_validation=bypass))
            self.assertEqual(status,400)

    def test_category_suggestions_include_current_catalog_and_new_uploads(self):
        (self.dist/'gallery/icons.json').write_text(json.dumps({
            'icons': [dict(self.icon, category='Animals'), dict(self.icon, category='Animals')],
            'failed_icons': [dict(self.icon, category='Tools'), dict(self.icon, category='  ')]}))
        status, data = self.call('GET', '/api/icon-categories')
        self.assertEqual(status, 200)
        self.assertEqual(data['categories'], ['Animals', 'manual_upload', 'Tools'])
        self.assertEqual(self.upload(category='New category')[0], 201)
        categories = self.call('GET', '/api/icon-categories')[1]['categories']
        self.assertIn('New category', categories)
        self.assertEqual(len(categories), len(set(categories)))
