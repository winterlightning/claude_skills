"""The local gallery's link to the Cloudflare Worker (``deploy.py --cloud-api URL``).

The cloud stores every piece of shared data and status; this machine does the graphics
processing. These classes keep the existing store logic (validation, geometry, rendering) and
only change where documents are read from and saved to:

* ``CloudClient``           HTTP calls to the Worker, with the push token for internal routes.
* ``CloudStrokeEditStore``  stroke edits saved in the cloud, keyed ``<icon>@<svg_sha256>``.
* ``CloudArtworkStore``     artwork choices saved in the cloud, cached briefly (read per record).
* ``CloudReferenceStore``   reference images downloaded on demand into a local cache folder.

Saves send the revision they started from; the cloud refuses a save when another machine saved
first, which surfaces here as the usual ``EditConflict``.
"""
from __future__ import annotations

from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import threading
import time
import urllib.error
import urllib.parse
import urllib.request

if __package__:
    from .icon_artwork import ArtworkStore
    from .reference_images import ReferenceStore
    from .stroke_edits import StrokeEditStore, EditConflict
else:
    from icon_artwork import ArtworkStore
    from reference_images import ReferenceStore
    from stroke_edits import StrokeEditStore, EditConflict

REPO = Path(__file__).resolve().parents[2]
ENV_FILE = REPO / 'cloud' / '.env'


class CloudError(OSError):
    def __init__(self, status: int, message: str, payload=None):
        super().__init__(message)
        self.status, self.payload = status, payload


def _settings() -> dict:
    values = {}
    if ENV_FILE.is_file():
        for line in ENV_FILE.read_text().splitlines():
            if '=' in line and not line.lstrip().startswith('#'):
                key, value = line.split('=', 1)
                values[key.strip()] = value.strip()
    values.update({k: v for k, v in os.environ.items() if k.startswith('PICTOGRAPHIC_')})
    return values


class CloudClient:
    def __init__(self, base_url: str, token: str | None = None, timeout: float = 60):
        self.base_url = base_url.rstrip('/')
        local = self.base_url.startswith(('http://127.0.0.1', 'http://localhost'))
        config = _settings()
        self.token = token or config.get('PICTOGRAPHIC_PUSH_TOKEN_LOCAL' if local else 'PICTOGRAPHIC_PUSH_TOKEN')
        self.timeout = timeout

    def request(self, method: str, path: str, body=None, *, cookie: str | None = None, raw: bytes | None = None,
                content_type: str = 'application/json', internal: bool = False) -> tuple[int, bytes, dict]:
        # Cloudflare's bot filter refuses Python's default User-Agent (error 1010).
        headers = {'Accept': 'application/json', 'User-Agent': 'pictographic-gallery/1.0'}
        data = raw if raw is not None else (json.dumps(body, ensure_ascii=False).encode('utf-8') if body is not None else None)
        if data is not None:
            headers['Content-Type'] = content_type
        if cookie:
            headers['Cookie'] = cookie
        if internal:
            if not self.token:
                raise CloudError(503, 'No push token for the cloud; set PICTOGRAPHIC_PUSH_TOKEN in cloud/.env.')
            headers['Authorization'] = 'Bearer ' + self.token
        request = urllib.request.Request(self.base_url + path, data=data, method=method, headers=headers)
        try:
            with urllib.request.urlopen(request, timeout=self.timeout) as response:
                return response.status, response.read(), dict(response.headers)
        except urllib.error.HTTPError as error:
            return error.code, error.read(), dict(error.headers)
        except (urllib.error.URLError, TimeoutError) as error:
            raise CloudError(502, f'The cloud is unreachable at {self.base_url}: {getattr(error, "reason", error)}') from error

    def json(self, method: str, path: str, body=None, **kwargs):
        status, content, _ = self.request(method, path, body, **kwargs)
        try:
            payload = json.loads(content or b'null')
        except ValueError:
            payload = {'error': content[:200].decode('utf-8', 'replace')}
        if status >= 400:
            message = payload.get('error') if isinstance(payload, dict) else str(payload)
            raise CloudError(status, message or f'HTTP {status}', payload)
        return payload

    def get(self, path: str, **kwargs):
        return self.json('GET', path, **kwargs)

    def post(self, path: str, body, **kwargs):
        return self.json('POST', path, body, **kwargs)

    # ---- helpers for the local-only routes ----

    def record(self, user: str, action: str, icon: str | None = None, **details) -> None:
        """record_activity, stored in the cloud's activity log."""
        self.post('/api/activity', {'user': user, 'action': action, 'icon': icon, 'details': details}, internal=True)

    def session_user(self, cookie: str | None) -> str | None:
        if not cookie:
            return None
        return self.get('/api/auth/session', cookie=cookie).get('user')

    def push_icons(self, rows: list[dict]) -> dict:
        """Update individual catalog rows (e.g. after an artwork choice changes an icon's drawing)."""
        stamp = datetime.now(timezone.utc).strftime('local-%Y%m%dT%H%M%S%fZ')
        return self.post('/api/catalog/push', {'push_id': stamp, 'icons': rows, 'final': False}, internal=True)


