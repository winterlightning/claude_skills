"""Independent role assignments for side sub-icons and container symbols.

This is a usage layer over SUB32, not a new canvas/profile. Shared drawings get
independent Python models. related_group links them without syncing geometry.
"""
from pathlib import Path
import ast,copy,csv,hashlib,inspect,json,xml.etree.ElementTree as ET
from collections import defaultdict,Counter

if __package__:
    from .workspace import build_dist
else:
    from workspace import build_dist

ROOT=Path(__file__).resolve().parents[2]
MANIFEST='icon_set/model/catalog/sub-usage-categories.json'

def geometry(doc):
    # Canonical structure is independent of ElementTree's global namespace
    # registration, which changes when the renderer and gallery are imported.
    def canonical(node):
        return [node.tag.rsplit('}',1)[-1],sorted(node.attrib.items()),[canonical(c) for c in node if c.tag.rsplit('}',1)[-1] not in ('title','desc')]]
    return json.dumps(canonical(ET.fromstring(doc)),separators=(',',':')).encode()


def stage_catalog(catalog,root=ROOT):
    path=root/MANIFEST
    if not path.exists():return
    # Catalog publication is read-only. Explicit maintenance refreshes role exports.
    data=json.loads(path.read_text())
    # The origin stays stable when a repaired variant replaces a role version.
    lookup={e['original_icon_id']:e for e in data['icons']}
    lookup.update({v['icon_id']:e for e in data['icons'] for v in e['versions'].values()})
    fixes=json.loads((root/'icon_set/work/container-fit-repair/fit-adjustments.json').read_text()).get('sub_revisions',{})
    for row in catalog['rows']:
        role='symbol' if row['kind']=='container' else 'side';choices=[];exports=[];seen=set();old_exports={x['icon']:x for x in row.get('sub_exports',[])}
        for choice in row.get('sub_generated',[]):
            original=lookup.get(choice['icon_id'],{}).get('original_icon_id',choice['icon_id'])
            if role=='symbol':
                overrides=[fixes.get(h['icon_id'],{}).get(original) for h in row.get('main_generated',[])]
                override=next((x for x in overrides if x),None)
                if override:original=override['variant']
            entry=lookup.get(original)
            if not entry or role not in entry['versions']:
                # A role copy discovered through source references must not leak
                # into the other role. New originals remain visible for triage.
                if entry:continue
                selected=dict(choice,usage_category=role)
            else:
                v=entry['versions'][role]
                selected=dict(choice,icon_id=v['icon_id'],key=v.get('family','sub')+'/'+v['icon_id'],preview_url=v['preview_url'],model_validation=v['model_validation'],usage_category=role,related_group=entry['related_group'],canonical_icon_id=original,related_icon_ids=[x['icon_id'] for k,x in entry['versions'].items() if k!=role])
                if not (root/v['svg']).is_file() and not (build_dist(root) / 'gallery'/v['preview_url']).resolve().is_file():
                    raise FileNotFoundError(v['svg'])
                source=old_exports.get(choice['icon_id']) or old_exports.get(original)
                if source:
                    exports.append(dict(source,icon=v['icon_id'],family=v.get('family','sub'),model_key=selected['key'],python_source=v['python_source'],svg=v['svg'],export_url=v['preview_url'],sha256=v['sha256'],model_validation=v['model_validation'],usage_category=role,related_group=entry['related_group']))
            if selected['icon_id'] not in seen:choices.append(selected);seen.add(selected['icon_id'])
        row['sub_generated']=choices;row['sub_exports']=list({x['icon']:x for x in exports}.values());row['sub_usage_category']=role

