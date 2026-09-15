from pathlib import Path
import sys,json,ast,importlib,inspect,math
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from icon_set.model.icons.base import Icon
from icon_set.model.primitives import Arc,Bezier,Line,primitive_from_dict
from icon_set.validation.envelope import arc_geometry
OUT=Path(__file__).resolve().parent
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/human-detection-review/source-models.json'
AUTHOR='gpt-6'
rows=json.loads((ROOT/SOURCE_PATH).read_text())
tree=ast.parse((ROOT/'icon_set/work/human-detection-review/build_preview.py').read_text())
specs=ast.literal_eval(next(n.value for n in tree.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='specs' for t in n.targets)))
# Anatomical classification after a fresh visual pass over all candidates.
# Outlined bodies are not represented by fictitious torso centerlines.
types={11:'outlined-body',15:'outlined-body',34:'mixed-adult-infant',52:'human-faced-animal',60:'group-busts',66:'bust',77:'outlined-body',90:'group-busts',93:'outlined-body',101:'mixed-segmented-body',133:'bust',144:'legs-only',152:'outlined-body',168:'group-busts',169:'group-busts',177:'outlined-body',180:'outlined-body'}
# Jet-ski rider is an outlined hunched body, not a lone stick torso.
specs[77]=[('head',['rider-2','rider-3','rider-4'],None)]
# Bird hunter shoulders are the two top edges; legs/side edges are not torso axes.
specs[15]=[('head',['torso-2','torso-3'],None)]
# Sphinx: human facial anatomy exists, but its animal haunch is not a human torso.
specs[52]=[('face',[],None)]
# Side heads in selection icon are fragments continuous with the bust outline.
# Record connected busts, not three detached head/torso-line pairings.
notes={52:'Human face with animal body: no human torso; excluded from head/torso-line repair.',60:'Central head above shoulder arch; side figures are continuous partial bust outlines. No torso lines.',66:'Face under helmet and separate shoulder arch: bust spacing, not a torso-axis construction.',15:'Head above an angular shoulder/back outline; shoulder edges are torso-2 and torso-3.',11:'Head above a broad shoulder bar and outlined waist. Measure against shoulder bar, not side walls.',77:'Hunched seated body is an outline; no single hip-to-neck stroke can be asserted.',101:'Director vertical stroke includes torso and leg; split at the hip before assigning a torso flag.',144:'Only legs and starting block are drawn; head and torso are absent.'}
def load(x):
 path=x['row']['source_path'];m=importlib.import_module(path[:-3].replace('/','.'))
 return next(c for _,c in inspect.getmembers(m,inspect.isclass) if issubclass(c,Icon) and getattr(c,'icon_id',None)==x['row']['icon_id'])()
def circle(prims):
 if not prims or any(not isinstance(p,Arc) for p in prims):return None
 gs=[arc_geometry(p) for p in prims];g=gs[0]
 if any(abs(z.center_x-g.center_x)+abs(z.center_y-g.center_y)+abs(z.radius_x-g.radius_x)+abs(z.radius_y-g.radius_x)>1e-7 for z in gs):return None
 if abs(sum(abs(z.delta_angle) for z in gs)-math.tau)>1e-6:return None
 return (g.center_x,g.center_y,g.radius_x)
def evaluate(i,fs):
 d=i.draw();by=d.by_id();out=[]
 for f in fs:
  hp=circle([by[z] for z in f['head_members']]);junction=f['torso_junction'];t=by[f['torso_members'][0]] if f['torso_members'] else None
  result=dict(f)
  if hp and junction and t:
   cx,cy,r=hp;q=getattr(t,junction).as_tuple();distance=math.hypot(cx-q[0],cy-q[1]);gap=distance-r-4
   if isinstance(t,Bezier):v=t.segments[0][0] if junction=='start' else t.segments[-1][1]
   elif isinstance(t,Arc):
    g=arc_geometry(t);theta=g.start_angle+(g.delta_angle if junction=='end' else 0);sign=(1 if g.delta_angle>0 else -1)*(1 if junction=='start' else -1);v=(q[0]-sign*g.radius_x*math.sin(theta),q[1]+sign*g.radius_y*math.cos(theta))
   else:v=(t.end if junction=='start' else t.start).as_tuple()
   a=(q[0]-v[0],q[1]-v[1]);b=(cx-q[0],cy-q[1]);den=math.hypot(*a)*math.hypot(*b);ang=math.degrees(math.acos(max(-1,min(1,sum(u*v for u,v in zip(a,b))/den)))) if den else 180
   result.update(head_circle=hp,neck=list(q),ink_gap=gap,axis_error_degrees=ang,needs_repair=abs(gap-4)>1e-6 or ang>1)
  out.append(result)
 return out
if __name__=='__main__':
 audit=[]
 for x in rows:
  i=load(x);d=i.draw();by=d.by_id();cs={c.contour_id:c.members for c in d.contours};n=x['number']
  def expand(ref):return [p for k in ([ref] if isinstance(ref,str) else ref) for p in cs.get(k,[k])]
  fs=[dict(figure_id=f'person-{j+1}',head=h,torso=t,head_members=expand(h),torso_members=expand(t),torso_junction=k) for j,(h,t,k) in enumerate(specs[n])]
  fs=evaluate(i,fs)
  audit.append(dict(number=n,icon_id=i.icon_id,type=types.get(n,'stick-figure'),note=notes.get(n,'Reviewed shoulder, hip, limbs and head as anatomical parts.'),figures=fs,source_path=x['row']['source_path']))
  print(n,i.icon_id,types.get(n,'stick'),[(round(f['ink_gap'],3),round(f['axis_error_degrees'],1)) for f in fs if 'ink_gap' in f],flush=True)
 (OUT/'audit.json').write_text(json.dumps(audit,indent=2))
