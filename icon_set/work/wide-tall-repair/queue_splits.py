from pathlib import Path
import sys,json,importlib,subprocess
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from icon_set.model.icons.registry import create
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/wide-tall-repair/targets.json'
AUTHOR='gpt-6'
W=Path(__file__).parent
entries=[('left-double-click-mouse','side','Computer mouse','solo','Left double-click arcs','sub'),('right-double-click-mouse','side','Computer mouse','solo','Right double-click arcs','sub'),('monitor-download-arrow','container','Desktop monitor frame','container','Down arrow','sub'),('monitor-upload-arrow','container','Desktop monitor frame','container','Up arrow','sub'),('monitor-in-security-shield','container','Security shield outline','container','Desktop monitor glyph','sub'),('knight-helm-on-shield','container','Heraldic shield outline','container','Knight helmet glyph','sub'),('open-locket-with-portrait','container','Open oval locket frame','container','Portrait bust','sub')]
results=[]
for id,kind,a,af,b,bf in entries:
 m=importlib.import_module(type(create(id)).__module__)
 x={'reference_path':m.SOURCE_PATH,'source_icon_id':m.SOURCE_ICON_ID,'reviewed_icon':id,'combination_type':kind,'reason':f'The inspected reference combines an independently meaningful {a.lower()} with a separate {b.lower()}.','components':[{'name':a,'family':af,'description':f'Draw the {a.lower()} alone, excluding the {b.lower()} in the full reference.'},{'name':b,'family':bf,'description':f'Draw only the {b.lower()}, excluding the {a.lower()} in the full reference.'}]}
 f=W/'splits'/f'{id}.json';f.parent.mkdir(exist_ok=True);f.write_text(json.dumps(x,indent=2));p=subprocess.run([sys.executable,'icon_set/scripts/queue_brief.py','--file',str(f)],capture_output=True,text=True);results.append({'original':id,'file':str(f),'exit_code':p.returncode,'output':p.stdout+p.stderr});print(id,p.returncode,flush=True)
(W/'splits.json').write_text(json.dumps(results,indent=2))
