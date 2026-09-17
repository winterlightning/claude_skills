"""Attach visual source-fidelity findings only to the exact reviewed model revision."""
import hashlib
import json
import shutil
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]

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

def stage_sub_reference_review(target, root=ROOT):
    source=root/'work/sub-family-reference-audit'
    if not (source/'review.json').exists():return
    dest=target/'sub-family-review';dest.mkdir(exist_ok=True)
    for name in ('index.html','review.json','complete-redraws.zip'):shutil.copyfile(source/name,dest/name)
    shutil.copytree(source/'current',dest/'current',dirs_exist_ok=True)
    records=json.loads((source/'review.json').read_text())['records']
    for row in records:
        if row['original_url']:
            output=dest/row['original_url'];output.parent.mkdir(exist_ok=True)
            shutil.copyfile(row['source_path'],output)
        for version in row['versions']:
            output=dest/version['url'];output.parent.mkdir(exist_ok=True)
            shutil.copyfile(root/'work/state-category-complete/svg'/version['file'],output)