def catalog_row(record: dict, svg: str | None, origin: str = 'build') -> dict:
    """One /api/catalog/push row from a gallery record and its current drawing."""
    fields = ('key', 'icon_id', 'name', 'family', 'category', 'profile', 'canvas_size', 'svg_sha256', 'python_source',
              'preview_url', 'variant_of', 'variant_root', 'variant_label')
    row = {field: record.get(field) for field in fields}
    row.update(original_sources=record.get('original_sources') or [], build_failed=bool(record.get('build_failed')),
               svg=svg if svg is not None and hashlib.sha256(svg.encode('utf-8')).hexdigest() == record.get('svg_sha256') else None,
               origin=origin)
    return row


def catalog_json(catalog: dict) -> bytes:
    """The gallery catalog as the cloud stores it: uploads left out (they live in D1), ``icons`` last,
    compact, so the file ends with ``]}`` and the Worker can append uploads while streaming it."""
    icons = [{k: v for k, v in r.items() if k != 'uploaded_svg'} for r in catalog.get('icons', []) if not r.get('uploaded_icon')]
    dump = lambda value: json.dumps(value, ensure_ascii=False, separators=(',', ':'))  # noqa: E731
    parts = [f'{dump(k)}:{dump(v)}' for k, v in catalog.items() if k != 'icons']
    return ('{' + ''.join(p + ',' for p in parts) + '"icons":[' + ','.join(dump(r) for r in icons) + ']}').encode('utf-8')


def _save_document(client: CloudClient, store: str, key: str, document: dict, previous_revision: int, user: str) -> None:
    try:
        client.post(f'/api/store/{store}', {'key': key, 'document': document, 'expected_revision': previous_revision,
                                            'user': user}, internal=True)
    except CloudError as error:
        if error.status == 409:
            raise EditConflict('Someone saved newer edits on another machine. Reload before saving again.') from error
        raise


class CloudStrokeEditStore(StrokeEditStore):
    """Stroke edits in the cloud; the local folder only holds files while a save is in progress."""

    def __init__(self, client: CloudClient, root, contracts_path=None):
        super().__init__(root, contracts_path)
        self.client = client

    @staticmethod
    def cloud_key(key: str, sha: str) -> str:
        return f'{key}@{sha}'

    def get(self, key, sha):
        documents = self.client.get('/api/store/stroke-edits?key=' + urllib.parse.quote(self.cloud_key(key, sha), safe=''),
                                    internal=True)['documents']
        entry = documents.get(self.cloud_key(key, sha))
        return entry['document'] if entry else None

    def previous_versions(self, key, sha):
        documents = self.client.get('/api/store/stroke-edits?prefix=' + urllib.parse.quote(key + '@', safe=''),
                                    internal=True)['documents']
        return [{'source_svg_sha256': entry['document']['source_svg_sha256'], 'updated_at': entry['document']['updated_at']}
                for entry in documents.values() if entry['document'].get('source_svg_sha256') != sha]

    def save(self, icon, data, user):
        previous = data.get('revision')
        document = super().save(icon, data, user)  # validates against the cloud's current revision, writes a local file
        _save_document(self.client, 'stroke-edits', self.cloud_key(icon['key'], icon['svg_sha256']), document,
                       previous if isinstance(previous, int) else 0, user)
        return document


class CloudArtworkStore(ArtworkStore):
    """Artwork choices in the cloud. Every catalog record looks its choice up, so all choices are
    fetched together and reused for a few seconds."""

    TTL = 5.0

    def __init__(self, client: CloudClient, root):
        super().__init__(root)
        self.client = client
        self._cache: tuple[float, dict] | None = None
        self._lock = threading.Lock()

    def _documents(self) -> dict:
        with self._lock:
            if self._cache is None or self._cache[0] < time.monotonic():
                documents = self.client.get('/api/store/icon-artwork', internal=True)['documents']
                self._cache = (time.monotonic() + self.TTL, {key: entry['document'] for key, entry in documents.items()})
            return self._cache[1]

    def get(self, key):
        document = self._documents().get(key)
        if document is not None and (document.get('schema') != 'pictographic.icon-artwork.v1' or document.get('icon') != key):
            raise ValueError('Invalid saved artwork record.')
        return document

    def save(self, icon, data, user, edits):
        with self._lock:
            self._cache = None  # decide against the cloud's current choice, not a cached one
        previous = (self.get(icon['key']) or {}).get('revision', 0)
        result = super().save(icon, data, user, edits)
        _save_document(self.client, 'icon-artwork', icon['key'], result, previous, user)
        with self._lock:
            self._cache = None
        return result


class CloudReferenceStore(ReferenceStore):
    """Reference images live in the cloud; ids are content hashes, so a local copy never goes stale."""

    def __init__(self, client: CloudClient, folder):
        super().__init__(folder)
        self.client = client

    def meta(self, image_id):
        try:
            return super().meta(image_id)
        except ValueError:
            pass
        if not isinstance(image_id, str) or len(image_id) != 64:
            raise ValueError('Unknown reference image.')
        status, content, headers = self.client.request('GET', '/api/reference-images?id=' + image_id)
        if status != 200:
            raise ValueError('Unknown reference image.')
        kind = 'png' if headers.get('Content-Type', '').startswith('image/png') else 'svg'
        self.folder.mkdir(parents=True, exist_ok=True)
        (self.folder / f'{image_id}.{kind}').write_bytes(content)
        (self.folder / f'{image_id}.json').write_text(json.dumps({'id': image_id, 'kind': kind, 'name': f'reference.{kind}'}))
        return super().meta(image_id)
