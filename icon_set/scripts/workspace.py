"""Shared filesystem ownership and build locking for the icon workspace.

One build root: ``published/``. Every build, the local server, the publisher and
release export read and write it, and Git tracks it. Python originals, curated
metadata, supporting datasets and experiments are versioned beside it. The only
ignored things are runtime state (the review database, uploads, edits and jobs
under ``icon_set/state/``), regenerated QA evidence and lock files.
"""
from contextlib import contextmanager
import fcntl
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]


def build_dist(root=REPO_ROOT):
    """The tracked build output: family exports, gallery, failed builds, reports."""
    return Path(root) / 'published'


def preview_dir(root=REPO_ROOT):
    """Tracked PNG previews, inside the build output."""
    return build_dist(root) / 'previews-png'


def state_root(root=REPO_ROOT):
    """Ignored runtime state: review database, uploads, stroke edits, jobs, backups."""
    return Path(root) / 'icon_set' / 'state'


PUBLISHED_DIST = build_dist()
DEFAULT_DIST = PUBLISHED_DIST
DEFAULT_PNG = preview_dir()
STATE_ROOT = state_root()
DEFAULT_DATABASE = STATE_ROOT / 'feedback.sqlite3'


@contextmanager
def output_lock(dist):
    """Fail fast instead of allowing overlapping build/publication transactions.

    The lock sits beside the output so directory swaps cannot replace its inode.
    Never unlink it: another process may already hold an open descriptor.
    """
    dist = Path(dist).resolve()
    dist.parent.mkdir(parents=True, exist_ok=True)
    with (dist.parent / f'.{dist.name}.lock').open('a') as stream:
        try:
            fcntl.flock(stream, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError as error:
            raise ValueError(f'Build output is busy: {dist}. Wait for the active build or release export.') from error
        try:
            yield
        finally:
            fcntl.flock(stream, fcntl.LOCK_UN)


if __name__ == '__main__':
    import json
    print(json.dumps({'build_output': str(DEFAULT_DIST),
                      'previews': str(DEFAULT_PNG),
                      'runtime_state': str(STATE_ROOT),
                      'database': str(DEFAULT_DATABASE)}))
