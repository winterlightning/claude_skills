"""Save source-preserving, family-specific component handoffs for later authoring."""
import hashlib
import json
from pathlib import Path
import re
import os
from tempfile import TemporaryDirectory

from .brief_queue import validate_split


def save_split_handoffs(reference: Path, data: dict, output: Path) -> list[Path]:
    kind, parts, reason = validate_split(data)
    content = reference.read_bytes()
    source_hash = hashlib.sha256(content).hexdigest()
    source_path = data['reference_path']
    match = re.search(r'[0-9a-f]{8}(?:-[0-9a-f]{4}){3}-[0-9a-f]{12}', reference.stem, re.I)
    source_id = data.get('source_id') or (match[0] if match else None)
    normalized = {'reference_path': source_path, 'source_sha256': source_hash,
                  'source_id': source_id, 'combination_type': kind, 'reason': reason,
                  'components': parts}
    digest = hashlib.sha256(json.dumps(normalized, sort_keys=True, ensure_ascii=False).encode()).hexdigest()[:16]
    stem = re.sub(r'[^a-zA-Z0-9_-]+', '-', reference.stem).strip('-')[:100] or 'reference'
    folders = []
    for position, part in enumerate(parts, 1):
        family = part['family']
        name = part['name'].strip()
        other = parts[1 if position == 1 else 0]['name'].strip()
        record = {**normalized, 'status': 'pending-brief', 'component_position': position,
                  'concept': name, 'family': family, 'description': part['description'].strip(),
                  'icon_id': part.get('icon_id'), 'tags': part.get('tags', []),
                  'source_copy': reference.name, 'excluded_component': other}
        markdown = '\n'.join([
            '# ' + name, '', '- Status: pending-brief', '- Family: ' + family,
            '- Combination: ' + kind, f'- Component: {position} of 2',
            '- Original source: ' + source_path, '- Source copy: ' + reference.name,
            '- Source ID: ' + (str(source_id) if source_id else 'Not supplied'),
            '- Source SHA-256: ' + source_hash, '', '## Component to generate', '',
            part['description'].strip(), '', '## Exclude', '', other,
            '', '## Why the reference was split', '', reason or 'Two independently meaningful icons.',
            '', '## AI handoff', '', '$icon-making',
            'Process this pending component brief with the copied reference. Generate or reuse only '
            + name + ' as a standalone ' + family + ' icon. Do not recreate the combined reference.',
            'The source is an unchanged copy of the full reference, not an extracted component. '
            'Visually isolate the named part. Preserve its reference identity and use the matching family skill.',
            'Do not modify or move the original reference. Keep existing generated icons intact. '
            'Validate and build the new component; leave approval to the reviewer.', '',
        ])
        expected = {reference.name: content, 'brief.md': markdown.encode('utf-8'),
                    'brief.json': (json.dumps(record, indent=2, ensure_ascii=False) + '\n').encode('utf-8')}
        # Prevent a strangely named input from colliding with our brief files.
        if reference.name in ('brief.md', 'brief.json'):
            raise ValueError('Source filename conflicts with handoff metadata.')
        target = output / family / (stem + '-' + digest)
        target.parent.mkdir(parents=True, exist_ok=True)
        if target.exists():
            if not all((target/name).is_file() and (target/name).read_bytes() == payload for name,payload in expected.items()):
                raise FileExistsError(f'{target}: existing handoff differs; preserve it and choose another --out directory.')
        else:
            with TemporaryDirectory(prefix='.brief-stage-', dir=target.parent) as temp:
                staged = Path(temp) / 'bundle'
                staged.mkdir()
                for filename, payload in expected.items():
                    (staged/filename).write_bytes(payload)
                os.rename(staged, target)
        folders.append(target)
    return folders
