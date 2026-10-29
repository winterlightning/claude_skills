"""Explicit, reviewed private source repairs; frozen master bytes remain intact."""
import json
from pathlib import Path
from ..treatments import geometry as g


def apply_derivations(root, name, original):
    root=Path(root).resolve()
    manifest=root/'source-derivations'/(name+'.json')
    if not manifest.exists():return original
    data=json.loads(manifest.read_text())
    if data.get('schema')!='fill-source-derivation/v1' or data.get('name')!=name:
        raise ValueError('source: invalid private derivation manifest')
    if not data.get('styles') or set(data['styles'])-{'normal','round','sharp'}:
        raise ValueError('source: private derivation needs explicit styles')
    selected=dict(original)
    for style,record in data['styles'].items():
        if record.get('verdict')!='accepted' or not all(record.get(k) for k in ('method','reason','reviewed_at','evidence')):
            raise ValueError('source: private source repair lacks actual accepted visual evidence')
        if record.get('original_source_sha256')!=original.get(style,{}).get('sha256'):
            raise ValueError('source: private repair no longer matches frozen styled master')
        if record.get('normal_master_sha256')!=original['normal']['sha256']:
            raise ValueError('source: private repair no longer matches original Normal master')
        path=(root/record['file']).resolve()
        if not path.is_relative_to(root/'derived-candidates') or not path.is_file() or g.sha(path)!=record.get('sha256'):
            raise ValueError('source: private derived SVG is missing, changed or outside candidate directory')
        for evidence in record['evidence']:
            proof=Path(evidence['file'])
            if not proof.is_file() or g.sha(proof)!=evidence.get('sha256'):
                raise ValueError('source: private source-review evidence changed')
        selected[style]={'file':str(path.relative_to(root)),'sha256':record['sha256']}
    return selected
