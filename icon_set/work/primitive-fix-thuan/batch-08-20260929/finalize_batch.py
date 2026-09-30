from pathlib import Path
import json,sys,importlib.util
ROOT=Path(__file__).resolve().parents[4];sys.path.insert(0,str(ROOT))
from icon_set.scripts.primitive_fix import load_icon,run_module
BASE=Path(__file__).parent
rows=json.loads((BASE/'claims.json').read_text());runs=json.loads((BASE/'runs.json').read_text())
changes=[
'Rounded the head, added a thorax boundary, restored paired legs, and lifted the mirrored wings.',
'Rebuilt the cloud from round arcs and exposed a circular sun; lengthened three diagonal rain strokes.',
'Replaced the shallow hill with a taller rounded dome and restored a circular solar arc above it.',
'Enlarged the exposed sun into a circular arc; separated the cloud, lightning and two snow pellets.',
'Restored both eyes and a broad arched open mouth, with clear space beside the sweat drop.'
]
omissions=[
'Fine leg bends and additional narrow abdominal bands reduced; two legs and one abdominal stripe retained.',
'Fine solar-ray series reduced to one dot and one diagonal ray.',
'Two minor lateral rays omitted; three main rays retained.',
'Tiny solar rays omitted to preserve the large exposed disk; both snow marks retained.',
'Fine eyebrows omitted. Face outline opens behind the enlarged sweat drop to retain clearance.'
]
construction=[
'Lucide bug original and atomic-debug: paired antennae and structured body. Symmetric head/body, mirrored wings and legs.',
'Lucide cloud-sun-rain original and atomic-debug: joined circular cloud lobes, partly hidden sun and detached rainfall. Intentional upper-right sun.',
'Lucide sunrise original and atomic-debug: circular sun segment and separated radial rays. Symmetric hill and sun about x=24.',
'Lucide cloud-sun original and atomic-debug: a circular sun partly hidden by cloud. Sun is upper left, with lightning slightly right to preserve negative space.',
'No useful exact local Lucide face match. The supplied reference informs the worried mouth and sweat. Eyes sit left of the enlarged drop; the mouth and circular face are centered at x=24.'
]
report=['# Once-disapproved solo fix batch 08','', 'Requested 20 at offset 0 with --max-disapprovals 1. Production returned 5 eligible claims; history confirmed exactly one disapproval for each. No written reviewer feedback or reason was recorded for these five icons.','', 'All fixed modules use AUTHOR = "gpt-6". Each passed validate_icon() and the full build QA gate with zero warnings and was visually reviewed at 48 px in light and dark themes. Upload status is recorded below after finish completes.','']
for i,r in enumerate(rows):
 out=ROOT/runs[str(i)];module=run_module(out);icon=load_icon(module);validation=icon.validate_icon();g=json.loads((out/'gate.json').read_text());assert validation.status=='valid' and not validation.warnings and g['status']=='pass' and not g['warnings']
 meta=json.loads(next(out.glob('*.metadata.json')).read_text());key=r['key'].split('/')[1]
 finding=(out/'review-before.txt').read_text().splitlines()[0]
 visual=changes[i]+' Reviewed native and enlarged light/dark renders: clear identifying parts, smooth curved contours, and readable openings.'
 # Correct descriptive omissions from draft comments; geometry is unchanged.
 text=module.read_text();start=text.index('"""');end=text.index('"""',start+3)+3
 text='"""'+finding+'\n'+changes[i]+'\n'+construction[i]+'\nOmissions: '+omissions[i]+'\n"""'+text[end:];module.write_text(text)
 (out/'visual-review.txt').write_text(visual+'\n'+construction[i]+'\n'+omissions[i]+'\n')
 result={**meta,'source_path':r['ref'],'icon_id':key,'source_key':r['key'],'author':'gpt-6','validation_status':'valid','validation_errors':[],'validation_warnings':[],'build_gate':g,'comparison':finding,'reviewer_feedback':r['feedback'],'changes':changes[i],'visual_review':visual,'construction_references':construction[i],'omissions':omissions[i],'keyshape':icon.keyshape.name,'artifacts':{'module':module.name,'svg':key+'.svg','metadata':key+'.metadata.json','previews':[f'preview-{t}-{s}.png' for t in ['light','dark'] for s in [48,384]],'validation':'validation.txt','gate':'gate.json'}}
 (out/'result.json').write_text(json.dumps(result,indent=2)+'\n')
 report += ['## '+r['key'],'',finding,'',changes[i], '',construction[i], '', 'Omissions: '+omissions[i], '',f'Keyshape: {icon.keyshape.name}. AUTHOR: gpt-6. Model valid; full QA pass; zero warnings. Feedback: none recorded.','',f'[RESULT_DIR]({out}) · [SVG]({out/(key+".svg")}) · [Validation]({out/"validation.txt"})','']
report += ['## Artifacts','',f'[Before/reference comparison]({BASE.resolve()/"actual-comparison.png"}) · [Final light/dark review]({BASE.resolve()/"final-review.png"}) · [Eligibility history]({BASE.resolve()/"eligibility.json"})','']
(BASE/'REPORT.md').write_text('\n'.join(report))
(BASE/'finish-notes.json').write_text(json.dumps(changes,indent=2))
print('Finalized 5 standalone runs and batch report.')
