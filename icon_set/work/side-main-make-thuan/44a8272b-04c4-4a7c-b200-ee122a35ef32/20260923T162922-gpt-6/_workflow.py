"""Local, folder-only evidence utilities for this batch."""
from pathlib import Path
import sys, json, subprocess, datetime, shutil, importlib.util, traceback
import cairosvg
from PIL import Image, ImageDraw

SOURCE_ICON_ID = "44a8272b-04c4-4a7c-b200-ee122a35ef32"
SOURCE_PATH = "pictographic-primitives/other/laptop skull_44a8272b-04c4-4a7c-b200-ee122a35ef32.svg"
AUTHOR = "gpt-6"
ROOT = Path.cwd()
sys.path.insert(0, str(ROOT))

def retrieve():
    r = subprocess.run(['python3', 'icon_set/scripts/next_side_main.py', '--offset', '20'], capture_output=True, text=True)
    if r.returncode:
        print(r.stdout + r.stderr); sys.exit(r.returncode)
    f = dict(s.split(': ', 1) for s in r.stdout.splitlines() if ': ' in s and not s.startswith('- '))
    d = ROOT / 'icon_set/work/side-main-make-thuan' / f['source UUID'] / datetime.datetime.now().strftime('%Y%m%dT%H%M%S-gpt-6')
    d.mkdir(parents=True, exist_ok=False)
    m = {k: f.get(v) for k,v in [('concept','concept'), ('source_uuid','source UUID'), ('reference_path','reference'), ('category','category'), ('aliases','aliases'), ('uses','uses')]}
    m.update(combination_context=[s for s in r.stdout.splitlines() if s.startswith('- ')], retrieval_stdout=r.stdout, retrieval_stderr=r.stderr)
    (d/'retrieval.metadata.json').write_text(json.dumps(m, indent=2))
    shutil.copyfile(f['reference'], d/'reference.svg')
    for size in (48,384):
        cairosvg.svg2png(url=f['reference'], write_to=str(d/f'reference-{size}.png'), output_width=size, output_height=size, background_color='white')
    print(r.stdout); print('RESULT_DIR: '+str(d))
    matches = subprocess.run(['rg','-l', '-e', f['source UUID'], '-e', f['source UUID'].replace('-','_'), 'icon_set/model/icons'], capture_output=True, text=True)
    print('Existing source matches: '+(matches.stdout or 'none'))

def author(d):
    m=json.loads((d/'retrieval.metadata.json').read_text())
    p=json.loads((d/'design.json').read_text())
    filename=p['icon_id'].replace('-','_')+'_'+m['source_uuid'].replace('-','_')+'.py'
    code='from icon_set.model.keyshapes import Keyshape\nfrom icon_set.model.icons.solo._base import Solo48\n\n'
    code+=f'SOURCE_ICON_ID = {m["source_uuid"]!r}\nSOURCE_PATH = {m["reference_path"]!r}\nAUTHOR = {AUTHOR!r}\n\n'
    code+='class Drawing(Solo48):\n'
    code+=f'    """{p["subject"]}\n\n    Plan: {p["plan"]}\n    References: {p["references"]}\n    """\n'
    code+=f'    icon_id = {p["icon_id"]!r}\n    keyshape = Keyshape.{p["keyshape"]}\n    semantic_role = "MAIN"\n    semantic_kind = "noun"\n    category = {p.get("category","objects/other")!r}\n    aliases = ()\n    keywords = {tuple(p.get("keywords",[]))!r}\n\n    def build(self):\n'
    code+='\n'.join('        '+s for s in p['code'].splitlines())+'\n'
    (d/filename).write_text(code)
    (d/(p['icon_id']+'.metadata.json')).write_text(json.dumps(m,indent=2))
    spec=importlib.util.spec_from_file_location('authored',d/filename); mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
    icon=mod.Drawing()
    try:
        report=icon.validate_icon(); desc=report.describe(); status=report.status
    except Exception:
        desc=traceback.format_exc();status='error'
    (d/'validation.txt').write_text(desc)
    (d/'validation-status.json').write_text(json.dumps({'status':status}))
    print(desc)
    try:
        svg=icon.to_svg();(d/(p['icon_id']+'.svg')).write_text(svg)
        # Render unchanged model SVG; use CSS currentColor through CairoSVG's color setting.
        for theme,bg,fg in [('light','#ffffff','#111111'),('dark','#15191f','#ffffff')]:
            for size in (48,384):
                cairosvg.svg2png(bytestring=svg.encode(),write_to=str(d/f'{theme}-{size}.png'),output_width=size,output_height=size,background_color=bg,color=fg)
    except TypeError:
        # CairoSVG supports currentColor via a surrounding SVG context; geometry remains untouched.
        for theme,bg,fg in [('light','#ffffff','#111111'),('dark','#15191f','#ffffff')]:
            wrapper=f'<svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 48 48" color="{fg}">{svg}</svg>'
            for size in (48,384):
                cairosvg.svg2png(bytestring=wrapper.encode(),write_to=str(d/f'{theme}-{size}.png'),output_width=size,output_height=size,background_color=bg)
    except Exception:
        (d/'render-error.txt').write_text(traceback.format_exc())
        print(traceback.format_exc())
    sheet=Image.new('RGB',(864,432),'#dddddd')
    for x,t in [(0,'light'),(432,'dark')]:
        for size,y in [(384,0),(48,384)]:
            if (d/f'{t}-{size}.png').exists(): sheet.paste(Image.open(d/f'{t}-{size}.png'),(x,y))
    sheet.save(d/'review.png')

def finish(d):
    m=json.loads((d/'retrieval.metadata.json').read_text()); p=json.loads((d/'design.json').read_text())
    result=dict(source_uuid=m['source_uuid'],source_path=m['reference_path'],icon_id=p['icon_id'],author=AUTHOR,keyshape=p['keyshape'],keyshape_reason=p['keyshape_reason'],validation_status=json.loads((d/'validation-status.json').read_text())['status'],visual_review=(d/'visual-review.txt').read_text(),omissions=p.get('omissions',[]),references=p['references'],artifacts=sorted(x.name for x in d.iterdir() if x.is_file()))
    (d/'result.json').write_text(json.dumps(result,indent=2))
    print(p['icon_id']+': '+result['validation_status'])

if __name__=='__main__':
    if sys.argv[1]=='retrieve': retrieve()
    else: {'author':author,'finish':finish}[sys.argv[1]](Path(sys.argv[2]))
