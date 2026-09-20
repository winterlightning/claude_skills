import json,csv,html,sys
from collections import Counter,defaultdict
from pathlib import Path
W=Path(__file__).parent;ROOT=W.resolve().parents[2];sys.path.insert(0,str(ROOT))
from icon_set.model.icons.registry import create
load=lambda s:json.loads((ROOT/s).read_text())
rows=json.loads((W/'inventory.json').read_text());lookup={r['icon']:r for r in rows};aliases=load('icon_set/data/sub-profile-aliases.json');roles=load('icon_set/model/catalog/sub-usage-categories.json');pairs=load('icon_set/data/combination-pairs.json')['rows'];remaps={}
for e in roles['icons']:
 if 'side' not in e['versions']:continue
 v=e['versions']['side'];target=aliases.get(v['icon_id'],v['icon_id'])
 for key in [e['original_icon_id']]+[v['icon_id'] for v in e['versions'].values()]:remaps[key]=target
resolve=lambda uid:remaps.get(uid,aliases.get(uid,uid))
assigned=defaultdict(set)
for r in rows:
 for pid in r["pair_ids"]:assigned[pid].add(r["icon"])
blocked=Counter();paired=Counter();missing=set();ready=0;waiting=0;unmapped_pairs=[]
for p in pairs:
 ids=assigned[p['id']] or {resolve(x['icon']) for x in p['subs']};paired.update(ids);unknown=ids-set(lookup);missing.update(unknown)
 if unknown:
  unmapped_pairs.append(p["id"]);continue
 if any(lookup.get(uid,{}).get('status')=='pass' for uid in ids):ready+=1
 else:
  waiting+=1;blocked.update(uid for uid in ids if uid in lookup)
(W/"legacy-pair-mapping-issues.json").write_text(json.dumps(dict(pair_ids=unmapped_pairs,unmapped_icons=sorted(missing)),indent=2))
prior=load('icon_set/work/sub-failed-repair-50/audit.json')+load('icon_set/work/side-repair-50-priority-1/audit.json')+load('icon_set/work/side-repair-50-priority-2/audit.json')+load('icon_set/work/side-repair-50-priority-3/audit.json')+load('icon_set/work/side-repair-50-priority-4/audit.json')+load('icon_set/work/side-repair-50-priority-5/audit.json')+load('icon_set/work/side-repair-50-priority-6/audit.json')+load('icon_set/work/side-repair-50-priority-7/audit.json')+load('icon_set/work/side-repair-50-priority-8/audit.json')+load('icon_set/work/side-repair-50-priority-9/audit.json')+load('icon_set/work/side-repair-50-priority-10/audit.json')+load('icon_set/work/side-final-eight/audit.json');held={r['icon']:r['reason'] for r in prior if r['outcome']=='unresolved'}
for r in rows:
 r['side_combinations_using_icon']=len(set(r['pair_ids']));r['available_pairs_using_icon']=paired[r['icon']];r['waiting_pairs_using_icon']=blocked[r['icon']];r['previous_batch_unresolved']=r['icon'] in held;r['previous_issue']=held.get(r['icon'],'')
queue=sorted((r for r in rows if r['status']!='pass'),key=lambda r:(r['status']!='fail',r['previous_batch_unresolved'],-r['waiting_pairs_using_icon'],-r['side_combinations_using_icon'],r['icon']))
for i,r in enumerate(queue):r['priority']=i+1
next50=[r for r in queue if r['status']=='fail' and not r['previous_batch_unresolved']][:50]
counts={k:0 for k in ('pass','fail','review')}
counts.update(Counter(r['status'] for r in rows))
next_note=(f'All {len(rows)} selected side sub-icons pass. No repair or review items remain.' if not queue else f'Next batch: {len(next50)} unreviewed failed side sub-icons, prioritized by waiting combinations.' if next50 else 'All remaining failed profiles have documented issues. Revisit those designs and the separate review warnings; none is counted as repaired.')
summary=dict(side_sub_icons=len(rows),statuses=counts,repair_or_review=len(queue),paired_combinations=len(pairs),legacy_pairs_needing_mapping=len(unmapped_pairs),pairs_with_passing_sub=ready,pairs_waiting_for_passing_sub=waiting,freshly_validated=sum(bool(r.get('freshly_validated')) for r in rows),unchanged_saved_geometry_verified=sum(not r.get('freshly_validated',False) for r in rows),previous_batch_unresolved_in_side_queue=sum(r['previous_batch_unresolved'] for r in queue),next_batch_size=len(next50),policy='Side usage only. Resolve currently selected side variants and accepted repair aliases. Failed checks first; review-only warnings separate. Rank failures by waiting paired combinations, then total side usage. Previously unresolved batch entries are held separately. Counts refer to Python profiles, not human repair flags or cached combination SVGs.')
(W/'summary.json').write_text(json.dumps(summary,indent=2));(W/'repair-queue.json').write_text(json.dumps(queue,indent=2));(W/'next-50.json').write_text(json.dumps(next50,indent=2))
with (W/'repair-queue.csv').open('w') as f:
 fields=['priority','icon','status','waiting_pairs_using_icon','side_combinations_using_icon','previous_batch_unresolved','previous_issue'];w=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore');w.writeheader();w.writerows(queue)
