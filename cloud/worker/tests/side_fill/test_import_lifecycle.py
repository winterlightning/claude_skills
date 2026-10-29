"""The fill side pairs import (icon_set/scripts/side_fill/d1_import.py) against the migrated schema in SQLite: what a
person changed on the site survives importing again, and an untouched pick keeps its output.

    python3 -m pytest cloud/worker/tests/side_fill/test_import_lifecycle.py -q      # no Worker needed
"""
from __future__ import annotations

import sqlite3
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO))
from icon_set.scripts.side_fill import d1_import as D  # noqa: E402

NOW = '2026-10-29T00:00:00+00:00'
EDITED = "UPDATE fill_pairs SET version = version + 1, edited_at = ?2, updated_at = ?2 WHERE reference_id = ?1"  # core side_fill::EDITED


def database():
    db = sqlite3.connect(':memory:')
    for path in sorted((REPO / 'cloud/worker/migrations').glob('*.sql')):
        db.executescript(path.read_text())
    for ref in ('p1', 'p2'):
        db.execute("INSERT INTO \"references\"(reference_id, kind, concept, source) VALUES (?, 'combination', ?, 't')", (ref, ref))
    for key in ('solo/a', 'solo/a--fill', 'solo/a--fill-region-1', 'sub/b', 'sub/b--fill'):
        db.execute("INSERT INTO icons(key, icon_id, family, svg_sha256, record, pushed_at) VALUES (?, ?, ?, 's', '{}', 'x')",
                   (key, key, key.split('/')[0]))
    return db


def run(db, statements):
    db.executescript('\n'.join(statements))


def pairs(db):
    return [D.pair_statement(ref, ref, 'picked', 'solo/a', 'sub/b', ['NULL', 'NULL'], None, NOW) for ref in ('p1', 'p2')]


def picks(layout='[{"x": 1}]'):
    """Both pairs: rank 1 the main's fill with the sub's fill, rank 2 the main's region fill with the sub's outline."""
    rows = []
    for ref in ('p1', 'p2'):
        rows += [D.pick_statement(ref, 'main', 1, 'solo/a--fill', layout, None, NOW, exists=True),
                 D.pick_statement(ref, 'sub', 1, 'sub/b--fill', layout, None, NOW, exists=True),
                 D.pick_statement(ref, 'main', 2, 'solo/a--fill-region-1', layout, None, NOW, exists=True),
                 D.pick_statement(ref, 'sub', 2, 'sub/b', layout, None, NOW)]
    keys = {f'{ref} {role} {rank}' for ref in ('p1', 'p2') for role in ('main', 'sub') for rank in (1, 2)}
    return [D.picks_head(keys)] + rows + D.COUNTS


def order(db, ref):
    return db.execute("SELECT rank, role, icon, combined, built_sha FROM reference_part_fills WHERE reference_id = ? ORDER BY rank, role",
                      (ref,)).fetchall()


def test_edits_on_the_site_survive_and_untouched_picks_keep_their_output():
    db = database()
    run(db, pairs(db) + picks())
    # Both pairs built: each pick has its output and its built drawings.
    db.execute("UPDATE reference_part_fills SET built_sha = 'built', combined = CASE WHEN role = 'main' THEN 'side_combination64/' || reference_id || "
               "'--fill' || CASE WHEN rank > 1 THEN '-' || rank ELSE '' END END")
    # On the site, p1's second pick is made the output (move), then its new second pick removed (unpick).
    db.execute("UPDATE reference_part_fills SET rank = CASE rank WHEN 1 THEN -2 ELSE -1 END WHERE reference_id = 'p1'")
    db.execute("UPDATE reference_part_fills SET rank = -rank WHERE reference_id = 'p1'")
    db.execute("DELETE FROM reference_part_fills WHERE reference_id = 'p1' AND rank = 2")
    db.execute(EDITED, ('p1', NOW))
    edited = order(db, 'p1')
    untouched = order(db, 'p2')
    run(db, pairs(db) + picks())                     # the same import again
    assert order(db, 'p1') == edited, 'an import must not undo what a person changed'
    assert order(db, 'p2') == untouched, 'an unchanged pick keeps its output and its built drawings'
    assert db.execute("SELECT n FROM fill_counts WHERE scope = 'pairs' AND status = 'picked'").fetchone() == (2,)


def test_a_changed_pick_keeps_its_output_and_needs_building_again():
    db = database()
    run(db, pairs(db) + picks())
    db.execute("UPDATE reference_part_fills SET built_sha = 'built', combined = CASE WHEN role = 'main' THEN 'out' END WHERE reference_id = 'p2' AND rank = 1")
    run(db, pairs(db) + picks(layout='[{"x": 2}]'))  # the build laid p2 out again
    main = db.execute("SELECT combined, built_sha, layout FROM reference_part_fills WHERE reference_id = 'p2' AND role = 'main' AND rank = 1").fetchone()
    assert main == ('out', None, '[{"x": 2}]')


def test_a_pick_the_build_no_longer_has_goes_unless_the_pair_was_edited():
    db = database()
    run(db, pairs(db) + picks())
    db.execute(EDITED, ('p1', NOW))
    statements = picks()
    keep = {f'{ref} {role} 1' for ref in ('p1', 'p2') for role in ('main', 'sub')}
    run(db, pairs(db) + [D.picks_head(keep)] + [s for s in statements[1:] if "', 2, '" not in s])
    assert [r[0] for r in order(db, 'p1')] == [1, 1, 2, 2]
    assert [r[0] for r in order(db, 'p2')] == [1, 1]


def test_a_part_filled_on_the_site_stays_filled_and_its_pair_pickable():
    db = database()
    run(db, [D.pair_statement('p1', 'p1', 'uncombined', 'solo/a', 'sub/b', ['NULL', 'NULL'], D.NO_FILL_NOTE, NOW),
             D.part_statement('solo/a', 'main', 'a', 'outline', 'only an outline', None, 1, NOW)] + D.COUNTS)
    # A fill was added on the site (core side_fill::FIRST_FILL): the part is filled, the pair can be picked.
    db.execute("UPDATE fill_parts SET status = 'ready', note = ? WHERE key = 'solo/a'", (D.READY_NOTE,))
    db.execute("UPDATE fill_pairs SET state = 'unpicked', note = NULL WHERE reference_id = 'p1'")
    run(db, [D.pair_statement('p1', 'p1', 'uncombined', 'solo/a', 'sub/b', ['NULL', 'NULL'], D.NO_FILL_NOTE, NOW),
             D.part_statement('solo/a', 'main', 'a', 'outline', 'only an outline', None, 1, NOW)] + D.COUNTS)
    assert db.execute("SELECT status FROM fill_parts WHERE key = 'solo/a'").fetchone() == ('ready',)
    assert db.execute("SELECT state, note FROM fill_pairs WHERE reference_id = 'p1'").fetchone() == ('unpicked', None)
