"""Persistent, idempotent two-component briefs for rejected combined references."""
import json
from datetime import datetime, timezone


def init_brief_queue(connection):
    connection.execute('''CREATE TABLE IF NOT EXISTS split_requests (
        id INTEGER PRIMARY KEY, icon TEXT NOT NULL, svg_sha256 TEXT NOT NULL,
        combination_type TEXT NOT NULL, reason TEXT NOT NULL, reference_path TEXT NOT NULL,
        active INTEGER NOT NULL DEFAULT 1, created_at TEXT NOT NULL,
        UNIQUE(icon, svg_sha256))''')
    connection.execute('''CREATE TABLE IF NOT EXISTS pending_briefs (
        id INTEGER PRIMARY KEY, split_id INTEGER NOT NULL REFERENCES split_requests(id),
        position INTEGER NOT NULL, name TEXT NOT NULL, family TEXT NOT NULL,
        description TEXT NOT NULL, status TEXT NOT NULL DEFAULT 'pending',
        generated_icon TEXT, UNIQUE(split_id, position))''')


def validate_split(data):
    kind = data.get('combination_type')
    if kind not in ('container', 'side'):
        raise ValueError('Choose container combination or side combination.')
    parts = data.get('components')
    if not isinstance(parts, list) or len(parts) != 2:
        raise ValueError('Describe exactly two component icons.')
    for part in parts:
        if not isinstance(part, dict):
            raise ValueError('Invalid component brief.')
        for key, limit in [('name', 160), ('description', 10000)]:
            if not isinstance(part.get(key), str) or not 0 < len(part[key].strip()) <= limit:
                raise ValueError(f'Each component needs a {key} (maximum {limit} characters).')
        if part.get('family') not in ('solo', 'sub', 'container'):
            raise ValueError('Each component needs a valid family.')
    if parts[0]['name'].strip().lower() == parts[1]['name'].strip().lower():
        raise ValueError('Give the two components distinct names.')
    expected_first = ('container',) if kind == 'container' else ('solo', 'container')
    if parts[0]['family'] not in expected_first or parts[1]['family'] != 'sub':
        raise ValueError('Use container + sub for a container combination; solo/container + sub for a side combination.')
    reason = data.get('reason', '')
    if not isinstance(reason, str) or len(reason) > 10000:
        raise ValueError('Invalid rejection reason.')
    return kind, parts, reason.strip()


def enqueue_split(connection, icon, sha, reference_path, data):
    kind, parts, reason = validate_split(data)
    existing = connection.execute('SELECT id, active FROM split_requests WHERE icon=? AND svg_sha256=?', (icon, sha)).fetchone()
    if existing and existing[1]:
        return existing[0]  # Repeated clicks/retries cannot duplicate or reset work.
    now = datetime.now(timezone.utc).isoformat()
    if existing:
        split_id = existing[0]
        connection.execute('UPDATE split_requests SET active=1, combination_type=?, reason=?, reference_path=?, created_at=? WHERE id=?', (kind, reason, reference_path, now, split_id))
        connection.execute('DELETE FROM pending_briefs WHERE split_id=?', (split_id,))
    else:
        split_id = connection.execute('INSERT INTO split_requests(icon,svg_sha256,combination_type,reason,reference_path,created_at) VALUES (?,?,?,?,?,?)', (icon, sha, kind, reason, reference_path, now)).lastrowid
    for index, part in enumerate(parts, 1):
        connection.execute('INSERT INTO pending_briefs(split_id,position,name,family,description) VALUES (?,?,?,?,?)', (split_id,index,part['name'].strip(),part['family'],part['description'].strip()))
    return split_id


def list_briefs(connection):
    cursor = connection.execute('''SELECT b.id,b.split_id,b.position,b.name,b.family,b.description,
        b.status,b.generated_icon,s.icon,s.svg_sha256,s.combination_type,s.reason,s.reference_path,s.created_at
        FROM pending_briefs b JOIN split_requests s ON s.id=b.split_id WHERE s.active=1
        ORDER BY s.id DESC,b.position''')
    return [dict(zip([d[0] for d in cursor.description], row)) for row in cursor.fetchall()]


def brief_archive(rows, catalog, dist, source_root):
    """Export active component briefs and available references without changing reviews."""
    from io import BytesIO
    from pathlib import Path
    import hashlib
    import re
    from zipfile import ZipFile, ZIP_DEFLATED

    output = BytesIO()
    with ZipFile(output, 'w', ZIP_DEFLATED) as archive:
        archive.writestr('pending-briefs/README.txt',
            'All active component briefs, including generated components, regardless of page filters.\n'
            'Each family folder contains a brief.md for an AI agent, brief.json metadata, '
            'and the reference image when available. Missing references are recorded in each brief.\n')
        for row in rows:
            family = row['family']
            if family not in ('solo', 'sub', 'container'):
                raise ValueError('Unknown brief family')
            slug = re.sub(r'[^a-zA-Z0-9_-]+', '-', row['name']).strip('-')[:80] or 'icon'
            folder = f"pending-briefs/{family}/{int(row['id'])}-{slug}/"
            reference = None
            # Use the published copy first, so dist-only deployments work too.
            candidates = []
            for source in catalog.get(row['icon'], {}).get('original_sources', []):
                if source.get('source_path') == row['reference_path']:
                    candidates.append((dist / 'gallery' / source['url'], dist))
            if row['reference_path']:
                candidates.append((source_root / row['reference_path'], source_root))
            for candidate, boundary in candidates:
                candidate = candidate.resolve()
                if not candidate.is_relative_to(boundary.resolve()) or candidate.suffix.lower() not in ('.svg', '.png'):
                    continue
                try:
                    content = candidate.read_bytes()
                except OSError:
                    continue
                if row['icon'].startswith('reference:') and hashlib.sha256(content).hexdigest() != row['svg_sha256']:
                    continue  # A changed source must not masquerade as the queued revision.
                reference = 'reference' + candidate.suffix.lower()
                archive.writestr(folder + reference, content)
                break
            metadata = dict(row, source_copy=reference)
            archive.writestr(folder + 'brief.json', json.dumps(metadata, ensure_ascii=False, indent=2) + '\n')
            text = '\n'.join([
                '$icon-making', '', f"# {row['name']}", '',
                f"Family/type: {family}", f"Status: {row['status']}",
                f"Pending brief ID: {row['id']}", f"Source icon: {row['icon']}",
                f"Reference path: {row['reference_path'] or 'Not linked'}",
                f"Reference image: {reference or 'Unavailable on this server; obtain the original before visual inspection.'}",
                f"Source revision: {row['svg_sha256']}",
                f"Rejected combination: {row['combination_type']}",
                f"Reason: {row['reason']}", '', '## Requested component', row['description'], '',
                'Inspect the reference and generate ONLY this standalone component. Do not recreate the whole combination.',
                'Preserve the old icon. Reuse a suitable standalone icon or create a separate file/variant; route through the matching icon skill.',
                'Validate and build the family, then link the resulting family/icon-id to this pending brief. Approval stays with the reviewer.',
                f"Already generated icon: {row['generated_icon'] or 'None'}", '',
            ])
            archive.writestr(folder + 'brief.md', text)
    return output.getvalue()
