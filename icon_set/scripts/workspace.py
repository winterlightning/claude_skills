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


def primitive_results_dir(root=REPO_ROOT):
    """Standalone Ray results, separate from published catalogs and runtime state."""
    return Path(root) / 'icon_set' / 'work' / 'primitive-make-ray'


PUBLISHED_DIST = build_dist()
DEFAULT_DIST = PUBLISHED_DIST
DEFAULT_PNG = preview_dir()
STATE_ROOT = state_root()
DEFAULT_DATABASE = STATE_ROOT / 'feedback.sqlite3'
LEGACY_COMBINATION_DATABASE = STATE_ROOT / 'combinations.sqlite3'
DEFAULT_COMBINATION_DATABASE = DEFAULT_DATABASE


# Never rewritten by compaction: regenerated QA evidence and the publication marker.
UNCOMPACTED = ('qa',)


def compact_json_tree(dist) -> int:
    """Rewrite every JSON catalog under the build root in compact form.

    Builds and the publisher both call this, so the tracked files never flip
    between pretty and compact form and a targeted build leaves no churn.
    """
    import json
    dist = Path(dist)
    rewritten = 0
    for path in dist.rglob('*.json'):
        relative = path.relative_to(dist)
        if relative.parts[0] in UNCOMPACTED or relative.name == 'release.json' or path.is_symlink() \
                or any(part.startswith('.') for part in relative.parts):
            continue
        text = path.read_text(encoding='utf-8')
        compact = json.dumps(json.loads(text), ensure_ascii=False, separators=(',', ':')) + '\n'
        if compact != text:
            path.write_text(compact, encoding='utf-8')
            rewritten += 1
    return rewritten


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
