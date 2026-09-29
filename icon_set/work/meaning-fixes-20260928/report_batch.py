from pathlib import Path
import json,html,os
ROOT=Path('icon_set/work/meaning-fixes-20260928');R=json.loads((ROOT/'runs.json').read_text());base=Path.cwd()
lines=['# Meaning fixes — thuan-mac','', '20 claimed icons revised and returned to Ready through `primitive_fix.py finish`. All modules use `AUTHOR = "gpt-6"`. Two automatically pass with zero warnings; 18 use user-authorized, drawing-bound visual exceptions. Automatic findings remain in each validation report.','', 'The original and rejected SVGs were rendered and visually compared before drawing. Final candidates were inspected at 48px and enlarged in both light and dark themes. All retained the SOLO48 canvas and uniform 4px strokes.','', '[Visual comparison gallery](index.html)','']
cards=[]
for n,r in R.items():
 out=Path(r['result_dir']);f=Path(r['fix'])/'result.json';done=json.loads(f.read_text());assert done['outcome']=='done',f
 result=json.loads((out/'result.json').read_text());v=json.loads((out/'validation.json').read_text())
 assert done['author']=='gpt-6' and done['build_gate']['status']=='pass',done
 svg=out/(r['id']+'.svg');runlink=str((base/out).resolve());svglink=str((base/svg).resolve())
 lines += [f'## {n}. `{r["key"]}`','',f'- **Before:** {r["problem"]}',f'- **Reviewer feedback:** {r["feedback"].replace(chr(10)," / ")}',f'- **Changed:** {r["change"]}',f'- **Keyshape:** `{r["keyshape"]}`; follows the dominant subject envelope, with the natural proportions retained where excepted.',f'- **Construction reference:** {r["construction_reference"]}. The original reference determines the subject; local Lucide original/atomic geometry informs round enclosures, coherent curves or repeated circles as applicable.',f'- **Omissions:** {r["omissions"]}',f'- **Artifacts:** [RESULT_DIR]({runlink}) · [SVG]({svglink}) · [validation]({runlink}/validation.txt)',f'- **AUTHOR:** `gpt-6`.',f'- **Status:** production `done` → Ready; full QA `{r["release_status"]}`; automatic model `{v["status"]}`.', '']
 if r.get('exception_reason'):lines += [f'**Exception:** {r["exception_reason"]} The approval identifies the user-delegated judgment and exact SHA-256; it does not erase automatic errors or warnings.','']
 if r.get('human_construction'):lines += [f'**Human construction:** {r["human_construction"]} Shared reference: `icon_set/references/human_ref/`.','']
 rel=lambda p:html.escape(os.path.relpath(p,ROOT))
 images=[]
 for title,p in [('Original',out/'reference.png'),('Rejected',out/'before.png'),('Revised light',out/'preview-light-384.png'),('Revised dark',out/'preview-dark-384.png')]:
  images.append(f'<figure><figcaption>{title}</figcaption><img class="large" src="{rel(p)}"><img class="native" src="{rel(p)}"></figure>')
 cards.append(f'<article><h2>{n}. {html.escape(r["id"])}</h2><p>{html.escape(r["change"])}</p><div class="images">{"".join(images)}</div><p><strong>{html.escape(r["release_status"])}</strong> · Ready · AUTHOR gpt-6 · <a href="{rel(svg)}">SVG</a> · <a href="{rel(out/"validation.txt")}">Validation</a></p></article>')
(ROOT/'REPORT.md').write_text('\n'.join(lines))
(ROOT/'index.html').write_text('<!doctype html><meta charset="utf-8"><title>20 meaning fixes</title><style>body{font:16px system-ui;background:#eee;color:#222;max-width:1100px;margin:32px auto}article{background:white;padding:24px;margin:24px 0;border-radius:14px}h2{font-size:20px}p{line-height:1.5}.images{display:flex;gap:16px}figure{margin:0;flex:1}figcaption{margin:10px 0;color:#555}.large{width:200px;height:200px;display:block}.native{width:48px;height:48px;display:block;margin:18px auto}a{color:#254b9d}</style><h1>20 meaning fixes</h1><p>All 20 returned to Ready. Two automatic passes; 18 accepted visual exceptions. Native previews appear below each enlarged drawing.</p>'+''.join(cards))
summary={'claimed':20,'done':20,'automatic_pass':sum(r['release_status']=='pass' for r in R.values()),'visual_exceptions':sum(r['release_status']=='pass-exception' for r in R.values()),'worker':'thuan-mac','author':'gpt-6','keys':[r['key'] for r in R.values()]}
(ROOT/'summary.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps(summary,indent=2))
