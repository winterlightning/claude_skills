from pathlib import Path
import sys,ast,json,inspect,re,textwrap,hashlib
ROOT=Path(__file__).resolve().parent/'snapshot';sys.path.insert(0,str(ROOT))
from icon_set.scripts.create_variant import prepare_variant
from icon_set.model.icons.registry import factories
SOURCE_ICON_ID=None
SOURCE_PATH='/Users/jakesdev/Downloads/feedback-briefs 2/solo'
AUTHOR='gpt-6'
W=Path(__file__).parent
rows=json.loads((W/'inventory.json').read_text());by={r['number']:r for r in rows}
records=json.loads((W/'revisions.json').read_text()) if (W/'revisions.json').exists() else {}
HELP='''
def path(n,start,commands,closed=False):
    here=start;members=[]
    for i,c in enumerate(commands):
        kind,end,*args=c;name=f'{n}-{i}'
        if kind=='L':self.add_line(name,here,end)
        elif kind=='A':self.add_arc(name,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
        elif kind=='C':self.add_bezier(name,here,(args[0],args[1],end))
        members.append(name);here=end
    self.add_contour(n,*members,closed=closed)
def oval(n,x,y,rx,ry):
    path(n,(x-rx,y),[('A',(x+rx,y),rx,ry,True),('A',(x-rx,y),rx,ry,True)],True)
def box(n,l,t,r,b,rad=4):
    path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
line=self.add_line
poly=self.add_polyline
dot=self.add_dot
join=lambda a,b:self.relate('connect',a,b)
'''
def revise(nums,note,body=None,patch=None,keyshape=None,ref=None):
    if isinstance(nums,int):nums=[nums]
    r=by[nums[0]];fac=factories()[r['parent']]
    record=records.get(str(nums[0]))
    if record and any(v['id']==record['id'] and int(k) not in nums and int(k)<nums[0] for k,v in records.items()):record=None
    if record:
        dest=ROOT/record['file'];ident=record['id'];tree=ast.parse(dest.read_text())
    else:
        import importlib
        import icon_set.model.icons.registry as registry
        importlib.invalidate_caches();registry._FACTORIES=None
        dest,ident,source=prepare_variant(r['parent'],'solo',note);tree=ast.parse(source)
        module=sys.modules[fac.__module__];sid=getattr(module,'SOURCE_ICON_ID',None)
        if sid:dest=dest.with_name(dest.stem+'_'+sid.replace('-','_')+'.py')
    cls=next(n for n in tree.body if isinstance(n,ast.ClassDef) and n.name!=fac.__name__ and any(isinstance(v,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='icon_id' for t in v.targets) for v in n.body))
    # Re-evaluate a patch from the preserved parent so reruns never compound changes.
    if patch:
        src=ast.unparse(ast.parse(textwrap.dedent(inspect.getsource(fac.build))));newsrc=patch(src);fn=ast.parse(newsrc).body[0]
    elif body:
        fn=ast.parse('def build(self):\n'+textwrap.indent(HELP+'\n'+textwrap.dedent(body),'    ')).body[0]
    else:raise ValueError('Missing edit')
    fn.body.insert(0,ast.Expr(value=ast.Constant(value='Symbol plan: '+note+' Reference: '+(ref or 'inspected current parent; no useful exact Lucide match selected')+'.')))
    cls.body=[n for n in cls.body if not(isinstance(n,ast.FunctionDef) and n.name=='build')]+[fn]
    if keyshape:
        for n in cls.body:
            if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='keyshape' for t in n.targets):n.value=ast.parse('Keyshape.'+keyshape,mode='eval').body
    tree.body=[n for n in tree.body if not(isinstance(n,ast.Expr) and isinstance(n.value,ast.Constant) and isinstance(n.value.value,str))]
    for n in tree.body:
        if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='AUTHOR' for t in n.targets):n.value=ast.Constant(AUTHOR)
    tree.body.insert(0,ast.Expr(value=ast.Constant(value=note+' Independent feedback revision; parent preserved.')))
    ast.fix_missing_locations(tree);dest.write_text(ast.unparse(tree)+'\n')
    for num in nums:records[str(num)]={'id':ident,'file':str(dest.relative_to(ROOT)),'parent':r['parent'],'note':note,'reference':ref or 'Current parent; no useful exact Lucide match','brief_numbers':nums}
    (W/'revisions.json').write_text(json.dumps(records,indent=2))
def remove_named(src,names):
    tree=ast.parse(src)
    class Remover(ast.NodeTransformer):
        def visit_Expr(self,node):
            if isinstance(node.value,ast.Call) and any(isinstance(a,ast.Constant) and a.value in names for a in node.value.args):return None
            return node
    return ast.unparse(Remover().visit(tree))

