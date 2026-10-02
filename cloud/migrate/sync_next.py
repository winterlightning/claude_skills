#!/usr/bin/env python3
"""Refresh the test copy (pictographic-review-next) from production's D1, read-only on production.

    # 1. production, table by table (one `wrangler d1 export` stops at 260 MiB); admin_sessions is never copied
    cd cloud/worker
    npx wrangler d1 export pictographic-review --remote --no-data --output /tmp/sync-next/prod/schema.sql
    npx wrangler d1 export pictographic-review --remote --no-schema --table <t> --output /tmp/sync-next/prod/data-<t>.sql

    # 2. a local copy with the migrations production lacks, and the files that load it
    python3 cloud/migrate/sync_next.py build --export /tmp/sync-next/prod --out /tmp/sync-next/build

    # 3. empty pictographic-review-next and load it (asks first)
    python3 cloud/migrate/sync_next.py load --build /tmp/sync-next/build

`build` loads the export into a fresh SQLite file (tables, then rows, then indexes and triggers, so no trigger runs
on copied rows), checks every table holds as many rows as its export file inserts, applies the migrations in
cloud/worker/migrations that production has not recorded (0013_side_pairs_72, 0015_icon_list, …), and writes:

* wipe.sql   drops every object next has now (asked of next when it is written, so nothing is left behind)
* load.sql   tables, rows, the icon_search full-text table refilled from icons, then indexes, views, triggers
* large.json rows over D1's 100 KB statement limit, inserted by `load` through the D1 API with bound parameters

`load` runs wipe.sql and load.sql with `wrangler d1 execute pictographic-review-next --remote --file`, then the large
rows, and prints each table's count on next beside the local copy's. Restore point: `wrangler d1 time-travel info`
before loading (the command is printed).
"""
from __future__ import annotations

import argparse
import json
import re
import sqlite3
import subprocess
import sys
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import cloudapi  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
WORKER = ROOT / 'cloud' / 'worker'
MIGRATIONS = WORKER / 'migrations'
NEXT = 'pictographic-review-next'
NEXT_CONFIG = 'wrangler.next.toml'
# D1 refuses statements over 100 KB; rows near that go through the API with bound parameters.
STATEMENT_LIMIT = 90_000
# Production's login sessions stay in production.
SKIPPED_TABLES = {'admin_sessions'}
SEARCH = 'icon_search'


def statements(text: str) -> list[str]:
    """SQL text split into complete statements."""
    out, current = [], ''
    for line in text.splitlines(keepends=True):
        current += line
        if sqlite3.complete_statement(current):
            out.append(current.strip())
            current = ''
    if current.strip():
        raise SystemExit(f'error: an incomplete statement at the end: {current[:120]!r}')
    return out


def is_table(statement: str) -> bool:
    return bool(re.match(r'CREATE TABLE', statement, re.I))


def build(args) -> None:
    export, out = Path(args.export), Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    db_path = out / 'next.sqlite'
    db_path.unlink(missing_ok=True)
    con = sqlite3.connect(db_path)
    schema = [s for s in statements((export / 'schema.sql').read_text()) if not s.upper().startswith(('PRAGMA', 'DELETE FROM SQLITE_SEQUENCE'))]
    for statement in schema:
        if is_table(statement):
            con.execute(statement)
    tables = [r[0] for r in con.execute("SELECT name FROM sqlite_master WHERE type = 'table' AND name NOT LIKE 'sqlite_%'")]
    print(f'{len(tables)} tables in the export schema')
    problems = []
    for table in tables:
        if table in SKIPPED_TABLES:
            continue
        path = export / f'data-{table}.sql'
        if not path.is_file():
            problems.append(f'{table}: no export file')
            continue
        rows = [s for s in statements(path.read_text()) if s.upper().startswith('INSERT')]
        con.executescript('BEGIN;\n' + ';\n'.join(rows) + (';\n' if rows else '') + 'COMMIT;')
        stored = con.execute(f'SELECT COUNT(*) FROM "{table}"').fetchone()[0]
        if stored != len(rows):
            problems.append(f'{table}: {len(rows)} rows exported, {stored} stored')
    for statement in schema:
        if not is_table(statement):
            con.execute(statement)
    if problems:
        raise SystemExit('error: ' + '; '.join(problems))
    con.commit()

    # The migrations production has not recorded, in file order, recorded as wrangler records them.
    applied = {r[0] for r in con.execute('SELECT name FROM d1_migrations')}
    for path in sorted(MIGRATIONS.glob('*.sql')):
        if path.name in applied:
            continue
        print(f'applying {path.name}')
        con.executescript(path.read_text())
        con.execute('INSERT INTO d1_migrations(name) VALUES (?)', (path.name,))
    con.commit()
    write_load(con, out)
    write_wipe(out)
    counts = {t: con.execute(f'SELECT COUNT(*) FROM "{t}"').fetchone()[0] for t in user_tables(con)}
    (out / 'counts.json').write_text(json.dumps(counts, indent=1) + '\n')
    print(f'built {db_path} ({db_path.stat().st_size / 1e6:.0f} MB): {sum(counts.values()):,} rows in {len(counts)} tables')