def initialize(root=ROOT):
    from icon_set.model.icons.registry import factories
    manifest=root/MANIFEST
    if manifest.exists():raise RuntimeError('Already categorized; refresh exports instead of recreating editable versions.')
    catalog=json.loads((build_dist(root) / 'gallery/combinations.json').read_text());paired=json.loads((root/'icon_set/work/container-pair-combinations/results.json').read_text());usage=defaultdict(lambda:defaultdict(set));sources={};defs=json.loads((root/'combination_data.json').read_text())
    for row in catalog['rows']:
        for s in row['sub_generated']:
            sources.setdefault(s['icon_id'],dict(doc=(build_dist(root) / 'gallery'/s['preview_url']).resolve().read_text(),status=s.get('model_validation','unknown')))
            if row['kind']=='side':usage[s['icon_id']]['side'].add(row['id'])
    for r in paired['rows']:
        s=paired['subs'][r[1]];sources[s['name']]=dict(doc=s['svg32'],status=s['model_validation']);usage[s['name']]['symbol'].add(r[9])
    models=factories();entries=[];pending=[]
    backup=root/'icon_set/work/sub-symbol-categories';backup.mkdir(parents=True,exist_ok=True)
    (backup/'catalog-before.json').write_text(json.dumps(catalog,separators=(',',':')))
    (backup/'container-results-before.json').write_text(json.dumps(paired,separators=(',',':')))
    for uid,roles in sorted(usage.items()):
        if uid not in models:raise ValueError('Missing editable model: '+uid)
        cls=models[uid];source=Path(inspect.getsourcefile(cls));module=inspect.getmodule(cls);versions={}
        for role in sorted(roles):
            new_id=uid;model_path=source
            if len(roles)==2 and role=='symbol':
                new_id=uid+'-symbol';source_id=getattr(module,'SOURCE_ICON_ID',None);suffix='_'+str(source_id).replace('-','_') if source_id else ''
                model_path=source.with_name(new_id.replace('-','_')+suffix+'.py')
                if new_id in models or model_path.exists():raise ValueError('Existing role-copy collision: '+new_id)
                tree=ast.parse(source.read_text());target=next(n for n in tree.body if isinstance(n,ast.ClassDef) and n.name==cls.__name__)
                if not any(isinstance(n,(ast.FunctionDef,ast.AsyncFunctionDef)) and n.name=='build' for n in target.body):raise ValueError('Inherited drawing requires explicit independent copy: '+uid)
                siblings={f.__name__ for f in models.values() if f.__module__==cls.__module__ and f is not cls}
                tree.body=[ast.ImportFrom(module=source.stem,names=[ast.alias(name=n.name)],level=1) if isinstance(n,ast.ClassDef) and n.name in siblings else n for n in tree.body]
                oldname=target.name;target.name=oldname+'ContainerSymbol'
                for node in ast.walk(tree):
                    if isinstance(node,ast.Name) and node.id==oldname:node.id=target.name
                attrs={'icon_id':new_id,'variant_of':uid,'variant_label':'Independent container symbol','usage_category':'symbol','related_group':'sub-origin/'+uid,'counterpart_icon_id':uid}
                target.body=[n for n in target.body if not (isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id in attrs for t in n.targets))]
                target.body[0:0]=[ast.Assign(targets=[ast.Name(id=k,ctx=ast.Store())],value=ast.Constant(v)) for k,v in attrs.items()]
                ast.fix_missing_locations(tree);text='# Independent container symbol; edit separately from linked side sub-icon.\n'+ast.unparse(tree)+'\n';compile(text,str(model_path),'exec');pending.append((model_path,text))
            asset=root/'icon_set/assets/sub-usage'/role/(new_id+'.svg');public=build_dist(root) / 'gallery/sub-usage'/role/(new_id+'.svg')
            versions[role]={'icon_id':new_id,'python_source':str(model_path.relative_to(root)),'svg':str(asset.relative_to(root)),'preview_url':'sub-usage/'+role+'/'+new_id+'.svg','sha256':hashlib.sha256(sources[uid]['doc'].encode()).hexdigest(),'model_validation':sources[uid]['status'],'initial_geometry_sha256':hashlib.sha256(geometry(sources[uid]['doc'])).hexdigest()}
        entries.append({'original_icon_id':uid,'related_group':'sub-origin/'+uid,'source_icon_id':getattr(module,'SOURCE_ICON_ID',None),'usage':'both' if len(roles)==2 else next(iter(roles)),'pair_ids':{k:sorted(v) for k,v in roles.items()},'versions':versions})
    # Plan every independent module before writing any of them.
    for path,text in pending:path.write_text(text)
    for e in entries:
        for v in e['versions'].values():
            for path in (root/v['svg'],build_dist(root) / 'gallery'/v['preview_url']):path.parent.mkdir(parents=True,exist_ok=True);path.write_text(sources[e['original_icon_id']]['doc'])
    counts=Counter(e['usage'] for e in entries)
    data={'schema_version':1,'policy':'Side sub-icons and container symbols are independent editable roles on SUB32. Shared origin links do not synchronize geometry. Existing validation states are retained. Unused library icons are not assigned speculatively.','counts':dict(counts),'side_icons':sum('side' in e['versions'] for e in entries),'symbols':sum('symbol' in e['versions'] for e in entries),'distinct_originals':len(entries),'independent_copies_created':len(pending),'defined_pairs':{k:len(v) for k,v in defs.items()},'icons':entries}
    manifest.write_text(json.dumps(data,indent=2));stage_catalog(catalog,root);(build_dist(root) / 'gallery/combinations.json').write_text(json.dumps(catalog,separators=(',',':')));print({k:v for k,v in data.items() if k!='icons'})

