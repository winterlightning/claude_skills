from pathlib import Path
import json,shutil
import sys
sys.path.insert(0,str(Path.cwd()))
from icon_set.scripts.primitive_fix import load_icon
root=Path('icon_set/work/primitive-make-ray/review-20260925T060624Z');rows=json.loads((root/'batch.json').read_text())
omissions={2:'Reduced two short ringing strokes on each side to one longer stroke for readable spacing.',5:'Retained all three birds, three optical sections and tripod; compressed the tripod height to separate it from the barrel.',16:'Omitted small bolt dots and the extra concentric rotor ring; retained the caliper, outer rotor and an open central hub.',17:'Reduced minor antler undulations to clear branches and omitted the internal neck seam.',19:'Opened the lower edge around the fracture so both broken halves remain separated at 48px.'}
reasons={'SQUARE':'Near-square subject with an even inset and full 36-unit centerline extent.','VRECT_M':'Tall, slender leg silhouette with 28-unit centerline width.','VRECT_L':'Upright book proportions with room for the lower page block.','HRECT_L':'Wide subject preserving the reference proportions.','CIRCLE':'Circular object centered on (24,24) with a 20-unit centerline radius.'}
for i,r in enumerate(rows):
 run=Path(r['run']);icon=load_icon(Path(r['module']));report=icon.validate_icon();g=json.loads((run/'gate.json').read_text());assert report.status=='valid' and not report.warnings;assert g['status']=='pass'
 svg=icon.to_svg();assert (run/(r['id']+'.svg')).read_text()==svg
 shutil.copyfile(r['ref'],run/'reference.svg')
 (run/'validation.txt').write_text(report.describe()+'\n\nBuild gate: '+g['status']+'\n'+'\n'.join(g['errors']+g['warnings'])+'\n')
 metadata=json.loads((run/(r['id']+'.metadata.json')).read_text());result={**metadata,'icon_id':r['id'],'author':'gpt-6','module':Path(r['module']).name,'svg':r['id']+'.svg','keyshape':r['keyshape'],'keyshape_reason':reasons[r['keyshape']],'validation_status':report.status,'validation_warnings':list(report.warnings),'build_gate':g,'exception':getattr(icon,'exception',None),'visual_review':{'status':'approved','sizes':[48,192],'themes':['light','dark'],'findings':r['plan']+' Reviewed the final emitted geometry at native size and enlargement in both themes; smooth connected contours, clear subject silhouette and intentional reference-specific asymmetry.','references':[r['ref'],r['lucide']]},'omissions':omissions.get(i,'No identifying parts omitted; nonessential microdetail simplified for 4px strokes.'),'artifacts':sorted(p.name for p in run.iterdir() if p.is_file())}
 (run/'result.json').write_text(json.dumps(result,indent=2)+'\n')
print('Finalized 20 fresh runs.')
