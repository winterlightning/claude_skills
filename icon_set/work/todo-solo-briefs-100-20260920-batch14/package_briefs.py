from pathlib import Path
import json,hashlib,shutil,subprocess,sys
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT))
P=Path(__file__).resolve().parent
rows=json.loads((P/'selection.json').read_text()); drafts=json.loads((P/'drafts.json').read_text())
held={1, 129, 131, 132, 11, 12, 13, 139, 142, 17, 18, 147, 20, 21, 22, 23, 24, 25, 26, 27, 30, 33, 35, 36, 37, 39, 41, 42, 43, 49, 50, 51, 52, 53, 70, 71, 72, 83, 84, 86, 92, 99, 100, 106, 113, 114, 115, 116, 117, 122, 125}
TYPE_GUIDANCE="Reuse the named preferred glyph and its stored paths from icon_set/typeface/glyphs.json. Do not generate, trace, or modify replacement letter geometry. Preserve natural proportions and baseline metrics; retain the full source identity."
GUIDANCE="You can try modifying a copy of the SVG reference to fit the icon design rules, or generate a new icon that matches the icon name. Either approach must follow the requested family's design rules and preserve the named subject's identity. Apply this only to the named component and exclude the other components. Keep the original reference unchanged."
def comp(name,family,description):return dict(name=name,family=family,description=description)
flagged={int(k):v for k,v in json.loads((P/'flagged.json').read_text()).items()}
triage=[]; manifests=[];flags=[]
shutil.copytree(P/'sheets',P/'triage-sheets')
for name in ['index.html','index.md']:
 shutil.copyfile(P/name,P/('triage-'+name))
