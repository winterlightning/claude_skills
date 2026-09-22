import sys,subprocess,json,ast
from pathlib import Path
sys.path.insert(0,str(Path.cwd()))
from icon_set.model.icons.registry import create
from icon_set.validation.library_qa import inspect_icon
W=Path(__file__).parent
for i in map(int,sys.argv[1:]):
 p=Path((W/f'{i:02}-original.txt').read_text())
 tree=ast.parse(p.read_text());cls=next(n for n in tree.body if isinstance(n,ast.ClassDef));name=next(ast.literal_eval(n.value) for n in cls.body if isinstance(n,ast.Assign) and n.targets[0].id=='icon_id')
 r=inspect_icon(create(name));r.pop('_svg',None)
 (W/f'{i:02}-full-qa.json').write_text(json.dumps(r,indent=2,default=str))
 print(i,name,r['status'],r['errors'],r['warnings'],flush=True)
 if r['status']!='pass':continue
 with (W/f'{i:02}-build.log').open('w') as f:
  result=subprocess.run([sys.executable,'-m','icon_set','build','--icon',str(p),'--no-png','--no-report'],stdout=f,stderr=subprocess.STDOUT)
 print(i,'build exit',result.returncode,flush=True)
