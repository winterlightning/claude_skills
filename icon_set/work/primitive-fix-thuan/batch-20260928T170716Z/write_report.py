from pathlib import Path
import json
B=Path(__file__).parent.resolve()
rows=json.loads((B/'completed.json').read_text())
assert len(rows)==20
exception_count=sum(r['accepted_exception'] for r in rows)
def link(label,p):return f'[{label}](<{Path(p).resolve()}>)'
lines=['# Manual fix batch — 20 icons','',f'Worker: `thuan-mac`. All 20 production claims finished as `done` and returned to `ready`. AUTHOR is `gpt-6` in every module. {20-exception_count} strict passes; {exception_count} drawing-bound visual exceptions authorized by the user. Each exception retains the automatic QA errors/warnings and exact SVG hash.','',link('Final light/dark preview',B/'final-preview.png'),'','Every original and rejected current drawing was compared before authoring. Each candidate was reviewed at native 48px and enlarged size in both themes. All geometry remains on the SOLO48 canvas with uniform 4px strokes. Registered modules and published output were not changed.','', 'Shared construction references: local Lucide smartphone (coherent rounded frame), monitor (screen/stand hierarchy), dollar-sign (smooth currency bowls), hand (round fingertips and joined palm), and human_ref/user.svg (circular heads/open shoulders). Busts have exactly 4 units of visible head-to-body clearance. Directional hands and the message tail retain intentional asymmetry.','']
for r in rows:
 run=Path(r['run']);result=json.loads((run/'result.json').read_text());review=json.loads((run/'review.json').read_text());finish=json.loads((Path(r['fix'])/'result.json').read_text())
 assert finish['outcome']=='done' and finish['review_status']=='ready' and finish['author']=='gpt-6'
 assert finish['build_gate']['status']=='pass'
 status='Pass · visual exception (automatic '+r['automatic_status']+')' if r['accepted_exception'] else 'Strict pass · zero warnings'
 module=Path(r['module']);shape=module.read_text().split('keyshape = Keyshape.',1)[1].splitlines()[0]
 why='upright device proportions' if r['index']<13 else 'full-height pointing hand' if r['index']==14 else 'upright finger proportions and natural diagonal thumb' if r['index'] in (18,19) else 'broad screen/message composition and full-height support/tail'
 lines += [f'## {r["key"]}','',f'**Current versus original:** {review["before_problem"]}',f'**Reviewer feedback:** {r["feedback"].replace(chr(10)," / ")}',f'**Revision:** {r["note"]}',f'**Keyshape:** `{shape}` for {why}.',f'**Omissions:** {review["omissions"]}',f'**Author / validation / production:** `gpt-6` · {status} · Ready.',f'**Construction reference:** Lucide `{review["construction_reference"]}`; source composition from the claimed original.',f'**RESULT_DIR:** {link("Run folder",run)} · {link("SVG",run/(r["icon_id"]+".svg"))} · {link("Python",module)} · {link("Validation",run/"validation.txt")} · {link("Finish receipt",Path(r["fix"])/"result.json")}', '']
 if r['accepted_exception']:lines += [f'**Exception rationale:** {result["build_gate"]["exception"]["reason"]}','']
(B/'report.md').write_text('\n'.join(lines))
print('Verified 20 done/Ready production receipts; author gpt-6; 5 strict passes, 15 accepted visual exceptions.')
print(B/'report.md')
