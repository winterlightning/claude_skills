"""Attach visual source-fidelity findings only to the exact reviewed model revision."""
import hashlib
import json
import shutil
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]

def resolve_audit_source(value, root=ROOT):
    """Keep saved audits portable when the repository checkout moves."""
    source = Path(value)
    candidate = source if source.is_absolute() else root / source
    if candidate.is_file():
        return candidate
    for folder in ('pictographic-primitives', 'pictographic-combinations'):
        if folder in source.parts:
            relative = Path(*source.parts[source.parts.index(folder):])
            relocated = root / relative
            if relocated.is_file():
                return relocated
    return candidate  # Preserve a real missing-file error rather than hiding it.

def annotate_sub_references(records, root=ROOT):
    path=root/'icon_set/data/sub-reference-fidelity.json'
    if not path.exists():return
    findings=json.loads(path.read_text())
    for record in records:
        record.pop('reference_fidelity',None)
        if record.get('family')!='sub':continue
        finding=findings.get(record['icon_id'])
        source=(record.get('python_source') or {}).get('path')
        if not finding or not source:continue
        model=root/source
        if model.is_file() and hashlib.sha256(model.read_bytes()).hexdigest()==finding['model_sha256']:
            record['reference_fidelity']=finding
    repair_path=root/'icon_set/data/sub-reference-repairs.json'
    if not repair_path.exists():return
    repairs=json.loads(repair_path.read_text())
    by_id={r['icon_id']:r for r in records if r.get('family')=='sub'}
    for icon_id, repair in repairs.items():
        parent=by_id.get(icon_id)
        if not parent or parent.get('reference_fidelity',{}).get('status')!='superseded':continue
        # A saved resolution cannot certify later edits or a missing replacement.
        if parent['reference_fidelity']['model_sha256']!=repair['parent_model_sha256']:continue
        finding=dict(parent['reference_fidelity'])
        if repair['status']=='redrawn':
            replacement=by_id.get(repair['new_id'])
            model=root/repair['new_model_path']
            if not replacement or replacement.get('build_failed') or not model.is_file():continue
            if hashlib.sha256(model.read_bytes()).hexdigest()!=repair['new_model_sha256']:continue
            if replacement.get('validation',{}).get('status')!='valid':continue
            finding.update(resolution='redrawn',replacement_id=repair['new_id'],review_url=repair['review_url'])
            replacement['reference_fidelity']={
                'status':'redrawn','source_id':repair['source_id'],
                'review_url':repair['review_url'],'finding':'Complete source composition redrawn and visually reviewed; awaiting human approval.',
                'model_sha256':repair['new_model_sha256'],
            }
        elif repair['status']=='skip':
            finding.update(resolution='skip',review_url=repair['review_url'],redraw_reason=repair['reason'])
        parent['reference_fidelity']=finding

def stage_sub_reference_review(target, root=ROOT):
    outlines=root/'work/sub-outline-restoration-20260918/report'
    if (outlines/'index.html').exists():
        shutil.copytree(outlines,target/'sub-outline-restoration',dirs_exist_ok=True)
    repairs=root/'work/sub-superseded-fix-20260918/report'
    if (repairs/'index.html').exists():
        shutil.copytree(repairs,target/'sub-reference-repairs',dirs_exist_ok=True)
    source=root/'work/sub-family-reference-audit'
    if not (source/'review.json').exists():return
    dest=target/'sub-family-review';dest.mkdir(exist_ok=True)
    for name in ('index.html','review.json','complete-redraws.zip'):shutil.copyfile(source/name,dest/name)
    shutil.copytree(source/'current',dest/'current',dirs_exist_ok=True)
    records=json.loads((source/'review.json').read_text())['records']
    for row in records:
        if row['original_url']:
            output=dest/row['original_url'];output.parent.mkdir(exist_ok=True)
            shutil.copyfile(resolve_audit_source(row['source_path'], root),output)
        for version in row['versions']:
            output=dest/version['url'];output.parent.mkdir(exist_ok=True)
            shutil.copyfile(root/'work/state-category-complete/svg'/version['file'],output)
