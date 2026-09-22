import json
from pathlib import Path
W=Path(__file__).parent
def write(i,icon_id,keyshape,body,doc,category="objects"):
 d=json.loads((W/f"{i:02}-intake.json").read_text());u=d["uuid"];r=d["row"]
 source="pictographic-primitives/"+r["path"]
 text=f"""{doc!r}
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = {u!r}
SOURCE_PATH = {source!r}
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = {icon_id!r}
    keyshape = Keyshape.{keyshape}
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = {category!r}
    aliases = {[r['concept']]!r}
    keywords = {r.get('tags',[])!r}
    def build(self):
"""+body
 p=Path('icon_set/model/icons/solo')/(icon_id.replace('-','_')+'_'+u.replace('-','_')+'.py');p.write_text(text);return p
