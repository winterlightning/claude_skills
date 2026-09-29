from pathlib import Path
import hashlib, json

ROOT=Path(__file__).resolve().parents[4]
HERE=Path(__file__).parent
rows=json.loads((HERE/'finals.json').read_text())
lines=['# Meaning repair batch — 20 completed', '',
       'Worker: `thuan-mac`. Author in every module: `gpt-6`.', '',
       'All 20 claimed icons were compared with their original and rejected drawings, redrawn in fresh standalone primitive-make-ray folders, reviewed at native 48px in light and dark themes, uploaded through primitive_fix.py finish, and returned to **Ready** on production.', '',
       '**Validation:** 1 full automatic pass with zero warnings; 19 user-authorized drawing-bound visual exceptions. The exceptions retain all automatic findings. They do not claim a strict geometry pass. Every export remains SOLO48 with uniform 4px strokes.', '',
       f'[Visual before/after review]({HERE / "review.html"})', '',
       'The feedback on every claim was: “Does not convey the intended meaning.”', '',
       'Original registered modules and published output were left untouched. These revisions are uploaded production work results; promotion remains separate.', '']
verified=[]
for index,row in enumerate(rows,1):
 out=ROOT/row['result_dir']
 receipt_path=ROOT/row['claim']/'result.json'
 receipt=json.loads(receipt_path.read_text())
 assert receipt['outcome']=='done'
 assert receipt['reported']['state']=='done'
 assert receipt['review_status']=='ready'
 assert receipt['worker']=='thuan-mac' and receipt['author']=='gpt-6'
 assert receipt['make_ray_run']==row['result_dir']
 assert receipt['uploaded']['has_python'] and receipt['uploaded']['has_validation']
 assert receipt['build_gate']['status']=='pass'
 assert receipt.get('accepted_exception',False)==bool(row['exception'])
 assert (ROOT/row['claim']/'after'/f'{row["icon_id"]}.svg').read_bytes()==(out/f'{row["icon_id"]}.svg').read_bytes()
 if row['exception']:
  assert hashlib.sha256((out/f'{row["icon_id"]}.svg').read_bytes()).hexdigest()==row['exception']['svg_sha256']
 status=('Accepted visual exception; automatic model '+row['validation_status']+', automatic full gate '+row['automatic_status']+'.'
         if row['exception'] else 'Full automatic pass; valid model, zero errors, zero warnings.')
 lines += [f'## {index}. `{row["key"]}`', '',
           f'**Original versus rejected:** {row["plan"]["wrong"]}', '',
           '**Feedback:** Does not convey the intended meaning.', '',
           f'**Changed:** {row["plan"]["change"]}', '',
           f'**Construction:** {row["plan"]["construction_reference"]}', '',
           f'**Keyshape:** `{row["plan"]["keyshape"]}` — selected for the subject’s orientation and overall proportion. '+
             ('The exception preserves its natural footprint or identity-bearing local details.' if row['exception'] else 'The ink exactly fits the profile envelope.'), '',
           f'**Author:** `gpt-6`. **Validation:** {status} **Production:** done → Ready.', '']
 if row['exception']:lines += [f'**Exception rationale:** {row["exception"]["reason"]}', '']
 lines += [f'**RESULT_DIR:** [{row["result_dir"]}]({out})', '',
           f'[SVG]({out / (row["icon_id"]+".svg")}) · [Python]({out / row["module"]}) · '+
           f'[Validation]({out / "validation.txt"}) · [Visual review]({out / "visual-review.md"}) · [Production receipt]({receipt_path})', '']
 verified.append(dict(key=row['key'],author='gpt-6',status='ready',outcome='done',
                      accepted_exception=bool(row['exception']),result_dir=row['result_dir'],
                      production_receipt=str(receipt_path.relative_to(ROOT))))
(HERE/'REPORT.md').write_text('\n'.join(lines))
(HERE/'completion.json').write_text(json.dumps(dict(count=20,worker='thuan-mac',author='gpt-6',automatic_passes=1,visual_exceptions=19,icons=verified),indent=2))
print(f'Verified {len(verified)} production done/Ready receipts, uploaded Python/validation, matching after SVGs and exception hashes.')
print(HERE/'REPORT.md')
