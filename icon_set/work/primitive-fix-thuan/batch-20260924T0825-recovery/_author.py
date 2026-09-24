from pathlib import Path
import json,textwrap
AUTHOR='gpt-6'
ROOT=Path(__file__).parent
ROWS=json.loads((ROOT/'inputs.json').read_text())
SOURCE_ICON_ID={r['icon_id']:r['source_uuid'] for r in ROWS}
SOURCE_PATH={r['icon_id']:r['reference_path'] for r in ROWS}
HELPERS='''
    def path(self, name, start, commands, closed=False):
        members=[]
        for i,(kind,end,*args) in enumerate(commands):
            n=f'{name}-{i}'
            if kind=='L': self.add_line(n,start,end)
            elif kind=='A': self.add_arc(n,start,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
            elif kind=='C': self.add_bezier(n,start,(args[0],args[1],end))
            members.append(n);start=end
        self.add_contour(name,*members,closed=closed)
    def oval(self,n,x,y,rx,ry):
        self.path(n,(x-rx,y),[('A',(x+rx,y),rx,ry,True),('A',(x-rx,y),rx,ry,True)],True)
    def mirror(self,n,start,commands,closed=True):
        axis=24
        m=lambda p:(2*axis-p[0],p[1])
        nodes=[start]+[c[1] for c in commands]
        rev=[]
        for i,c in reversed(list(enumerate(commands))):
            k,end,*args=c
            if k=='C':rev.append((k,m(nodes[i]),m(args[1]),m(args[0])))
            elif k=='A':rev.append((k,m(nodes[i]),*args))
            else:rev.append((k,m(nodes[i])))
        self.path(n,start,commands+rev,closed)
'''
D={}
def design(i,key,plan,body,ref="No useful exact Lucide match.",omit="None."):
 D[i]=(key,plan,body,ref,omit)
def write(indices=None):
 for i,(key,plan,body,ref,omit) in D.items():
  if indices is not None and i not in indices:continue
  r=ROWS[i]
  code=f'"""{plan}\nConstruction: {ref}\nOmissions: {omit}\n"""\nfrom icon_set.model.keyshapes import Keyshape\nfrom icon_set.model.icons.solo._base import Solo48\nSOURCE_ICON_ID = {r["source_uuid"]!r}\nSOURCE_PATH = {r["reference_path"]!r}\nAUTHOR = {AUTHOR!r}\n\nclass Drawing(Solo48):\n    icon_id = {r["icon_id"]!r}\n    keyshape = Keyshape.{key}\n    semantic_role = "MAIN"\n    semantic_kind = "noun"\n    category = "objects"\n    aliases = ()\n    keywords = {tuple(r["concept"].split())!r}\n\n    def build(self):\n        # Symbol plan: {plan}\n        p=self.path; oval=self.oval; line=self.add_line; poly=self.add_polyline; dot=self.add_dot\n        join=lambda a,b:self.relate("connect",a,b)\n'+textwrap.indent(textwrap.dedent(body).strip(),'        ')+'\n'+HELPERS
  target=Path(r['module'])
  if target.exists() and target.read_text()!=code:
   import shutil
   history=Path(r['run'])/'attempts';history.mkdir(exist_ok=True)
   snap=history/str(len(list(history.iterdir()))+1);snap.mkdir()
   shutil.copyfile(target,snap/'model.py')
   for name in ('validation.txt',r['icon_id']+'.svg'):
    old=Path(r['run'])/name
    if old.exists():shutil.copyfile(old,snap/name)
  target.write_text(code)
  (Path(r['run'])/'design.json').write_text(json.dumps({'keyshape':key,'plan':plan,'construction_reference':ref,'omissions':omit},indent=2))