def run():
    revise(9,'Remove both cuff divider lines; retain the single crown-to-cuff division.',patch=lambda s:remove_named(s,{'panel-left','panel-right'}))
    revise(10,'Remove both internal crown seams.',patch=lambda s:remove_named(s,{'left-seam','right-seam'}))
    revise(19,'Replace the circular hub with one centered dot.',patch=lambda s:s.replace("circle('hub', 24, 24, 3)","self.add_dot('hub', (24,24))"),ref='Lucide disc: concentric rim and hub')
    revise(29,'Remove the central fan rib; keep the mirrored pair of remaining ribs.',patch=lambda s:remove_named(s,{'centre-rib'})+"\n    self.relate('connect','rib-left','rib-right')\n")
    revise(88,'Remove the middle lower leg while preserving the two outer legs.',patch=lambda s:s.replace('(14, 26, 38)','(14, 38)'))
    revise([176,195],'Add two dot eyes, mirrored around the face center.',patch=lambda s:s+"\n    self.add_dot('eye-left',(18,25))\n    self.add_dot('eye-right',(30,25))\n",ref='Lucide cat: paired eyes inside an open face')
    revise(181,'Align both dot eyes below the sweat drop.',patch=lambda s:s.replace('(17,21)','(16,25)').replace('(27,23)','(26,25)'))
    revise(186,'Remove the internal feather rib, leaving three outer feather curves and an empty feather fan.',patch=lambda s:remove_named(s,{'feather-rib'}))
    revise(193,'Replace the hub ring with a dot at the exact disc center (24,21).',patch=lambda s:s.replace("self.circle('hub',24,18,3)","self.add_dot('hub',(24,21))"),ref='Lucide disc: shared center for rim and hub')
    revise(196,'Dot-lens alternative: replace the small lens circle with a dot.',patch=lambda s:s.replace("circle('lens',29,18,3)","self.add_dot('lens',(29,18))"),ref='Lucide disc: centered dot')
    revise(199,'Large-lens alternative: enlarge and center the circular lens; remove the adjacent screen mark to keep clearance.',patch=lambda s:remove_named(s.replace("circle('lens',29,18,3)","circle('lens',24,18,4)"),{'screen'}),ref='Lucide disc: concentric circular geometry')
    for n in [201,202]:
        revise(n,'Replace the pointed lower jaw with a true horizontal oval while retaining the eye style.',patch=lambda s:s.replace("self.add_arc('jaw-right',(44,22),(24,40),radius_x=22)","self.add_arc('jaw-right',(44,24),(24,40),radius_x=20,radius_y=16)").replace("self.add_arc('jaw-left',(24,40),(4,22),radius_x=22)","self.add_arc('jaw-left',(24,40),(4,24),radius_x=20,radius_y=16)").replace("self.add_arc('crown',(4,22),(44,22),radius_x=20,radius_y=14)","self.add_arc('crown',(4,24),(44,24),radius_x=20,radius_y=16)") if n==201 else s.replace("(4,22), (44,22), radius_x=20, radius_y=14","(4,24), (44,24), radius_x=20, radius_y=16").replace("(44,22), (24,40), radius_x=22","(44,24), (24,40), radius_x=20,radius_y=16").replace("(24,40), (4,22), radius_x=22","(24,40), (4,24), radius_x=20,radius_y=16"))
    revise(130,'Add a centered oval nose inside the seal silhouette.',patch=lambda s:s+"\n    self.add_arc('nose-top',(18,22),(30,22),radius_x=6,radius_y=4)\n    self.add_arc('nose-bottom',(30,22),(18,22),radius_x=6,radius_y=4)\n    self.add_contour('nose','nose-top','nose-bottom',closed=True)\n")
    revise([150,163,164],'Widen both rectangular straps equally from 16 to 24 units, keeping the dial centered.',patch=lambda s:s.replace('(16,12),(16,4),(32,4),(32,12)','(12,12),(12,4),(36,4),(36,12)').replace('(16,36),(16,44),(32,44),(32,36)','(12,36),(12,44),(36,44),(36,36)'))
    revise(160,'Add two evenly spaced dot eyes to the baby face.',patch=lambda s:s+"\n    self.add_dot('eye-left',(18,26))\n    self.add_dot('eye-right',(30,26))\n",ref='Lucide baby: paired dot eyes; shared human reference for face proportions')
    revise(167,'Center the result window within the diagonal body, preserving its shared diagonal angle.',patch=lambda s:s.replace('(23,21)','(24,18)').replace('(25,19)','(26,16)').replace('(31,25)','(32,22)').replace('(29,27)','(30,24)').replace('(26,30)','(27,27)').replace('(23,33)','(24,30)').replace('(21,35)','(22,32)').replace('(15,29)','(16,26)').replace('(17,27)','(18,24)').replace('(20,24)','(21,21)'))
if __name__=='__main__':run()
