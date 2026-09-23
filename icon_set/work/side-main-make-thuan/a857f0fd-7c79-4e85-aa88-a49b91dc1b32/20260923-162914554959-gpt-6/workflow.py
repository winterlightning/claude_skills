"""Folder-only authoring and evidence helpers for this invocation."""
SOURCE_ICON_ID = 'a857f0fd-7c79-4e85-aa88-a49b91dc1b32'
SOURCE_PATH = 'pictographic-primitives/other/computer_a857f0fd-7c79-4e85-aa88-a49b91dc1b32.svg'
AUTHOR = 'gpt-6'

import datetime, importlib.util, json, pathlib, re, subprocess, textwrap, traceback
import cairosvg
from PIL import Image, ImageDraw

ROOT = pathlib.Path.cwd()
BASE = pathlib.Path(__file__).parent

def retrieve():
    p = subprocess.run(['python3', 'icon_set/scripts/next_side_main.py', '--offset', '10'], capture_output=True, text=True)
    if p.returncode:
        print(p.stdout, p.stderr); return None
    d = {}; contexts = []
    for line in p.stdout.splitlines():
        if line.startswith('- '): contexts.append(line)
        elif ': ' in line:
            k, v = line.split(': ', 1); d[k] = v
    uid = d['source UUID']; slug = re.sub('[^a-z0-9]+', '-', d['concept'].lower()).strip('-')
    out = ROOT / 'icon_set/work/side-main-make-thuan' / uid / ('20260923-' + datetime.datetime.now().strftime('%H%M%S%f') + '-gpt-6')
    out.mkdir(parents=True)
    m = dict(concept=d['concept'], source_uuid=uid, reference_path=d['reference'], category=d['category'], aliases=d['aliases'], uses=d['uses'], combination_context=contexts, retrieval_stdout=p.stdout, retrieval_stderr=p.stderr, icon_id=slug)
    (out / (slug + '.metadata.json')).write_text(json.dumps(m, indent=2)+'\n')
    (out / 'retrieval.txt').write_text(p.stdout)
    cairosvg.svg2png(url=str(ROOT/d['reference']), write_to=str(out/'reference.png'), output_width=384, output_height=384, background_color='white')
    print(p.stdout); print('RESULT_DIR:', out)
    return out

def metadata(out):
    return json.loads(next(pathlib.Path(out).glob('*.metadata.json')).read_text())

def author(out, keyshape, body, plan):
    out = pathlib.Path(out); m = metadata(out)
    name = m['icon_id'].replace('-', '_') + '_' + m['source_uuid'].replace('-', '_')
    source = f'''"""{m['concept']}.\n\nSymbol plan: {plan}\n"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = {m['source_uuid']!r}
SOURCE_PATH = {m['reference_path']!r}
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = {m['icon_id']!r}
    keyshape = Keyshape.{keyshape}
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = {m['category']!r}
    aliases = ()
    keywords = {tuple(m['concept'].lower().split())!r}

    def circle(self, name, x, y, r):
        self.add_arc(name+'-a', (x-r,y), (x+r,y), radius_x=r)
        self.add_arc(name+'-b', (x+r,y), (x-r,y), radius_x=r)
        self.add_contour(name, name+'-a', name+'-b', closed=True)

    def rounded_box(self, name, left, top, right, bottom, r):
        self.add_line(name+'-top', (left+r,top), (right-r,top))
        self.add_arc(name+'-tr', (right-r,top), (right,top+r), radius_x=r)
        self.add_line(name+'-right', (right,top+r), (right,bottom-r))
        self.add_arc(name+'-br', (right,bottom-r), (right-r,bottom), radius_x=r)
        self.add_line(name+'-bottom', (right-r,bottom), (left+r,bottom))
        self.add_arc(name+'-bl', (left+r,bottom), (left,bottom-r), radius_x=r)
        self.add_line(name+'-left', (left,bottom-r), (left,top+r))
        self.add_arc(name+'-tl', (left,top+r), (left+r,top), radius_x=r)
        self.add_contour(name, *(name+'-'+part for part in ('top','tr','right','br','bottom','bl','left','tl')), closed=True)

    def build(self):
'''+textwrap.indent(textwrap.dedent(body).strip()+'\n', '        ')
    (out/(name+'.py')).write_text(source)
    print(out/(name+'.py'))

def export(out):
    out = pathlib.Path(out); m = metadata(out)
    path = next(p for p in out.glob('*.py') if p.name!='workflow.py')
    spec = importlib.util.spec_from_file_location('candidate',path); module = importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
    try:
        icon = module.Drawing(); report = icon.validate_icon()
        (out/'validation.txt').write_text(report.describe()+'\n')
        svg = icon.to_svg(); (out/(m['icon_id']+'.svg')).write_text(svg)
        for theme,ink,bg in [('light','#111111','#ffffff'),('dark','#eeeeee','#171717')]:
            document = svg.replace('fill="none"', f'color="{ink}" fill="none"', 1)
            for size in (48,384):
                cairosvg.svg2png(bytestring=document.encode(), write_to=str(out/f'{theme}-{size}.png'), output_width=size, output_height=size, background_color=bg)
        panel = Image.new('RGB',(864,460),'#aaaaaa')
        for i,theme in enumerate(('light','dark')):
            panel.paste(Image.open(out/f'{theme}-384.png'),(i*432,0))
            panel.paste(Image.open(out/f'{theme}-48.png'),(i*432+168,400))
        panel.save(out/'review.png')
        print(report.describe())
        return report.status
    except Exception:
        (out/'error.txt').write_text(traceback.format_exc()); print(traceback.format_exc()); return 'error'

def finish(out, findings, omissions, references, rationale):
    out=pathlib.Path(out); m=metadata(out)
    v=(out/'validation.txt').read_text() if (out/'validation.txt').exists() else 'error'
    path=next(p for p in out.glob('*.py') if p.name!='workflow.py')
    spec=importlib.util.spec_from_file_location('candidate',path); mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    try: status=mod.Drawing().validate_icon().status
    except Exception: status='error'
    result=dict(source_uuid=m['source_uuid'],source_path=m['reference_path'],icon_id=m['icon_id'],author=AUTHOR,keyshape=mod.Drawing.keyshape.name,keyshape_rationale=rationale,validation_status=status,visual_review=findings,omissions=omissions,references=references,artifacts=sorted(p.name for p in out.iterdir() if p.is_file()))
    (out/'result.json').write_text(json.dumps(result,indent=2)+'\n')
    print('SAVED',m['icon_id'],status)

def lucide(out, name):
    out=pathlib.Path(out)
    p=subprocess.run(['python3','icon_set/scripts/lucide_reference.py','atoms',name],capture_output=True,text=True)
    (out/('lucide-'+name+'-atoms.txt')).write_text(p.stdout+p.stderr)
    print(p.stdout+p.stderr)
    cairosvg.svg2png(url=str(ROOT/'icon_set/references/lucide/original'/f'{name}.svg'),write_to=str(out/('lucide-'+name+'.png')),output_width=384,output_height=384,background_color='white')
