"""Before/after evidence and centerlines for the fixed 977-icon cohort."""
import hashlib,importlib.util,json,sys
import xml.etree.ElementTree as ET
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from icon_set.model.icons.registry import create
from icon_set.renderers.svg import _move_to,_segment
HERE=Path(__file__).parent
cohort=json.loads((ROOT/'icon_set/work/intersection-review-977/cohort.json').read_text())
baseline={r['id']:r for r in json.loads((HERE/'before.json').read_text())}
changes={r['id']:r for r in json.loads((HERE/'changes.json').read_text())}
validations={r['id']:r for r in json.loads((HERE/'validation.json').read_text())}
def geometry(icon):
 return dict(svg=icon.to_svg(),paths=[dict(id=p.element_id,d=_move_to(p)+_segment(p),start=p.start.as_tuple(),end=p.end.as_tuple()) for p in icon.primitives],strokes=len(ET.fromstring(icon.to_svg()).findall("{http://www.w3.org/2000/svg}path")),segments=sum(max(1,len(getattr(p,"segments",()))) for p in icon.primitives),primitives=len(icon.primitives),curve_segments=sum(len(getattr(p,'segments',())) for p in icon.primitives))
release=json.loads((ROOT/'icon_set/dist/solo48/manifest.json').read_text())
published={r['icon_id']:r for r in release['icons']}
assert all(r['icon_id'] in published for r in cohort)
rows=[]
for row in cohort:
 id=row['icon_id'];icon=create(id);current=geometry(icon);r=dict(id=id,category=row['category'],source=row['python_source']['path'],status='reconstructed' if id in changes else 'retained',current=current,sha256=hashlib.sha256((ROOT/row['python_source']['path']).read_bytes()).hexdigest())
 if id in changes:
  validation=published[id]['validation']
  assert validation['status']=='valid' and not validation['warnings'],id
  assert hashlib.sha256(current['svg'].encode()).hexdigest()==published[id]['svg_sha256'],id
  r['export_validation']=validation
  path=HERE/'before'/Path(r['source']).name;name='icon_set.model.icons.solo._before_'+str(len(rows));spec=importlib.util.spec_from_file_location(name,path);module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);original=getattr(module,row['python_source']['class_name'])()
  r.update(before=geometry(original),plan=changes[id]['plan'],reference=changes[id]['reference'],validation=validations[id],before_sha256=baseline[id]['sha256'])
 else:r.update(plan='Retained after the closer stroke and balance review.',before_sha256=baseline[id]['sha256'])
 rows.append(r)
out=dict(total=len(rows),reconstructed=len(changes),retained=len(rows)-len(changes),scope='Original fixed 977-icon json_to_solo cohort',review='All 599 curved icons inspected enlarged with centerlines; all 378 straight icons inspected enlarged. Reconstructed icons also inspected at native 48 px in both themes.',checks=json.loads((HERE/'geometry-checks.json').read_text()),rows=rows)
(HERE/'report.json').write_text(json.dumps(out,indent=2))
template=(HERE/'report-template.html').read_text();html=template.replace('__REPORT_DATA__',json.dumps(out,separators=(',',':')).replace('</','<\\/'))
(HERE/'index.html').write_text(html)
reports=ROOT/'icon_set/dist/reports';reports.mkdir(exist_ok=True)
(reports/'stroke-quality-977.html').write_text(html)
(ROOT/'icon_set/dist/gallery/stroke-quality-977.html').write_text(html)
print('Report:',out['total'],'icons;',out['reconstructed'],'reconstructed')
