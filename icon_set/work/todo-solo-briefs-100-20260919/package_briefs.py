from pathlib import Path
import json,hashlib,shutil,subprocess,sys
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT))
P=Path(__file__).resolve().parent
rows=json.loads((P/'selection.json').read_text()); drafts=json.loads((P/'drafts.json').read_text())
held={9,10,20,37,41}
GUIDANCE="You can try modifying a copy of the SVG reference to fit the icon design rules, or generate a new icon that matches the icon name. Either approach must follow the requested family's design rules and preserve the named subject's identity. Apply this only to the named component and exclude the other components. Keep the original reference unchanged."
def comp(name,family,description):return dict(name=name,family=family,description=description)
flagged={
9:dict(classification='container_combination',reason='The tall side rails form a distinct open pipeline frame around a centered bracket-and-slash code glyph.',components=[comp('Open pipeline frame','container','Two tall vertical side rails with short outward ticks at their upper and lower ends. Keep the central area empty and exclude the code brackets and slash.'),comp('Code brackets and slash','sub','A left angle bracket and right angle bracket flank a rising forward slash. Exclude the surrounding pipeline rails.')]),
10:dict(classification='side_combination',reason='The branching node graph is an independent version-control action graphic beside and overlapping a separate code panel; the panel itself hosts a reusable code glyph.',modifier_position='upper-left of the code panel, with the branch crossing its open corner',components=[comp('Open rounded code panel','container','A rounded rectangular panel with an opening along the upper-left area. Complete its standalone boundary as appropriate; exclude the node graph, arrow, and code glyph.'),comp('Branching revision graph','sub','Three circular nodes form a vertical chain, with a curved branch passing through a fourth node and ending in an arrow pointing upper-left. Exclude the code panel and bracket-and-slash glyph.'),comp('Code brackets and slash','sub','Two opposing angle brackets surround a diagonal forward slash. Exclude the panel enclosure and branching node graph.')]),
20:dict(classification='uncertain',reason='A small cube sits in a cleared lower-right area beside converging stream lines, but no arrow or physical connection establishes whether it is a modifier or the stream destination.',uncertainty='Is the cube a separate data-storage badge applied to a stream icon, or an intrinsic destination in a single data-flow diagram? Preserve this question before authoring the complete reference.',components=[comp('Converging data stream','solo','Curved lines flow inward from above and below toward the right. In a possible separate-component treatment, exclude the lower-right cube; confirm the split before generation.'),comp('Isometric data cube','solo','A complete isometric cube shows its diamond-shaped top and two vertical side faces. In a possible separate-component treatment, exclude the stream lines; confirm the split before generation.')]),
37:dict(classification='container_combination',reason='The cart basket surrounds a separate cluster of three regular hexagonal glyphs, with no item-specific physical features linking the cluster to the cart.',components=[comp('Empty shopping cart','container','An open-topped shopping basket has a curved lower edge, a raised handle on the right, and two circular wheels below. Exclude the hexagonal contents and keep the basket empty.'),comp('Three-hexagon cluster','sub','Three touching outlined hexagons form a compact triangular group with one above and two below. Exclude the cart, handle, and wheels.')]),
41:dict(classification='side_combination',reason='A distinct bar-chart glyph fills a cleared lower-right corner of the stream lines and acts as an analytics qualifier rather than part of the flowing lines.',modifier_position='bottom-right, occupying a gap in the stream lines',components=[comp('Converging data stream','solo','Several broad curved stream lines sweep in from the upper and lower left and flatten toward the right. Exclude the lower-right bar chart.'),comp('Three-bar analytics chart','sub','Three thin upright bars of unequal height rise from a common horizontal baseline, with the middle bar tallest. Exclude the surrounding stream lines.')])}
triage=[]; manifests=[];flags=[]
for name in ['index.html','index.md']:
 shutil.copyfile(P/name,P/('triage-'+name))
for i,r in enumerate(rows):
 source=ROOT/'pictographic-primitives'/r['path']; copy=P/'sources'/source.name
 assert copy.read_bytes()==source.read_bytes()
 entry={'source_uuid':r['uuid'],'reference_path':source.relative_to(ROOT).as_posix(),'classification':'standalone','review_folder':None,'inspected_large':f'png/{source.stem}.png','inspected_native':f'png/{source.stem}@48.png'}
 if i not in held:
  d={k:v for k,v in drafts[i].items() if k!='index'};manifests.append({'file':source.name,**d})
  if i in [0,1,3,4,6,12,13,14,17,18,21,22,23,25,26,30,31,32,35,36,40,42,43,44,45,46,47,50,56,64,65,66,67,68,69,81,85,88,94,96]:
   flags.append({'source_uuid':r['uuid'],'concept':d['concept'],'note':'Primarily a symbol, diagram, or logo rather than a physical solo subject; retained as solo as requested.'})
  if i==63:flags.append({'source_uuid':r['uuid'],'concept':d['concept'],'note':'An empty architectural enclosure; retained as solo as requested.'})
  triage.append(entry);continue
 f=flagged[i]; kind=f['classification'];digest=hashlib.sha256(str(source).encode()+source.read_bytes()).hexdigest()[:12]
 group={'side_combination':'side','container_combination':'container','uncertain':'uncertain'}[kind]
 review=P/'combination-review'/group/(source.stem+'-'+digest);review.mkdir(parents=True,exist_ok=False)
 shutil.copyfile(source,review/source.name)
 for suffix in ['.png','@48.png']:shutil.copyfile(P/'png'/(source.stem+suffix),review/(source.stem+suffix))
 shutil.move(str(P/'briefs'/(source.stem+'.md')),str(review/'initial-placeholder.md'))
 (review/'initial-placeholder.md').unlink() # own unedited placeholder; never a deliverable
 review_data={**entry,**f,'requested_family':'solo','review_status':'pending_human_review' if kind!='container_combination' else 'component_briefs_ready','main_subject':f['components'][0]['name'],'modifier':f['components'][1]['name'],'modifier_position':f.get('modifier_position'),'uncertainty':f.get('uncertainty')}
 (review/'review.json').write_text(json.dumps(review_data,indent=2)+'\n')
 (review/'components.json').write_text(json.dumps({'source_uuid':r['uuid'],'reference_path':entry['reference_path'],'generation_held':kind in ['side_combination','uncertain'],'components':f['components']},indent=2)+'\n')
 markdown=[f"# {drafts[i]['concept']} — reference review",'',f"- source: `{entry['reference_path']}`",f"- source UUID: `{r['uuid']}`",f"- classification: {kind}",f"- review: {review_data['review_status']}",'',f['reason'],'','## Visual draft','',drafts[i]['description'],'']
 if f.get('uncertainty'):markdown+=['## Open question','',f['uncertainty'],'']
 for n,c in enumerate(f['components'],1):
  text=f"# {c['name']}\n\n- source: `{entry['reference_path']}`\n- source UUID: `{r['uuid']}`\n- family: {c['family']}\n- render: `{source.stem}.png`\n- native 48px reference: `{source.stem}@48.png`\n\n{c['description']}\n\n## Authoring handoff\n\n{GUIDANCE}\n"
  (review/f'component-{n}.md').write_text(text)
  markdown += [f"## {n}. {c['name']} ({c['family']})",'',c['description'],'']
 markdown+=['## Authoring handoff','',GUIDANCE,'']
 (review/'generation-draft.md').write_text('\n'.join(markdown))
 if kind!='uncertain' and len(f['components'])==2:
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
