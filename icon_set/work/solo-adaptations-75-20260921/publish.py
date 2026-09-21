"""Install only inspected, passing SOLO48 candidates and build those files."""
import hashlib,json,pathlib,subprocess,sys
ROOT=pathlib.Path(__file__).resolve().parents[3]
WORK=pathlib.Path(__file__).parent
rows=json.loads((WORK/'validation.json').read_text())
qas={x['number']:x['qa'] for x in json.loads((WORK/'full-qa.json').read_text())}
installed=[]
for row in rows:
 qa=qas.get(row['number'],{})
 if row['status']!='valid' or qa.get('status')!='pass':continue
 assert not qa['errors'] and not qa['warnings']
 assert hashlib.sha256((WORK/'previews'/f"{row['number']}.svg").read_bytes()).hexdigest()==qa['svg_sha256']
 source=pathlib.Path(row['candidate']);dest=ROOT/'icon_set/model/icons/solo'/source.name
 if dest.exists():assert dest.read_bytes()==source.read_bytes(),f'Existing file differs: {dest}'
 else:
  with dest.open('xb') as f:f.write(source.read_bytes())
 installed.append({**row,'model_path':str(dest),'model_sha256':hashlib.sha256(dest.read_bytes()).hexdigest()})
(WORK/'installed.json').write_text(json.dumps(installed,indent=2)+'\n')
args=['rtk','proxy',sys.executable,'-m','icon_set','build','--no-png','--no-report']
for row in installed:args += ['--icon',row['model_path']]
with (WORK/'build.log').open('w') as log:
 result=subprocess.run(args,cwd=ROOT,stdout=log,stderr=subprocess.STDOUT)
print(f'Installed {len(installed)} solo modules; targeted build exit {result.returncode}.')
print((WORK/'build.log').read_text()[-6000:])
raise SystemExit(result.returncode)
