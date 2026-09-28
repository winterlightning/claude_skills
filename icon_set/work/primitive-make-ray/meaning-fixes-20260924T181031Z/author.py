from pathlib import Path
import json, textwrap, sys, re
ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT))
from icon_set.scripts.primitive_fix import load_icon, render_previews
from icon_set.scripts.build_gate import gate
import cairosvg
SOURCE_ICON_ID = None
SOURCE_PATH = None
AUTHOR = 'gpt-6'
BATCH = Path(__file__).parent
STAMP = '20260924T181031Z'

HELPERS = '''
    def path(self, name, start, steps, closed=False):
        current = start
        ids = []
        for index, step in enumerate(steps):
            ident = f"{name}-{index}"
            if len(step) == 2:
                self.add_line(ident, current, step)
                current = step
            else:
                end, rx, ry, sweep = step
                self.add_arc(ident, current, end, radius_x=rx, radius_y=ry, sweep=sweep)
                current = end
            ids.append(ident)
        self.add_contour(name, *ids, closed=closed)

    def circle(self, name, cx, cy, r):
        self.path(name, (cx-r,cy), [((cx+r,cy),r,r,True),((cx-r,cy),r,r,True)], True)

    def box(self, name, x, y, w, h, r=3):
        self.path(name,(x+r,y),[(x+w-r,y),((x+w,y+r),r,r,True),(x+w,y+h-r),
            ((x+w-r,y+h),r,r,True),(x+r,y+h),((x,y+h-r),r,r,True),(x,y+r),((x+r,y),r,r,True)],True)
'''

def create(icon_id, keyshape, body, note, refs='', omissions='', category='objects/general'):
    if len(sys.argv)>1 and icon_id not in sys.argv[1:]: return
    claim = ROOT / 'icon_set/work/primitive-fix-thuan' / ('solo__'+icon_id) / (STAMP+'-thuan-mac')
    reference = next((claim/'reference').glob('*.svg')).relative_to(ROOT)
    match = re.search(r'([0-9a-f-]{36})$', reference.stem)
    uuid = match.group(1)
    concept = reference.stem[:match.start()].rstrip('_')
    run = ROOT/'icon_set/work/primitive-make-ray'/uuid/(STAMP+'-meaning-'+icon_id)
    run.mkdir(exist_ok=True, parents=True)
    meta = dict(concept=concept, source_uuid=uuid, reference_path=str(reference))
    (run/(icon_id+'.metadata.json')).write_text(json.dumps(meta,indent=2)+'\n')
    for size in (48,384):
        cairosvg.svg2png(url=str(ROOT/reference),write_to=str(run/f'reference-{size}.png'),output_width=size,output_height=size,background_color='white')
    source = f'''from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = {uuid!r}
SOURCE_PATH = {str(reference)!r}
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = {icon_id!r}
    keyshape = Keyshape.{keyshape}
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = {category!r}
    aliases = ()
    keywords = ({concept!r},)
    # Plan: {note}
    # Construction references: {refs or 'No useful subject match; original reference silhouette.'}
    # Omissions: {omissions or 'None.'}
    def build(self):
'''+textwrap.indent(textwrap.dedent(body).strip()+'\n','        ')+HELPERS
    module = run/(icon_id.replace('-','_')+'_'+uuid.replace('-','_')+'.py')
    module.write_text(source)
    icon=load_icon(module)
    report=icon.validate_icon()
    svg=icon.to_svg()
    (run/(icon_id+'.svg')).write_text(svg)
    previews=render_previews(svg,icon_id,48,run)
    g=gate(module)
    (run/'validation.txt').write_text(report.describe()+'\n'+json.dumps(g,indent=2)+'\n')
    result=dict(**meta,icon_id=icon_id,author=AUTHOR,validation_status=report.status,build_gate=g,
                keyshape=keyshape,visual_review='Pending visual inspection',description=note,
                construction_references=refs,omissions=omissions,artifacts=[module.name,icon_id+'.svg',*previews])
    (run/'candidate.json').write_text(json.dumps(result,indent=2)+'\n')
    print(icon_id,report.status,g['status'],flush=True)
    for message in list(report.errors)+list(report.warnings)+g['errors']+g['warnings']: print(' ',message,flush=True)
    return run

if __name__=='__main__':
    exec((BATCH/'designs.py').read_text())
