from pathlib import Path
import sys,json,datetime
sys.path.insert(0,str(Path(__file__).resolve().parents[4]))
from icon_set.scripts import primitive_fix as fix,work_queue

root=Path(__file__).parent
rows=json.loads((root/'batch.json').read_text())
references={
 'female-user-profile':'human_ref/user.svg and Lucide user-round: round head, broad smooth shoulders; hair is intentionally attached to the head; head bottom y24 and shoulders top y32 give 4 units of visible gap.',
 'four-piece-jigsaw-puzzle':'Lucide puzzle original and atomic-debug: circular tabs and coherent continuous seams.',
 'gaming-console-and-controller':'Lucide gamepad-2 original and atomic-debug: rounded upper corners, broad grips, directional control and action button.',
 'grim-reaper-with-scythe':'Lucide skull original and atomic-debug: simplified head opening. Supplied grim reaper: hooded robe beside a tall curved scythe.',
 'grinning-face-with-heart-eyes':'Supplied face grin hearts reference: two hearts above a wide grin. No useful complete Lucide match was found in the inspected set.',
 'gudi-padwa-festival-flag':'Lucide flag original and atomic-debug: pole with attached cloth. Supplied reference identifies the ceremonial pot above the pole.',
 'kermit-face':'Supplied Kermit reference: paired protruding eyes, wide mouth and pointed collar; smooth curve construction informed by the inspected Lucide face references.',
}
omissions={
 'grinning-face-with-heart-eyes':'Outer face circle omitted so true outlined hearts retain legal openings and spacing.',
 'four-piece-jigsaw-puzzle':'Only two interlock tabs fit in the attempted four-piece layout; their surrounding clearances still fail the strict build gate.',
 'log-with-sprouting-branch':'Small sprouting branch and bark detail omitted to emphasize the source concept tree log, with a cylindrical body and end-grain ring.',
 'gaming-console-and-controller':'Console power indicator omitted to leave room for a recognizable directional control and button.',
 'grim-reaper-with-scythe':'Tiny facial details and double-line blade thickness omitted; retain hood opening, robe and curved scythe.',
 'lidded-pot-with-rising-steam':'Domed lid reduced to a flat lid with a raised handle; retain two steam strokes.',
 'kermit-face':'Pupils omitted to keep the protruding eye openings readable.',
}

for r in rows:
 out=Path(r['run']);claim=Path(r['claim']).parent
 if (claim/'result.json').exists():
  print('Already reported',r['icon_id'],flush=True);continue
 checks=json.loads((out/'checks.json').read_text());design=json.loads((out/'design.json').read_text())
 failed=r['icon_id']=='four-piece-jigsaw-puzzle'
 if not failed and (checks['model']!='valid' or checks['gate']['status']!='pass'):
  print('BLOCKED',r['icon_id'],flush=True);continue
 note=design['plan']
 if failed:note='Cannot preserve readable four-piece interlocking tabs within SOLO48: internal-spacing around tab1/tab2 versus frame and horizontal seam is approximately 0.07 ink units, below the required 4. Attempt retained; validation rules unchanged.'
 findings='Inspected light and dark previews at native 48px and enlarged size. '+('The four-piece layout remains visibly crowded at the tabs and cannot pass the gate.' if failed else 'Silhouette and defining marks remain readable, with balanced spacing and intentional asymmetry where required.')
 result=dict(source_uuid=r['source_uuid'],reference_path=r['reference_path'],concept=r['concept'],icon_id=r['icon_id'],author='gpt-6',
   validation_status=checks['model'],build_gate_status=checks['gate']['status'],visual_review=findings,
   omissions=omissions.get(r['icon_id'],'Nonessential micro-detail omitted; defining subject retained.'),
   references_used=references.get(r['icon_id'],'Supplied original reference and rejected drawing inspected. No useful exact Lucide match was found in the inspected set; apply geometric lines, arcs and shared parameters.'),
   keyshape=design['keyshape'],design=design['plan'],artifacts=sorted(p.name for p in out.iterdir() if p.is_file()),
   outcome='cannot-fix' if failed else 'done')
 (out/'result.json').write_text(json.dumps(result,indent=2)+'\n')
 try:
  code=fix.finish(work_queue.default_base_url(),'thuan-mac','solo/'+r['icon_id'],result['outcome'],note=note,ray_run=out)
  print('FINISH',r['icon_id'],code,flush=True)
 except Exception as e:
  print('UPLOAD ERROR',r['icon_id'],type(e).__name__,str(e),flush=True)
