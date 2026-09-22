import json
from pathlib import Path
W=Path(__file__).parent
ROOT=Path.cwd()
def write(i,name,key,plan,body):
 d=json.loads((W/f'{i:02}-intake.json').read_text());u=d['uuid'];r=d['row'];source='pictographic-primitives/'+r['path']
 doc=plan+'\n\nEditorial reference brief:\n'+d['brief']['brief']
 s=repr(doc)+'\nfrom ._base import Solo48\nfrom ...keyshapes import Keyshape\n\n'
 s+=f'SOURCE_ICON_ID = {u!r}\nSOURCE_PATH = {source!r}\nAUTHOR = "gpt-6-astra"\n\nclass Drawing(Solo48):\n'
 s+=f'    icon_id = {name!r}\n    keyshape = Keyshape.{key}\n    semantic_role = "MAIN"\n    semantic_kind = "noun"\n    category = {r.get("category","Uncategorized")!r}\n    aliases = [{r.get("concept",name)!r}]\n    keywords = {r.get("tags") or name.split("-")!r}\n\n    def build(self):\n'
 s+='\n'.join('        '+line if line else '' for line in body.splitlines())+'\n'
 path=ROOT/'icon_set/model/icons/solo'/f'{name.replace("-","_")}_{u.replace("-","_")}.py';path.write_text(s)
 (W/f'{i:02}-original.txt').write_text(str(path));print(path)
