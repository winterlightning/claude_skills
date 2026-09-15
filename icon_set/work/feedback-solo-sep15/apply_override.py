from pathlib import Path
import json,hashlib,tarfile,io,os,datetime
ROOT=Path(__file__).resolve().parents[3];W=Path(__file__).resolve().parent
SOURCE_ICON_ID=None
SOURCE_PATH='/Users/jakesdev/Downloads/feedback-briefs 2/solo'
AUTHOR='gpt-6'
plan=json.loads((W/'override-plan.json').read_text());contents={}
for row in plan:
 path=ROOT/row['target'];data=path.read_bytes();assert hashlib.sha256(data).hexdigest()==row['before_sha256'],('Changed since preparation',path);contents[row['target']]=data
backup=W/'originals-before-override.tar.gz';assert not backup.exists(),'Backup already exists; do not rerun blindly'
with tarfile.open(backup,'w:gz') as archive:
 for name,data in contents.items():
  info=tarfile.TarInfo(name);info.size=len(data);archive.addfile(info,io.BytesIO(data))
for row in plan:
 target=ROOT/row['target'];data=(W/row['staged']).read_bytes();assert hashlib.sha256(data).hexdigest()==row['after_sha256'];target.write_bytes(data)
 for cached in (target.parent/'__pycache__').glob(target.stem+'.*.pyc'):cached.unlink()
(W/'override-applied.json').write_text(json.dumps({'applied_at':datetime.datetime.now().astimezone().isoformat(),'count':len(plan),'backup':backup.name,'files':plan},indent=2));print('Overwrote',len(plan),'original icon files; original names and IDs preserved.')
