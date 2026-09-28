from pathlib import Path
import json,sys,importlib.util,subprocess,shutil
import cairosvg
ROOT=Path(__file__).resolve().parents[4];sys.path.insert(0,str(ROOT))
SOURCE_ICON_ID=None
SOURCE_PATH=None
AUTHOR='gpt-6'
ITEMS=json.loads((Path(__file__).parent/'items.json').read_text())
def check(n):
 item=ITEMS[n-1];run=Path(item['run']);p=next(run.glob('*.py'))
 rounds=run/'attempts';rounds.mkdir(exist_ok=True);k=len(list(rounds.glob('*.py')))+1
 shutil.copy(p,rounds/f'{k:02}.py')
 spec=importlib.util.spec_from_file_location('candidate',p);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
 cls=[v for v in vars(m).values() if isinstance(v,type) and v.__module__=='candidate'][0];icon=cls();r=icon.validate_icon();txt=r.describe();(run/'validation.txt').write_text(txt);(rounds/f'{k:02}-validation.txt').write_text(txt)
 svg=icon.to_svg();(run/(icon.icon_id+'.svg')).write_text(svg)
 for theme,bg,fg in [('light','#ffffff','#111111'),('dark','#15191f','#ffffff')]:
  for size in [48,240]:
   cairosvg.svg2png(bytestring=svg.replace('currentColor',fg).encode(),write_to=str(run/f'{theme}-{size}.png'),output_width=size,output_height=size,background_color=bg)
 proc=subprocess.run([sys.executable,'icon_set/scripts/build_gate.py',str(p),'--debug',str(run/'gate')],capture_output=True,text=True)
 (run/'build-gate.txt').write_text(proc.stdout+proc.stderr);(rounds/f'{k:02}-gate.txt').write_text(proc.stdout+proc.stderr)
 print(f'ICON {n} ROUND {k}\n{txt}\n{proc.stdout}{proc.stderr}',flush=True)
 return proc.returncode==0
if __name__=='__main__':
 for arg in sys.argv[1:]:check(int(arg))
