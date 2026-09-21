"""Shared filesystem ownership and build locking for the icon workspace.

Python sources and curated metadata are versioned. Build output is disposable.
Production receives release snapshots and owns a separate persistent state tree.
"""
from contextlib import contextmanager
import fcntl
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]


def development_dist(root=REPO_ROOT):
    return Path(root) / 'icon_set' / '.local' / 'dist'


def development_previews(root=REPO_ROOT):
    return Path(root) / 'icon_set' / '.local' / 'previews-png'


DEFAULT_DIST = development_dist()
DEFAULT_PNG = development_previews()
DEFAULT_DATABASE = REPO_ROOT / 'icon_set' / '.local' / 'state' / 'feedback.sqlite3'
PUBLISHED_DIST = REPO_ROOT / 'published'
PUBLICATION_BUILD = REPO_ROOT / 'icon_set' / '.local' / 'publish-dist'


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
    print(json.dumps({'development_assets': str(DEFAULT_DIST),
                      'development_previews': str(DEFAULT_PNG),
                      'development_database': str(DEFAULT_DATABASE)}))