for i,r in enumerate(rows):
 source=ROOT/'pictographic-primitives'/r['path']; copy=P/'sources'/source.name
 assert copy.read_bytes()==source.read_bytes()
 entry={'source_uuid':r['uuid'],'reference_path':source.relative_to(ROOT).as_posix(),'classification':'standalone','review_folder':None,'inspected_large':f'png/{source.stem}.png','inspected_native':f'png/{source.stem}@48.png'}
 if i not in held:
  d={k:v for k,v in drafts[i].items() if k!='index'};manifests.append({'file':source.name,**d})
  if i in [48,56,82,98,107,111,140]:
   flags.append({'source_uuid':r['uuid'],'concept':d['concept'],'note':'Primarily a symbol, diagram, or logo rather than a physical solo subject; retained as solo as requested.'})
  if i in []:flags.append({'source_uuid':r['uuid'],'concept':d['concept'],'note':'A page or article enclosure; retained as solo as requested.'})
  triage.append(entry);continue
 f=flagged[i]; kind=f['classification'];digest=hashlib.sha256(str(source).encode()+source.read_bytes()).hexdigest()[:12]
 group={'side_combination':'side','container_combination':'container','uncertain':'uncertain','typeface_reuse':'typeface'}[kind]
 review=P/'combination-review'/group/(source.stem+'-'+digest);review.mkdir(parents=True,exist_ok=False)
 shutil.copyfile(source,review/source.name)
 for suffix in ['.png','@48.png']:shutil.copyfile(P/'png'/(source.stem+suffix),review/(source.stem+suffix))
 shutil.move(str(P/'briefs'/(source.stem+'.md')),str(review/'initial-placeholder.md'))
 (review/'initial-placeholder.md').unlink() # own unedited placeholder; never a deliverable
 review_data={**entry,**f,'requested_family':'solo','review_status':'pending_human_review' if kind!='container_combination' else 'component_briefs_ready','main_subject':f['components'][0]['name'] if f['components'] else None,'modifier':f['components'][1]['name'] if len(f['components'])>1 else None,'modifier_position':f.get('modifier_position'),'uncertainty':f.get('uncertainty')}
 (review/'review.json').write_text(json.dumps(review_data,indent=2)+'\n')
 (review/'components.json').write_text(json.dumps({'source_uuid':r['uuid'],'reference_path':entry['reference_path'],'generation_held':kind in ['side_combination','uncertain'],'components':f['components']},indent=2)+'\n')
 markdown=[f"# {drafts[i]['concept']} — reference review",'',f"- source: `{entry['reference_path']}`",f"- source UUID: `{r['uuid']}`",f"- classification: {kind}",f"- review: {review_data['review_status']}",'',f['reason'],'','## Visual draft','',drafts[i]['description'],'']
 if f.get('uncertainty'):markdown+=['## Open question','',f['uncertainty'],'']
 for n,c in enumerate(f['components'],1):
  text=f"# {c['name']}\n\n- source: `{entry['reference_path']}`\n- source UUID: `{r['uuid']}`\n- family: {c['family']}\n- render: `{source.stem}.png`\n- native 48px reference: `{source.stem}@48.png`\n\n{c['description']}\n\n## Authoring handoff\n\n{GUIDANCE}\n"
  if c['family']=='typeface':text=text.replace(GUIDANCE,TYPE_GUIDANCE)
  (review/f'component-{n}.md').write_text(text)
  markdown += [f"## {n}. {c['name']} ({c['family']})",'',c['description'],'']
 markdown+=['## Authoring handoff','',TYPE_GUIDANCE if kind=='typeface_reuse' else GUIDANCE,'']
 if any(c['family']=='typeface' for c in f['components']):markdown+=['Typeface components must follow the reuse instructions above, never new icon generation.','']
 (review/'generation-draft.md').write_text('\n'.join(markdown))
 if kind!='uncertain' and len(f['components'])==2 and not any(c['family']=='typeface' for c in f['components']):
  request={'reference_path':entry['reference_path'],'source_id':r['uuid'],'combination_type':'container' if kind=='container_combination' else 'side','reason':f['reason'],'components':f['components']}
  dest=P/'pending-brief'/'requests'/(source.stem+'.json');dest.parent.mkdir(parents=True,exist_ok=True);dest.write_text(json.dumps(request,indent=2)+'\n')
  subprocess.run([sys.executable,str(ROOT/'icon_set/scripts/queue_brief.py'),'--file',str(dest),'--files-only','--out',str(P/'pending-brief')],check=True,stdout=subprocess.DEVNULL)
 (P/'held-sources').mkdir(exist_ok=True);shutil.move(str(copy),str(P/'held-sources'/copy.name))
 entry.update(classification=kind,review_folder=str(review.relative_to(P)),reason=f['reason']);triage.append(entry)
(P/'sources'/'manifest.json').write_text(json.dumps(manifests,indent=2)+'\n')
(P/'triage.json').write_text(json.dumps(triage,indent=2)+'\n');(P/'family-flags.json').write_text(json.dumps(flags,indent=2)+'\n')
assert len(manifests)==100
subprocess.run([sys.executable,str(ROOT/'icon_set/scripts/prepare_references.py'),str(P/'sources'),'--manifest',str(P/'sources/manifest.json'),'--native','48','--out',str(P)],check=True)
export=[]
for i,r in enumerate(rows):
 if i in held:continue
 source=ROOT/'pictographic-primitives'/r['path'];file=P/'briefs'/(source.stem+'.md');text=file.read_text();text=text.replace(str((P/'sources'/source.name).relative_to(ROOT)),str(source.relative_to(ROOT)))
 text=text.replace('## Description',f"- source UUID: `{r['uuid']}`\n\n## Description")
 text=text.replace('/icon-solo','$icon-solo');file.write_text(text)
 export.append({'uuid':r['uuid'],'reference_path':str(source.relative_to(ROOT)),'family':'solo','brief':text,'brief_file':str(file.relative_to(P))})
(P/'gallery-briefs.json').write_text(json.dumps(export,indent=2)+'\n')
print('Packaged',len(export),'solo briefs and',len(held),'review bundles')
