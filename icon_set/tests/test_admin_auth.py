"""Exercise admin access at the HTTP boundary without running generation."""
import hashlib
import http.client
import json
from pathlib import Path
import sqlite3
import tempfile
import threading
import unittest
from unittest.mock import Mock

from icon_set.scripts.deploy import create_server


class AdminAuthTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        root = Path(self.tmp.name)
        self.db = root / 'feedback.sqlite3'
        dist = root / 'dist'
        gallery = dist / 'gallery'
        gallery.mkdir(parents=True)
        for page in ('index', 'home', 'login', 'generate'):
            (gallery / (page+'.html')).write_text(page)
        (gallery / 'icons.json').write_text('{"icons": []}')
        self.server = create_server(dist, self.db, port=0)
        self.server.generation = Mock()
        self.server.generation.listing.return_value = []
        threading.Thread(target=self.server.serve_forever, daemon=True).start()
        self.addCleanup(self.server.server_close)
        self.addCleanup(self.server.shutdown)

    def request(self, path, data=None, cookie=None, method=None, origin=None):
        connection = http.client.HTTPConnection('127.0.0.1', self.server.server_port)
        headers = {'Content-Type': 'application/json'}
        if cookie:
            headers['Cookie'] = cookie
        if origin:
            headers['Origin'] = origin
        connection.request(method or ('POST' if data is not None else 'GET'), path,
                           json.dumps(data) if data is not None else None, headers)
        response = connection.getresponse()
        result = response.status, dict(response.getheaders()), response.read()
        connection.close()
        return result

    def test_reviewer_page_login_is_separate_from_system_api(self):
        self.assertEqual(self.request('/')[1]['Location'], '/gallery/home.html')
        for page in ('home', 'login', 'index'):
            self.assertEqual(self.request('/gallery/'+page+'.html')[0], 200)
        for path in ('/gallery/generate.html', '/gallery/../gallery/generate.html', '/gallery/%67enerate.html'):
            for method in ('GET', 'HEAD'):
                status, headers, _ = self.request(path, method=method)
                self.assertEqual(status, 302)
                self.assertEqual(headers['Location'], '/gallery/login.html')
        self.assertEqual(self.request('/api/generation')[0], 200)
        self.server.generation.start.return_value = {'id':'job', 'mode':'generate', 'name':'Demo'}
        self.assertEqual(self.request('/api/generation', {'name':'Demo'})[0],202)
        self.assertEqual(self.server.generation.start.call_args.args[-1], 'system')
        self.server.generation.decide.return_value = {'id':'job','mode':'generate','name':'Demo'}
        self.assertEqual(self.request('/api/generation/accept', {'id':'job'})[0],202)
        self.assertEqual(self.server.generation.decide.call_args.args[-1], 'system')

    def test_all_accounts_login_and_logout_revokes_cookie(self):
        for user in ('jakes', 'hina', 'ray', 'phuong', 'an'):
            status, headers, _ = self.request('/api/auth/login', {'username': user, 'password': '1'})
            self.assertEqual(status, 200)
            self.assertIn('HttpOnly', headers['Set-Cookie'])
            self.assertIn('SameSite=Strict', headers['Set-Cookie'])
            cookie = headers['Set-Cookie'].split(';')[0]
            self.assertEqual(json.loads(self.request('/api/auth/session', cookie=cookie)[2])['user'], user)
            self.assertEqual(self.request('/gallery/generate.html', cookie=cookie)[0], 200)
            self.assertEqual(self.request('/api/generation', cookie=cookie)[0], 200)
            self.assertEqual(self.request('/api/auth/logout', {}, cookie)[0], 200)
            self.assertEqual(self.request('/api/generation', cookie=cookie)[0], 200)

    def test_invalid_credentials_expiry_and_cross_origin(self):
        for data in ({'username':'jakes','password':'wrong'}, {'username':'unknown','password':'1'}, {'username':[], 'password':1}):
            self.assertEqual(self.request('/api/auth/login', data)[0], 401)
        self.assertEqual(self.request('/api/auth/login', {'username':'jakes','password':'1'}, origin='https://elsewhere.test')[0], 403)
        _, headers, _ = self.request('/api/auth/login', {'username':'jakes','password':'1'})
        cookie = headers['Set-Cookie'].split(';')[0]
        token = cookie.split('=',1)[1]
        with sqlite3.connect(self.db) as db:
            self.assertEqual(db.execute('SELECT token FROM admin_sessions').fetchone()[0], hashlib.sha256(token.encode()).hexdigest())
            db.execute('UPDATE admin_sessions SET expires=0')
        self.assertEqual(self.request('/api/generation', cookie=cookie)[0], 200)
        self.assertEqual(self.request('/api/generation', cookie='pictographic_session=forged')[0], 200)
