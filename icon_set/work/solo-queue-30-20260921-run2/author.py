import json,re
from pathlib import Path
W=Path(__file__).parent

def author(n,ident,key,plan,body,existing=None):
 x=json.loads((W/f'{n:02}-current.json').read_text());u=x['uuid'];brief=x['brief']['brief'];source=re.search(r'- source: `([^`]+)`',brief)[1];tags=re.search(r'- tags: (.*)',brief)[1].split(', ')
 p=Path(existing) if existing else Path('icon_set/model/icons/solo')/(ident.replace('-','_')+'_'+u.replace('-','_')+'.py')
 header=f'"""{plan}"""\nfrom ...keyshapes import Keyshape\nfrom ._base import Solo48\nSOURCE_ICON_ID = {u!r}\nSOURCE_PATH = {source!r}\nAUTHOR = "gpt-6"\nclass Drawing(Solo48):\n    icon_id = {ident!r}\n    keyshape = Keyshape.{key}\n    semantic_role = "MAIN"\n    semantic_kind = "noun"\n    category = "Uncategorized"\n    aliases = ({brief.splitlines()[0][2:]!r},)\n    keywords = {tuple(tags)!r}\n    def build(self):\n'
 p.write_text(header+(W/'helpers.txt').read_text()+body);print(p)
