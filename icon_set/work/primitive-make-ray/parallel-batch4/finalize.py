from pathlib import Path
import json,re,shutil
from PIL import Image,ImageDraw
SOURCE_ICON_ID=None
SOURCE_PATH=None
AUTHOR='gpt-6'
b=Path(__file__).parent
items=json.loads((b/'items.json').read_text())
notes={
1:('Overlapping phone and banknote retain the dollar mark, with a shared lower seam.','Square envelope accommodates the overlapping upright phone and landscape bill.','smartphone'),
2:('Detached head, reclining torso, blanket and one large Z remain readable.','Square envelope separates the sleeper from the large Z.','bed'),
3:('Sun, two-row solar panel and tall lightning charger remain in the reference arrangement.','Square envelope balances the panel with the tall charger.','sun'),
4:('SE lettering has open eight-unit bar spacing; a diagonal needle divides the small compass dial.','Portrait envelope stacks a compact dial over full-height lettering.',None),
5:('Single-stroke P has a large clear counter inside the rounded square.','Square envelope preserves the parking sign.','square-parking'),
6:('Small head and open shoulders remain legible inside the square enclosure.','Square envelope preserves the confined-person frame.',None),
7:('Crossing scissors blades, two open handle loops and partial female symbol remain separated.','Square envelope retains the scissors on the left and symbol at upper right.','scissors'),
8:('Full yuan mark retains two bars; the clipped tag corner remains visible.','Square envelope widens the tag body around the complete currency symbol.',None),
9:('Two sheets, an asymmetric check and a text rule remain clear at native size.','Square envelope preserves the overlapping page arrangement.',None),
10:('Open hand with two broad finger groups and thumb sits beside a processor with four pins.','Horizontal envelope separates the upright hand from the small processor.','hand'),
11:('Widened basketball retains a curved seam and upper crossing meridian above a smoothly notched ticket.','Square envelope makes room for the ball above the ticket.',None),
12:('Forward-leaning seated figure, sloped lower leg, bowl and check remain visible.','Square envelope separates the head, check and toilet.',None),
13:('More upright seated figure, vertical lower leg, bowl and X distinguish the wrong-use pose.','Square envelope separates the head, X and toilet.',None),
14:('Headline and text rule identify a page; the rising chart forms its lower right boundary.','Square envelope preserves the newspaper page.','file'),
15:('Triangular sail, open hull and two curved transfer arrows remain readable with clear gaps.','Square envelope leaves room below and beside the boat for the transfer arrows.','sailboat')}
human={2:'full_body_ref.png: head center (14,24), radius 5; torso begins (14,37), yielding exactly 8 centerline / 4 ink clearance. Figure is flagged.',6:'user.svg: head center (24,17), radius 2; shoulder crest (24,27), yielding exactly 8 centerline / 4 ink clearance.',10:'Shared human-reference guidance and Lucide hand construction informed the palm, thumb and reduced finger groups.',12:'full_body_ref.png: head center (20,11), radius 5; neck (15,23) lies 13 from the center, yielding exactly 8 centerline / 4 ink clearance. Figure is flagged.',13:'full_body_ref.png: head center (20,11), radius 5; neck (20,24) lies 13 from the center, yielding exactly 8 centerline / 4 ink clearance. Figure is flagged.'}
results=[];rows=[]
sheet=Image.new('RGB',(1100,930),'#e4e7eb');draw=ImageDraw.Draw(sheet)
for n,it in enumerate(items,1):
 run=Path(it['run']);mod=next(run.glob('*.py'));s=mod.read_text();ident=re.search(r"icon_id=['\"]([^'\"]+)",s)[1]
 gate=(run/'build-gate.txt').read_text();validation=(run/'validation.txt').read_text()
 assert 'BUILD GATE PASS (pass, 0 errors, 0 warnings)' in gate,(n,gate)
 assert validation.strip()=='status: valid',(n,validation)
 review,why,lucide=notes[n];design=json.loads((run/'design.json').read_text());omissions=design['omissions']
 if n==4:omissions='Dial ticks omitted; narrow triangular needle replaced by a diagonal diameter to leave two open dial regions.'
 design.update(omissions=omissions,keyshape_reason=why,visual_review=review)
 (run/'design.json').write_text(json.dumps(design,indent=2)+'\n')
 header='"""'+it['concept']+': fresh parallel-spacing repair.\nPlan: '+review+'\nKeyshape '+design['keyshape']+': '+why+'\nOmissions: '+omissions+'\n"""'
 s=re.sub(r'\A""".*?"""',lambda m:header,s,count=1,flags=re.S);mod.write_text(s)
 meta={k:it[k] for k in ['concept','source_uuid','reference_path']}
 (run/f'{ident}.metadata.json').write_text(json.dumps(meta,indent=2)+'\n');shutil.copyfile(it['reference_path'],run/'reference.svg')
 refs=[it['reference_path']]
 if lucide:
  for kind in ['original','atomic-debug']:
   path=f'icon_set/references/lucide/{kind}/{lucide}.svg'
   assert Path(path).exists(),path
   refs.append(path)
 if n==10:
  refs.extend(f'icon_set/references/lucide/{kind}/cpu.svg' for kind in ['original','atomic-debug'])
 if n in human:refs.append('icon_set/references/human_ref/'+('user.svg' if n==6 else 'full_body_ref.png'))
 result={**meta,'source_path':it['reference_path'],'icon_id':ident,'author':'gpt-6','result_dir':str(run),'module':mod.name,'svg':ident+'.svg','keyshape':design['keyshape'],'keyshape_reason':why,'validation_status':'valid','validation_errors':0,'validation_warnings':0,'build_gate':'pass','build_gate_errors':0,'build_gate_warnings':0,'status':'pass','visual_review':review+' Reviewed at 48px and enlarged in both light and dark themes.','omissions':omissions,'references':refs,'construction_reference':lucide or 'No useful local Lucide match for this complete composition; reference geometry was freshly reconstructed.','attempt_count':len(list((run/'attempts').glob('*.py'))),'blockers':[],'artifacts':sorted(p.name for p in run.iterdir() if p.name!='result.json')}
 if n in human:result['human_reference_verification']=human[n]
 (run/'result.json').write_text(json.dumps(result,indent=2)+'\n');results.append(result)
 root=run.resolve();rows.append(f'| {n} | `{it["reference_path"]}` | PASS | [run]({root}) · [SVG]({root}/{ident}.svg) | {omissions} |')
 x=(n-1)%5*220;y=(n-1)//5*310
 for j,t in enumerate(['light','dark']):
  sheet.paste(Image.open(run/f'{t}-240.png').resize((130,130)),(x,y+130*j));sheet.paste(Image.open(run/f'{t}-48.png'),(x+145,y+45+130*j))
 draw.text((x+3,y+265),f'{n}. {it["concept"][:27]}',fill='black')
sheet.save(b/'review-final.png')
report='# Parallel edges — batch 4 of 9\n\n15 passed; 0 blocked. Every final module passes validate_icon() and BUILD GATE with zero errors and zero warnings. All 15 references received fresh standalone runs. No registered originals, published output or gallery files were changed. Author: `gpt-6`.\n\n[Native light/dark review sheet](review-final.png)\n\nRepeated lines were spaced at least 8 units apart. Small features were reduced where needed; the table records every reduction. Real contact points share endpoints and scoped connect relationships. Failed attempts and the final gate output are retained in each run. Visual review prompted a more asymmetric task check and a second basketball seam, both revalidated.\n\n| # | Reference | Result | Artifacts | Reductions |\n|---|---|---|---|---|\n'+'\n'.join(rows)+'\n'
(b/'REPORT.md').write_text(report);(b/'results.json').write_text(json.dumps(results,indent=2)+'\n')
print('15 passes; 0 blocked. Attempts:',[r['attempt_count'] for r in results])
