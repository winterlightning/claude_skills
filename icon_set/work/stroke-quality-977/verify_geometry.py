"""Check unchanged scope, source identity and the requested geometric invariants."""
import ast,hashlib,io,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
import cairosvg,numpy as np
from PIL import Image
from icon_set.model.icons.registry import create
from icon_set.model.primitives import Line
H=Path(__file__).parent
before=json.loads((H/'before.json').read_text());changes=json.loads((H/'changes.json').read_text());selected={r['id'] for r in changes}
def metadata(s):
 out={}
 for n in ast.parse(s).body:
  if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id in ('SOURCE_ICON_ID','SOURCE_PATH') for t in n.targets):
   out[n.targets[0].id]=ast.literal_eval(n.value)
 return out
for r in before:
 p=ROOT/r['source'];original=H/'before'/p.name
 assert metadata(p.read_text())==metadata(original.read_text()),r['id']
 changed=hashlib.sha256(p.read_bytes()).hexdigest()!=r['sha256']
 assert changed==(r['id'] in selected),r['id']
def alpha(id):
 svg=create(id).to_svg();return np.asarray(Image.open(io.BytesIO(cairosvg.svg2png(bytestring=svg.encode(),output_width=960,output_height=960))).getchannel('A'),dtype=float)/255
results={}
for id,kind in [('panoramic','both'),('amazon-web-service-game-tech','vertical'),('pen-4d7410cc','diagonal')]:
 a=alpha(id)
 mirrors=[np.fliplr(a),np.flipud(a)] if kind=='both' else [np.fliplr(a)] if kind=='vertical' else [np.flipud(np.fliplr(a)).T]
 errors=[float(np.abs(a-b).sum()/a.sum()) for b in mirrors]
 assert max(errors)<.01,(id,errors)
 results[id]=dict(symmetry=kind,raster_difference=errors)
hexagon=create('amazon-elastic-kubernetes-service');c=next(c for c in hexagon.contours if c.contour_id=='hexagon')
assert len(c.members)==6
lines=[p for p in hexagon.primitives if p.element_id in c.members];assert all(isinstance(p,Line) for p in lines)
points={p.start.as_tuple() for p in lines};assert {(48-x,y) for x,y in points}==points;assert {(x,48-y) for x,y in points}==points
results['amazon-elastic-kubernetes-service']=dict(sides=6,opposite_sides_equal=True,symmetric_about_both_axes=True)
results['scope']=dict(total=len(before),changed=len(selected),unchanged=len(before)-len(selected),source_ids_and_paths_preserved=True)
(H/'geometry-checks.json').write_text(json.dumps(results,indent=2));print(json.dumps(results,indent=2))