assets=W/'svg';assets.mkdir(exist_ok=True);cards=[];nextids={r['icon'] for r in next50}
for r in queue:
 uid=r['icon'];(assets/(uid+'.svg')).write_text(create(uid).to_svg())
 cards.append(f'<tr data-status="{r["status"]}" data-next="{int(uid in nextids)}"><td>{r["priority"]}</td><td><img loading="lazy" src="svg/{uid}.svg" width="48" height="48"></td><td>{html.escape(uid)}'+(f'<small>Included in next {len(next50)}</small>' if uid in nextids else '')+('</td><td>Failed checks' if r['status']=='fail' else '</td><td>Needs review')+f'</td><td>{r["waiting_pairs_using_icon"]}</td><td>{r["side_combinations_using_icon"]}</td><td>{html.escape(r["previous_issue"])}</td></tr>')
(W/'index.html').write_text('''<!doctype html><html><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Side combination repair priority</title><style>body{margin:24px;font:14px system-ui;color:#21382d;background:#f5f7f5}h1{font-size:24px}p{max-width:950px;line-height:1.5}.stats{display:flex;gap:12px;flex-wrap:wrap}.stats b{padding:12px;background:white;border-radius:8px}input,select{padding:9px;font:inherit;margin:12px 8px 12px 0}table{border-collapse:collapse;width:100%;background:white}td,th{text-align:left;padding:10px;border-bottom:1px solid #dce5df}th{position:sticky;top:0;background:#e8eee9}td:last-child{font-size:12px;max-width:340px;line-height:1.45}small{display:block;color:#397856}a{color:#256b49}tr[hidden]{display:none}</style><h1>Side-combination sub-icons · current repair queue</h1>'''+f'<div class="stats"><b>{len(rows)} side sub-icons</b><b>{counts["pass"]} passing</b><b>{counts["fail"]} failed checks</b><b>{counts["review"]} review warnings</b></div>'+f'<p>{waiting} currently paired combinations still need a passing sub; {ready} have at least one passing sub option. These are eligibility counts, not regenerated combined SVGs. {len(unmapped_pairs)} additional legacy pair records need mapping and are excluded from those counts. {summary["freshly_validated"]} previously unknown profiles were checked; saved geometry hashes matched for the other {summary["unchanged_saved_geometry_verified"]}.</p><p>{next_note} Previously unresolved designs are retained at the end of the failure queue. Container symbols are excluded.</p><a href="repair-queue.csv">Download queue</a> · <a href="next-50.json">Unreviewed failures ({len(next50)})</a> · <a href="summary.json">Count details</a><br><input id="q" type="search" placeholder="Search icons"><select id="f"><option value="">All repair / review</option><option value="fail">Failed checks</option><option value="review">Review warnings</option><option value="next">Unreviewed failures ({len(next50)})</option></select><table><thead><tr><th>Priority</th><th>Icon</th><th>Name</th><th>Status</th><th>Waiting pairs</th><th>Side uses</th><th>Previously unresolved issue</th></tr></thead><tbody>'+''.join(cards)+'''</tbody></table><script>const q=document.getElementById('q'),f=document.getElementById('f'),rows=[...document.querySelectorAll('tbody tr')];function filter(){for(const r of rows)r.hidden=!(r.textContent.toLowerCase().includes(q.value.toLowerCase())&&(!f.value||(f.value==='next'?r.dataset.next==='1':r.dataset.status===f.value)));}q.oninput=filter;f.onchange=filter;</script></html>''')
print(json.dumps(summary,indent=2));print('First five:',[(r['icon'],r['waiting_pairs_using_icon']) for r in next50[:5]])
