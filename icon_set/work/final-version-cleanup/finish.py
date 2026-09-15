from pathlib import Path
import sys,json,hashlib,re,collections,html
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from icon_set.model.icons.registry import factories
W=Path(__file__).parent;D=ROOT/'icon_set/dist';plan=json.loads((W/'plan.json').read_text());r=factories();renames={};verified=[]
for g in plan:
 for old in [g['latest']]+[v['icon_id'] for v in g['olds']]:renames[(g['family'],old)]=g['root']
 q=json.loads((D/'qa'/g['family']/g['root']/'metrics.json').read_text());assert q['status']==g['expected_status'],(g['root'],q['status'])
 assert q['svg_sha256']==g['new_sha'],g['root']
 folder={'solo':'solo48','sub':'sub32','container':'container64'}[g['family']];out=D/('failed/'+folder if q['status']=='fail' else folder)/(g['root']+'.svg')
 if not out.exists():out.write_text(r[g['root']]().to_svg())
 assert hashlib.sha256(out.read_bytes()).hexdigest()==g['new_sha']
 for old in [g['latest']]+[v['icon_id'] for v in g['olds'] if v['icon_id']!=g['root']]:
  assert not (D/folder/(old+'.svg')).exists(),old
 verified.append({'icon_id':g['root'],'status':q['status'],'sha256':g['new_sha']})
b=Path((W/'backup.txt').read_text().strip());restored=[]
for f in (b/'gallery').glob('*.html'):
 if f.name not in {'solo-review-batch-100.html','hole-review-batch-100.html','solo-remaining-review.html'}:continue
 s=f.read_text()
 for (family,old),new in sorted(renames.items(),key=lambda x:-len(x[0][1])):
  folder={'solo':'solo48','sub':'sub32','container':'container64'}[family]
  s=s.replace('/'+folder+'/'+old+'.svg','/'+folder+'/'+new+'.svg').replace('/qa/'+family+'/'+old+'/','/qa/'+family+'/'+new+'/')
  # A superseded failure can now resolve to the released final drawing.
  if json.loads((D/'qa'/family/new/'metrics.json').read_text())['status']=='pass':s=s.replace('../failed/'+folder+'/'+new+'.svg','../'+folder+'/'+new+'.svg')
 s=s.replace('Original versions remain available.','Superseded source versions are archived in the cleanup backup; this page links to the final icon names.').replace('The Failed build tab can still show preserved parent versions; this review counts the latest chosen version of each icon.','The active library now keeps one final version per icon.')
 (D/'gallery'/f.name).write_text(s);restored.append(f.name)
# Keep the current audit selection usable after canonical renaming.
p=ROOT/'icon_set/work/solo-visual-reaudit-500/selected.json';rows=json.loads(p.read_text());byroot={g['root']:g for g in plan}
for row in rows:
 new=renames.get(('solo',row['selected']))
 if new:
  row['selected']=new;row['file']=str(Path(byroot[new]['target_file']).relative_to(ROOT));row['svg_sha256']=byroot[new]['new_sha']
p.write_text(json.dumps(rows,indent=2)+'\n')
counts={}
for folder in ['solo48','sub32','container64']:
 m=json.loads((D/folder/'manifest.json').read_text());ids=[i['icon_id'] for i in m['icons']];assert not any(re.search(r'-v\d+$',i) for i in ids);assert len(ids)==len(set(ids));counts[folder]=len(ids)
(W/'verified.json').write_text(json.dumps(verified,indent=2)+'\n');(W/'summary.json').write_text(json.dumps({'registered':len(r),'released':counts,'removed_versions':sum(len(g['olds']) for g in plan),'groups':len(plan),'restored_pages':restored},indent=2)+'\n');print('Verified123 retained drawings and statuses.',counts,'Registered:',len(r));print('Restored review pages:',restored)
