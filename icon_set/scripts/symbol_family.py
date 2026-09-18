"""Stage editable SYMBOL32 models in the main management gallery.

These are managed models, including existing review drafts. Only the normal
build pipeline publishes validated release assets to dist/symbol32.
"""
from pathlib import Path
import json,hashlib,inspect,sys
ROOT=Path(__file__).resolve().parents[2]
def stage(target, records, root=ROOT):
    from icon_set.model.icons.registry import create
    from .sub_usage_categories import MANIFEST
    path=root/MANIFEST
    if not path.exists():return records
    data=json.loads(path.read_text());symbol_ids={e['versions']['symbol']['icon_id'] for e in data['icons'] if 'symbol' in e['versions']}
    # Old sub release manifests may still contain models moved into this family.
    records[:]=[r for r in records if not (r.get('family')=='sub' and r['icon_id'] in symbol_ids)]
    present={r['key'] for r in records};folder=target/'symbol-models';folder.mkdir(parents=True,exist_ok=True)
    for entry,v in [(e,v) for e in data['icons'] for v in e['versions'].values()]:
        family=v.get('family','sub');uid=v['icon_id'];key=family+'/'+uid
        folder=target/(family+'-models');folder.mkdir(parents=True,exist_ok=True)
        model=create(uid);doc=model.to_svg()
        role='symbol' if family=='symbol' else 'side'
        preview=target/'sub-usage'/role/(uid+'.svg');preview.parent.mkdir(parents=True,exist_ok=True);preview.write_text(doc)
        if key in present:continue
        (folder/(uid+'.svg')).write_text(doc);row=model.to_record();source=Path(inspect.getsourcefile(type(model)))
        row.update(key=key,family=family,profile=model.profile.name,preview_url=family+'-models/'+uid+'.svg',svg_sha256=hashlib.sha256(doc.encode()).hexdigest(),python_source={'path':str(source.relative_to(root)),'family':family,'class_name':type(model).__name__},author=getattr(sys.modules[type(model).__module__],'AUTHOR',''),usage_category='symbol' if family=='symbol' else 'side',model_validation=v['model_validation'],managed_draft=True,release_eligible=False,validation={'status':v['model_validation'],'provenance':'Existing geometry validation retained during family migration; independent release build required.'},variant_root=uid)
        records.append(row)
    return records