def user_tables(con) -> list[str]:
    """Tables that load.sql fills: not SQLite's, not the full-text index's own (refilled from icons)."""
    return [r[0] for r in con.execute("SELECT name FROM sqlite_master WHERE type = 'table' AND name NOT LIKE 'sqlite_%' "
                                      "AND name NOT LIKE ? AND sql NOT LIKE 'CREATE VIRTUAL%' ORDER BY rowid", (SEARCH + '%',))]


def write_load(con, out: Path) -> None:
    """load.sql: tables, rows (large ones to large.json), the full-text table, then indexes, views and triggers."""
    tables = user_tables(con)
    large = []
    with open(out / 'load.sql', 'w') as f:
        f.write('PRAGMA defer_foreign_keys = TRUE;\n')
        for (sql,) in con.execute("SELECT sql FROM sqlite_master WHERE type = 'table' AND name IN (SELECT value FROM json_each(?)) "
                                  "ORDER BY rowid", (json.dumps(tables),)):
            f.write(sql.replace('CREATE TABLE "d1_migrations"', 'CREATE TABLE IF NOT EXISTS "d1_migrations"') + ';\n')
        for table in tables:
            columns = [r[1] for r in con.execute(f'PRAGMA table_info("{table}")')]
            names = ','.join(f'"{c}"' for c in columns)
            quoted = " || ',' || ".join(f'quote("{c}")' for c in columns)
            for rowid, values in con.execute(f'SELECT rowid, {quoted} FROM "{table}" ORDER BY rowid'):
                statement = f'INSERT INTO "{table}" ({names}) VALUES({values});\n'
                if len(statement.encode()) > STATEMENT_LIMIT:
                    row = con.execute(f'SELECT {",".join(chr(34) + c + chr(34) for c in columns)} FROM "{table}" WHERE rowid = ?', (rowid,)).fetchone()
                    large.append({'table': table, 'columns': columns, 'values': list(row)})
                else:
                    f.write(statement)
        # icon_search (migration 0015): created and filled from icons, so its shadow tables are D1's own.
        search = con.execute("SELECT sql FROM sqlite_master WHERE name = ?", (SEARCH,)).fetchone()
        if search:
            f.write(search[0] + ';\n')
            f.write(f'INSERT INTO {SEARCH}(search, key) SELECT search, key FROM icons;\n')
        for (sql,) in con.execute("SELECT sql FROM sqlite_master WHERE type IN ('index', 'view', 'trigger') AND sql IS NOT NULL "
                                  "AND tbl_name NOT LIKE ? ORDER BY CASE type WHEN 'index' THEN 0 WHEN 'view' THEN 1 ELSE 2 END, rowid",
                                  (SEARCH + '_%',)):
            f.write(sql + ';\n')
    (out / 'large.json').write_text(json.dumps(large))
    print(f'load.sql {(out / "load.sql").stat().st_size / 1e6:.0f} MB; {len(large)} rows over the statement limit in large.json')


def wrangler(*command: str, capture: bool = True) -> str:
    env = {**__import__('os').environ, **{k: v for k, v in cloudapi.settings().items() if k == 'CLOUDFLARE_API_TOKEN'}}
    result = subprocess.run(['npx', 'wrangler', *command], cwd=WORKER, env=env, capture_output=capture, text=True)
    if result.returncode:
        raise SystemExit(f'error: wrangler {" ".join(command[:3])} failed:\n{(result.stderr or result.stdout)[-2000:]}')
    return result.stdout


