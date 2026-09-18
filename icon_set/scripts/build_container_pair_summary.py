"""Summarize the current defined-pair vector gallery without changing artwork."""
from pathlib import Path
from collections import Counter
from datetime import datetime, timezone
import json,csv,html
BASE=Path(__file__).resolve().parents[1]
def main():
 out=BASE/'work/container-pair-combinations';d=json.loads((out/'results.json').read_text());rows=d['rows'];status=d['statuses'];esc=html.escape
 reasons=Counter();records=[];hosts=[]
 for r in rows:
  h,s=d['hosts'][r[0]],d['subs'][r[1]];st=status[r[2]];reason=[]
  if s['model_validation']!='pass':reason.append('Sub-icon drawing: '+s['model_validation'])
  if h['area_status']!='vector':reason.append('Interior needs review: '+h['area_status'])
  if r[7]=='review':reason.append('Fit measurement inconclusive')
  if h.get('error') or s.get('error'):reason.append(h.get('error') or s.get('error'))
  if st=='review':
   reasons['Sub-icon drawing needs correction' if s['model_validation']!='pass' else 'Interior or fit needs review']+=1
  records.append({'pair_id':r[9],'concept':r[10],'container':h['name'],'sub_icon':s['name'],'status':st,'fit_32':r[7] or 'untested','fit_24':r[8] or 'untested','gap_32_lower':r[5][0] if r[5] else '', 'gap_24_lower':r[6][0] if r[6] else '', 'priority':r[15]['action'] if r[15] else '', 'reason':'; '.join(reason),'suggestion':r[13]})
 for h in d['hosts']:
  rr=[r for r in records if r['container']==h['name']];hosts.append({'container':h['name'],'previews':len(rr),**{s:sum(r['status']==s for r in rr) for s in status}})
 with (out/'pair-report.csv').open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(records[0]));w.writeheader();w.writerows(records)
 summary={'generated_utc':datetime.now(timezone.utc).isoformat(),'defined_pairs':d['defined_pairs'],'resolved_pairs':d['resolved_pairs'],'previews':len(rows),'containers':len(hosts),'sub_assets':len(d['subs']),'missing':len(d['missing']),'statuses':d['counts'],'geometric_fit_32':dict(Counter(r['fit_32'] for r in records)),'review_reasons':dict(reasons),'repair_priorities':json.loads((out/'repair-priorities.json').read_text())['counts'],'containers_report':hosts}
 (out/'summary.json').write_text(json.dumps(summary,indent=2))
 labels={'keep-32':'Keep native 32','suggest-24':'24-unit preview fits','no-fit-at-center':'Neither size fits','review':'Needs review','blocked':'Size not assessed'}
 cards=''.join('<div class="metric"><strong>'+str(d['counts'].get(s,0))+'</strong>'+labels[s]+'</div>' for s in status)
 trs=''.join('<tr><td>'+esc(h['container'])+'</td>'+''.join('<td>'+str(h[k])+'</td>' for k in ['previews',*status])+'</tr>' for h in sorted(hosts,key=lambda h:(-h['no-fit-at-center'],-h['review'],h['container'])))
 report=f'''<!doctype html><html><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>All defined container pairs · report</title><style>body{{font:15px system-ui;color:#233047;background:#f5f7fa;margin:32px;line-height:1.6}}a{{color:#245bc1}}h1{{margin-bottom:8px}}.metrics{{display:flex;flex-wrap:wrap;gap:12px}}.metric,section{{background:white;border:1px solid #dbe2eb;border-radius:12px;padding:20px;margin:12px 0}}.metric{{min-width:145px}}strong{{display:block;font-size:30px}}table{{width:100%;border-collapse:collapse}}th,td{{text-align:left;padding:10px;border-bottom:1px solid #e3e7ed}}th{{position:sticky;top:0;background:white}}input{{padding:12px;width:min(420px,90%);border:1px solid #bdc8d6;border-radius:8px}}.scroll{{overflow:auto}}small{{color:#657185}}</style><h1>All defined container pairs</h1><p>{d['resolved_pairs']:,} / {d['defined_pairs']:,} defined pairs resolved · {len(rows):,} previews · {len(hosts)} containers · {len(d['missing'])} missing pairs.</p><p>Multiple mapped source variants can produce more than one preview for a pair. Only existing pairs are combined.</p><p><a href="index.html">Open all combinations on the 64 × 64 vector grid</a> · <a href="pair-report.csv">Download detailed report</a> · <a href="repair-priorities.html">Repair suggestions</a></p><div class="metrics">{cards}</div><section><h2>What needs attention</h2><p><b>{reasons['Sub-icon drawing needs correction']:,}</b> review previews have sub-icon drawing issues. <b>{reasons['Interior or fit needs review']:,}</b> need an interior or fit decision. Review does not automatically mean the container is too small.</p><p><b>{summary['geometric_fit_32'].get('pass',0):,}</b> previews pass the native-size spacing check, including some whose source sub-icon still needs correction. These are distinct checks.</p><p>The {d['counts'].get('blocked',0):,} unassessed previews retain wide or non-square source dimensions; the square 32/24 sizing test does not apply. They remain visible in the grid.</p><p>24-unit previews are scaled fit prototypes. A final grid-snapped 24-unit drawing still needs authoring and validation. Container repair suggestions preserve recognizable proportions and prioritize centered placement.</p></section><section><h2>Per-container results</h2><input id="search" placeholder="Find a container" aria-label="Find a container"><div class="scroll"><table><thead><tr><th>Container</th><th>Previews</th>{''.join('<th>'+labels[s]+'</th>' for s in status)}</tr></thead><tbody>{trs}</tbody></table></div></section><small>Generated {esc(summary['generated_utc'])}. Detailed rows and conservative gap measurements are included in the CSV.</small><script>document.querySelector('#search').addEventListener('input',e=>{{for(const r of document.querySelectorAll('tbody tr'))r.hidden=!r.cells[0].textContent.toLowerCase().includes(e.target.value.toLowerCase())}})</script></html>'''
 (out/'summary.html').write_text(report)
 print(json.dumps({k:v for k,v in summary.items() if k!='containers_report'},indent=2))
if __name__=='__main__':main()
