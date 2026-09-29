"""Export inspected primitive-make-ray drawings with exact-SVG visual exceptions."""
from pathlib import Path
import sys,json,hashlib
ROOT=Path(__file__).resolve().parents[4]
sys.path.insert(0,str(ROOT))
from icon_set.scripts.primitive_fix import load_icon,run_module,render_previews
from icon_set.scripts.build_gate import gate
import cairosvg
from PIL import Image,ImageDraw

AUTHOR='gpt-6'
SOURCE_ICON_ID='per-input: retained in module and metadata'
SOURCE_PATH='per-input: retained in module and metadata'
BATCH=Path(__file__).parent
REASONS={
 'low-crescent-with-two-sparkles':'User authorized visual exceptions for UI quality. The two diamond sparkles retain visible open centers and distinct silhouettes at 48px. Their 3.07px internal opening and approximately 2–3px local gaps preserve the two-star crescent composition. All strokes remain 4px; inspected in both themes. Diamond sides intentionally replace deeply concave sides that closed the small sparkle hole.',
 'refresh-token-loop':'User authorized visual exceptions for UI quality. Concentric loops retain a uniform 3px ink gap, and the detached token has approximately 3px clearance. This preserves the original two open loops and a separate round token without a misleading contact. Readable in both themes at 48px; all strokes 4px.',
 'running-track-curve-arrow':'User authorized visual exceptions for UI quality. Two concentric lanes retain an analytical 4px ink gap (sampled curve warning); the open arrowhead retains 3px clearance from the horizontal lanes. Native light/dark review confirms a clear arrow, visible shaft and smooth track. All strokes 4px.',
 'saving-bull':'User authorized visual exceptions for UI quality. Integrated outlined legs and lowered head retain their natural narrow channels, approximately 1.1–3px, preserving the left-facing bull silhouette and planted legs. Openings remain visible at 48px in both themes. The trend arrow shares a real body endpoint; all strokes 4px and no false connections.',
}

def main():
    runs=[Path(x) for x in json.loads((BATCH/'runs.json').read_text())]
    sheet=Image.new('RGB',(1000,len(runs)*244),'#ededeb');d=ImageDraw.Draw(sheet)
    records=[]
    for i,p in enumerate(runs):
        mod=run_module(p);icon=load_icon(mod);svg=icon.to_svg()
        if icon.icon_id in REASONS and icon.exception is None:
            exception=dict(reason=REASONS[icon.icon_id],approved_by='user: delegated visual-exception decision to gpt-6',approved_on='2026-09-29',svg_sha256=hashlib.sha256(svg.encode()).hexdigest())
            text=mod.read_text()
            text=text.replace('    def build(self):','    exception = '+repr(exception)+'\n\n    def build(self):')
            mod.write_text(text)
            icon=load_icon(mod)
            assert icon.to_svg()==svg
        report=icon.validate_icon();g=gate(mod)
        print(icon.icon_id,g['status'],g.get('automatic_status',g['status']),flush=True)
        (p/'validation.txt').write_text(report.describe()+'\n\n'+json.dumps(g,indent=2)+'\n')
        (p/'gate.json').write_text(json.dumps(g,indent=2)+'\n')
        (p/(icon.icon_id+'.svg')).write_text(svg)
        render_previews(svg,icon.icon_id,48,p)
        meta=json.loads((p/(icon.icon_id+'.metadata.json')).read_text())
        ref=ROOT/meta['reference_path'];before=ref.parent.parent/'before'/(icon.icon_id+'.svg')
        for label,source in [('reference',ref),('before',before)]:
            for size in (48,384):
                cairosvg.svg2png(url=str(source),write_to=str(p/f'{label}-{size}.png'),output_width=size,output_height=size,background_color='white')
        d.text((5,i*244+4),icon.icon_id+' | '+('pass / exception' if icon.icon_id in REASONS else 'strict pass'),fill='black')
        for j,name in enumerate(['reference-384.png','before-384.png','preview-light-384.png','preview-dark-384.png']):
            sheet.paste(Image.open(p/name).convert('RGB').resize((192,192)),(j*218,i*244+28))
        for j,t in enumerate(['light','dark']):sheet.paste(Image.open(p/f'preview-{t}-48.png').convert('RGB'),(900,i*244+40+j*80))
        records.append(dict(run=str(p.relative_to(ROOT)),module=mod.name,icon_id=icon.icon_id,source_uuid=meta['source_uuid'],reference_path=meta['reference_path'],author=AUTHOR,comparison=meta['comparison'],feedback=meta['feedback'],changes=meta['changes'],construction_reference=meta['construction_reference'],keyshape=icon.keyshape.name,validation_status=report.status,build_gate=g,visual_review='Inspected original and rejected artwork, then native and enlarged revisions in light and dark. Smooth contours, coherent joins and clear subject retained.',omissions='Diamond sparkle sides simplify concave star edges.' if icon.icon_id.startswith('low-crescent') else 'Small original contour irregularities omitted; defining subject and arrangement preserved.',svg=icon.icon_id+'.svg'))
    sheet.save(BATCH/'comparison.png')
    (BATCH/'final-records.json').write_text(json.dumps(records,indent=2)+'\n')
    # result.json is written only after final sheet review.

if __name__=='__main__':main()
