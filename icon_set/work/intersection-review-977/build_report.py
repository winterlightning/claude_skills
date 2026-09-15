"""Read-only intersection-tip audit of the fixed 977-icon review cohort."""
import copy,hashlib,html,importlib.util,inspect,json,math,sys
from collections import Counter
from dataclasses import replace
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from icon_set.model.icons.registry import create
from icon_set.model.primitives import Line,Arc,Bezier,Point
from icon_set.validation.envelope import arc_geometry,centerline_bounds
from icon_set.renderers.svg import _move_to,_segment
HERE=Path(__file__).resolve().parent
CLEANUP=ROOT.parent/'icon_simplification/icon_model_python/solo_icon_core/intersection_cleanup.py'
spec=importlib.util.spec_from_file_location('cleanup_audit',CLEANUP);cleanup=importlib.util.module_from_spec(spec);spec.loader.exec_module(cleanup)
# Add observation immediately before the existing ink guard; thresholds and decisions are unchanged.
code=inspect.getsource(cleanup.clean_intersection_tips).replace('                if loss > max_ink_loss or coverage < .95:', "                graph.setdefault('observed_candidates', []).append(dict(element=e['id'],node=nid,carrier=carrier['id'],before=list(a),after=list(q),centerline_tail=tail,ink_loss=loss,ink_coverage=coverage))\n                if loss > max_ink_loss or coverage < .95:")
exec(code,cleanup.__dict__)
def graph(icon,arcs):
 coords={};elements=[]
 def node(pt):
  xy=tuple(pt)
  if xy not in coords:coords[xy]=str(len(coords))
  return coords[xy]
 for p in icon.primitives:
  e=dict(id=p.element_id,kind='arc',nodes=[node(p.start.as_tuple()),node(p.end.as_tuple())])
  if isinstance(p,Line):e['kind']='line'
  elif isinstance(p,Bezier):e.update(kind='polyline',cubics=p.segments)
  elif isinstance(p,Arc) and arcs:
   a=arc_geometry(p);n=max(8,math.ceil(abs(a.delta_angle)*max(a.radius_x,a.radius_y)/.08));n+=n%2
   e.update(kind='polyline',points=[tuple(round(v,9) for v in a.point(a.start_angle+a.delta_angle*k/n)) for k in range(n+1)])
  elements.append(e)
 for name,p in icon.anchors.items():elements.append(dict(id='anchor:'+name,kind='anchor',nodes=[node(p.as_tuple())]))
 nodes={nid:xy for xy,nid in coords.items()};junctions=[]
 for e in elements:
  if e['kind']!='line':continue
  a,b=[nodes[n] for n in e['nodes']];v=(b[0]-a[0],b[1]-a[1]);length2=v[0]**2+v[1]**2
  if not length2:continue
  for nid,p in nodes.items():
   if nid in e['nodes']:continue
   t=((p[0]-a[0])*v[0]+(p[1]-a[1])*v[1])/length2
   if 0<t<1 and math.dist(p,(a[0]+t*v[0],a[1]+t*v[1]))<=.25:junctions.append(dict(node=nid,on=e['id']))
 return dict(nodes=[dict(id=n,x=p[0],y=p[1]) for n,p in nodes.items()],elements=elements,junctions=junctions)
def unique(rows):
 out={}
 for r in rows:out[(r['element'],tuple(r['before']),tuple(r['after']),r['carrier'])]=r
 return list(out.values())
def paths(icon):
 return [dict(id=p.element_id,d=_move_to(p)+_segment(p),start=p.start.as_tuple(),end=p.end.as_tuple()) for p in icon.primitives]
def audit(row):
 icon=create(row['icon_id']);source=ROOT/row['python_source']['path'];beforehash=hashlib.sha256(source.read_bytes()).hexdigest()
 base=graph(icon,False);base_changes=cleanup.clean_intersection_tips(base)
 extended=graph(icon,True);accepted=cleanup.clean_intersection_tips(extended);candidates=unique(extended.get('observed_candidates',[]))
 original=icon.primitives;proposal={}
 for c in candidates:proposal.setdefault((c['element'],tuple(c['before'])),c)
 edited=[]
 for p in original:
  if isinstance(p,Line):
   a=proposal.get((p.element_id,p.start.as_tuple()));b=proposal.get((p.element_id,p.end.as_tuple()))
   p=replace(p,start=Point(*a['after']) if a else p.start,end=Point(*b['after']) if b else p.end)
  edited.append(p)
 status='clean';guard=None;afterpaths=None;aftersvg=None
 if candidates:
  icon.primitives=edited
  try:
   report=icon.validate_icon();same_bounds=max(abs(a-b) for a,b in zip(centerline_bounds(original),centerline_bounds(edited)))<=.01
   guard=dict(validation=report.status,bounds_preserved=same_bounds,findings=list(report.errors)+list(report.warnings))
   afterpaths=paths(icon);aftersvg=icon.to_svg()
   acceptedkeys={(c['element'],tuple(c['before']),tuple(c['after'])) for c in accepted}
   for c in candidates:
    c['ink_guard_passed']=(c['element'],tuple(c['before']),tuple(c['after'])) in acceptedkeys
    c['arc_carrier']=isinstance(next(p for p in original if p.element_id==c['carrier']),Arc)
   status='eligible' if all(c['ink_guard_passed'] for c in candidates) and report.ok and not report.warnings and same_bounds else 'manual'
  finally:icon.primitives=original
 assert hashlib.sha256(source.read_bytes()).hexdigest()==beforehash
 return dict(id=row['icon_id'],category=row.get('category',''),source=row['python_source']['path'],source_sha256=beforehash,source_id=row.get('source_icon_id'),status=status,paths=paths(icon),svg=icon.to_svg(),after_paths=afterpaths,after_svg=aftersvg,candidates=candidates,existing_function_trims=len(base_changes),guard=guard)
def main():
 rows=json.loads((HERE/'cohort.json').read_text());assert len(rows)==977 and len({r['icon_id'] for r in rows})==977
 out=[]
 for i,row in enumerate(rows):
  out.append(audit(row))
  if (i+1)%100==0:print('Scanned',i+1,flush=True)
 summary=dict(Counter(r['status'] for r in out));data=dict(total=len(out),summary=summary,method=str(CLEANUP),method_sha256=hashlib.sha256(CLEANUP.read_bytes()).hexdigest(),rows=out)
 (HERE/'report.json').write_text(json.dumps(data,ensure_ascii=False))
 template=(HERE/'report-template.html').read_text();page=template.replace('__REPORT_DATA__',json.dumps(data,ensure_ascii=False).replace('</','<\\/'))
 (HERE/'index.html').write_text(page)
 (ROOT/'icon_set/dist/gallery/intersection-review-977.html').write_text(page)
 print(summary,flush=True)
if __name__=='__main__':main()
