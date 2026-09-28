"""Uploaded reference images (SVG or PNG) for feedback and generation briefs.

Files are stored by content hash outside the served dist folder and referred to
by that hash, so feedback rows and generation jobs only ever carry ids. With a
database, each image's metadata is a reference_images row; the bytes stay in the folder.
"""
from contextlib import closing
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import re
import xml.etree.ElementTree as ElementTree

MAX_IMAGES = 4
LIMITS = {'png': 2 * 1024 * 1024, 'svg': 1024 * 1024}
MIME = {'png': 'image/png', 'svg': 'image/svg+xml'}
PNG_SIGNATURE = b'\x89PNG\r\n\x1a\n'
_ID = re.compile('[a-f0-9]{64}')


def _kind(data):
    if data.startswith(PNG_SIGNATURE):
        return 'png'
    try:
        text = data.decode('utf-8')
    except UnicodeDecodeError:
        raise ValueError('Reference images must be SVG or PNG files.')
    # No DTDs: entity expansion is the XML parser's classic abuse.
    if re.search(r'<!(DOCTYPE|ENTITY)', text, re.I):
        raise ValueError('SVG references may not declare a DOCTYPE or entities.')
    try:
        root = ElementTree.fromstring(text)
    except ElementTree.ParseError:
        raise ValueError('Reference images must be SVG or PNG files.')
    if root.tag not in ('svg', '{http://www.w3.org/2000/svg}svg'):
        raise ValueError('Reference images must be SVG or PNG files.')
    return 'svg'


def _name(name, kind):
    stem = Path(name if isinstance(name, str) else '').stem.lower()
    stem = re.sub(r'[^a-z0-9._-]+', '-', stem).strip('.-_')[:72] or 'reference'
    return f'{stem}.{kind}'


class ReferenceStore:
    def __init__(self, folder, database=None):
        self.folder = Path(folder)
        self.database = Path(database) if database else None
        if self.database:
            from icon_set.scripts import state_db
            self._db = state_db
            with closing(state_db.connect(self.database)) as connection, connection:
                state_db.init_store_tables(connection)

    def save(self, name, data):
        if not isinstance(data, bytes) or not data:
            raise ValueError('Choose an SVG or PNG file.')
        kind = _kind(data)
        if len(data) > LIMITS[kind]:
            raise ValueError(f'{kind.upper()} references must be at most {LIMITS[kind] // (1024 * 1024)} MB.')
        image_id = hashlib.sha256(data).hexdigest()
        meta = {'id': image_id, 'kind': kind, 'name': _name(name, kind)}
        self.folder.mkdir(parents=True, exist_ok=True)
        image = self.folder / f'{image_id}.{kind}'
        if not image.exists():
            temporary = image.with_suffix('.tmp')
            temporary.write_bytes(data)
            temporary.replace(image)
        if self.database:
            with closing(self._db.connect(self.database)) as connection, connection:
                connection.execute('INSERT INTO reference_images VALUES (?,?,?,?,?) ON CONFLICT(id) DO UPDATE SET name=excluded.name',
                                   (image_id, kind, meta['name'], len(data), datetime.now(timezone.utc).isoformat()))
        else:
            (self.folder / f'{image_id}.json').write_text(json.dumps(meta))
        return meta

    def _stored_meta(self, image_id):
        if self.database:
            with closing(self._db.connect(self.database)) as connection:
                row = connection.execute('SELECT kind, name FROM reference_images WHERE id=?', (image_id,)).fetchone()
            if row:
                return {'id': image_id, 'kind': row[0], 'name': row[1]}
        # Images saved before the database held their metadata keep a JSON sidecar.
        return json.loads((self.folder / f'{image_id}.json').read_text())

    def meta(self, image_id):
        if not isinstance(image_id, str) or not _ID.fullmatch(image_id):
            raise ValueError('Unknown reference image.')
        try:
            meta = self._stored_meta(image_id)
        except (OSError, ValueError):
            raise ValueError('Unknown reference image.')
        if not (self.folder / f"{image_id}.{meta.get('kind')}").is_file():
            raise ValueError('Unknown reference image.')
        return meta

    def resolve(self, ids):
        """Validated metadata for a request's reference ids, in order and without repeats."""
        if ids is None:
            return []
        if not isinstance(ids, list) or len(ids) > MAX_IMAGES or not all(isinstance(i, str) for i in ids):
            raise ValueError(f'Attach up to {MAX_IMAGES} reference images.')
        return [self.meta(image_id) for image_id in dict.fromkeys(ids)]

    def path(self, image_id):
        meta = self.meta(image_id)
        return self.folder / f"{image_id}.{meta['kind']}"

    def read(self, image_id):
        meta = self.meta(image_id)
        return self.path(image_id).read_bytes(), MIME[meta['kind']]