def query_next(sql: str) -> list[dict]:
    out = wrangler('d1', 'execute', NEXT, '--remote', '-c', NEXT_CONFIG, '--json', '--command', sql)
    return json.loads(out)[0]['results']


def write_wipe(out: Path) -> None:
    """wipe.sql: next's triggers, views, the full-text table, then every other table (children before parents)."""
    objects = query_next("SELECT type, name, sql FROM sqlite_master WHERE name NOT LIKE 'sqlite_%' AND name NOT LIKE '_cf_%' "
                         "AND name != 'd1_migrations' ORDER BY rowid DESC")
    lines = ['PRAGMA defer_foreign_keys = TRUE;']
    for kind in ('trigger', 'view'):
        lines += [f'DROP {kind.upper()} IF EXISTS "{o["name"]}";' for o in objects if o['type'] == kind]
    lines.append(f'DROP TABLE IF EXISTS "{SEARCH}";')
    shadow = re.compile(rf'^{SEARCH}_(data|idx|content|docsize|config)$')
    lines += [f'DROP TABLE IF EXISTS "{o["name"]}";' for o in objects
              if o['type'] == 'table' and o['name'] != SEARCH and not shadow.match(o['name'])]
    lines.append('DELETE FROM d1_migrations;')
    (out / 'wipe.sql').write_text('\n'.join(lines) + '\n')
    print(f'wipe.sql: {len(lines) - 2} drops for next')


def d1_api(sql: str, params: list) -> None:
    config = cloudapi.settings()
    toml = (WORKER / NEXT_CONFIG).read_text()
    account = re.search(r'account_id = "([^"]+)"', toml).group(1)
    database = re.search(r'database_id = "([^"]+)"', toml).group(1)
    req = urllib.request.Request(f'https://api.cloudflare.com/client/v4/accounts/{account}/d1/database/{database}/query',
                                 data=json.dumps({'sql': sql, 'params': params}).encode(), method='POST',
                                 headers={'Authorization': 'Bearer ' + config['CLOUDFLARE_API_TOKEN'], 'Content-Type': 'application/json'})
    with urllib.request.urlopen(req, timeout=120) as response:
        answer = json.loads(response.read())
    if not answer.get('success'):
        raise SystemExit(f'error: D1 API: {answer.get("errors")}')


def load(args) -> None:
    out = Path(args.build)
    print(wrangler('d1', 'time-travel', 'info', NEXT, '-c', NEXT_CONFIG).strip().splitlines()[-1])
    if not args.yes and input(f'Empty {NEXT} and load {out / "load.sql"}? [y/N] ').strip().lower() != 'y':
        raise SystemExit('stopped')
    for name in ('wipe.sql', 'load.sql'):
        print(f'running {name} on {NEXT}…')
        wrangler('d1', 'execute', NEXT, '--remote', '-c', NEXT_CONFIG, '--yes', '--file', str(out / name), capture=False)
    large = json.loads((out / 'large.json').read_text())
    for row in large:
        names = ','.join(f'"{c}"' for c in row['columns'])
        d1_api(f'INSERT INTO "{row["table"]}" ({names}) VALUES ({",".join("?" * len(row["columns"]))})', row['values'])
    print(f'{len(large)} large rows inserted')
    verify(out)


def verify(out: Path) -> None:
    counts = json.loads((out / 'counts.json').read_text())
    select = ', '.join(f'(SELECT COUNT(*) FROM "{t}") AS "{t}"' for t in counts)
    remote = query_next(f'SELECT {select}')[0]
    bad = {t: (n, remote.get(t)) for t, n in counts.items() if remote.get(t) != n}
    for table, n in counts.items():
        print(f'{table:28}{n:>10}{remote.get(table)!s:>10}' + ('  *' if table in bad else ''))
    print('next matches the local copy' if not bad else f'error: {len(bad)} tables differ')
    if bad:
        raise SystemExit(1)


def main(argv=None) -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest='command', required=True)
    b = sub.add_parser('build')
    b.add_argument('--export', required=True)
    b.add_argument('--out', required=True)
    l = sub.add_parser('load')
    l.add_argument('--build', required=True)
    l.add_argument('--yes', action='store_true', help='do not ask before emptying next')
    v = sub.add_parser('verify')
    v.add_argument('--build', required=True)
    args = parser.parse_args(argv)
    {'build': build, 'load': load, 'verify': lambda a: verify(Path(a.build))}[args.command](args)


if __name__ == '__main__':
    main()
