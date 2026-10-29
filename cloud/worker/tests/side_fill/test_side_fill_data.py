"""The fill side pairs snapshot store (cloud/migrate/side_fill_data.py) against an in-memory R2: a push that fails part
way leaves the previous snapshot whole, and pulling restores it exactly.

    python3 -m pytest cloud/worker/tests/side_fill/test_side_fill_data.py -q      # no Worker, no R2 needed
"""
from __future__ import annotations

import hashlib
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO / 'cloud/migrate'))
import side_fill_data as store  # noqa: E402


class Memory:
    """R2 in memory; `fail_on` makes one key's put fail, as a dropped connection would."""
    def __init__(self):
        self.objects, self.fail_on = {}, None

    def existing(self, prefix):
        return {k: hashlib.md5(v).hexdigest() for k, v in self.objects.items() if k.startswith(prefix)}

    def put(self, key, content, content_type):
        if self.fail_on and self.fail_on in key:
            raise OSError('connection dropped')
        self.objects[key] = content

    def get(self, key):
        return self.objects[key]


@pytest.fixture
def snapshot(tmp_path, monkeypatch):
    monkeypatch.setattr(store, 'DATA', tmp_path / 'side-fill')
    (tmp_path / 'side-fill/data').mkdir(parents=True)
    return tmp_path / 'side-fill'


def write(folder, files):
    for name, text in files.items():
        (folder / name).parent.mkdir(parents=True, exist_ok=True)
        (folder / name).write_text(text)
    store.write_manifest()


def test_a_failed_push_leaves_the_previous_snapshot_restorable(snapshot, tmp_path, monkeypatch):
    r2 = Memory()
    write(snapshot, {'data/a.json': 'A1', 'data/b.json': 'B1'})
    assert store.push(r2, jobs=1) == 0
    # The next snapshot changes both files; sending b fails after a was sent.
    write(snapshot, {'data/a.json': 'A2', 'data/b.json': 'B2'})
    r2.fail_on = hashlib.sha256(b'B2').hexdigest()
    assert store.push(r2, jobs=1) == 1
    # A fresh checkout pulls the snapshot R2 names: the first one, whole.
    fresh = tmp_path / 'fresh'
    monkeypatch.setattr(store, 'DATA', fresh)
    assert store.pull(r2, jobs=1) == 0
    assert (fresh / 'data/a.json').read_text() == 'A1' and (fresh / 'data/b.json').read_text() == 'B1'
    assert store.check() == 0


def test_a_push_sends_each_content_once_and_never_overwrites_one(snapshot):
    r2 = Memory()
    write(snapshot, {'data/a.json': 'same', 'data/copy.json': 'same'})
    assert store.push(r2, jobs=1) == 0
    objects = {k for k in r2.objects if k.startswith(store.OBJECTS)}
    assert len(objects) == 1
    before = dict(r2.objects)
    write(snapshot, {'data/a.json': 'same', 'data/copy.json': 'same', 'data/new.json': 'new'})
    assert store.push(r2, jobs=1) == 0
    assert all(r2.objects[k] == v for k, v in before.items() if k.startswith(store.OBJECTS))