def refresh(root=ROOT):
    """Emit edited role copies; validation becomes stale when their geometry changes."""
    from icon_set.model.icons.registry import create
    path=root/MANIFEST;data=json.loads(path.read_text())
    for entry in data['icons']:
        for role,v in entry['versions'].items():
            doc=create(v['icon_id']).to_svg();digest=hashlib.sha256(geometry(doc)).hexdigest()
            if digest!=v.get('validated_geometry_sha256',v['initial_geometry_sha256']):v['model_validation']='stale-validation'
            for dst in (root/v['svg'],build_dist(root) / 'gallery'/v['preview_url']):
                dst.parent.mkdir(parents=True, exist_ok=True)
                dst.write_text(doc)
            v['sha256']=hashlib.sha256(doc.encode()).hexdigest()
    path.write_text(json.dumps(data,indent=2))

def annotate_records(records,root=ROOT):
    path=root/MANIFEST
    if not path.exists():return
    data=json.loads(path.read_text());lookup={v['icon_id']:(e,role) for e in data['icons'] for role,v in e['versions'].items()}
    for record in records:
        if record.get('family') not in ('sub','symbol') or record['icon_id'] not in lookup:continue
        entry,role=lookup[record['icon_id']]
        record['related_role_icons']=[{'key':v.get('family','sub')+'/'+v['icon_id'],'relationship':'Independent '+('container symbol' if k=='symbol' else 'side sub-icon')} for k,v in entry['versions'].items() if k!=role]
        record.update(usage_category=role,usage_label='Container symbol' if role=='symbol' else 'Side sub-icon',related_group=entry['related_group'],related_icon_ids=[v['icon_id'] for k,v in entry['versions'].items() if k!=role])

def validate_versions(ids,root=ROOT):
    from icon_set.model.icons.registry import create
    from icon_set.validation.library_qa import inspect_icon
    path=root/MANIFEST;data=json.loads(path.read_text());versions={v['icon_id']:v for e in data['icons'] for v in e['versions'].values()}
    for uid in ids:
        if uid not in versions:raise ValueError('Not a categorized icon: '+uid)
        model=create(uid);qa=inspect_icon(model);v=versions[uid]
        v['model_validation']=qa['status'];v['validated_geometry_sha256']=hashlib.sha256(geometry(model.to_svg())).hexdigest()
        evidence=root/'icon_set/work/sub-symbol-categories/validation';evidence.mkdir(exist_ok=True)
        (evidence/(uid+'.json')).write_text(json.dumps({k:qa[k] for k in ('status','errors','warnings')},indent=2))
    path.write_text(json.dumps(data,indent=2))

if __name__=='__main__':
    import argparse
    p=argparse.ArgumentParser();p.add_argument('--initialize',action='store_true');p.add_argument('--validate',action='append',default=[]);a=p.parse_args()
    if a.initialize:initialize()
    else:
        if a.validate:validate_versions(a.validate)
        refresh()
