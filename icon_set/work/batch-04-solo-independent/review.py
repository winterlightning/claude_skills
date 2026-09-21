"""Render only independently authored candidates and save their actual QA."""
from pathlib import Path
import html
import io
import json
import cairosvg
from PIL import Image, ImageDraw
from icon_set.model.icons.registry import create
from icon_set.validation.library_qa import inspect_icon

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT/'work/drawn-unpublished-2026-09-21/batch-04/solo-results'
NAMES = ['Star-eyed face','Sun, cloud and rain','Hooded swaddle','Diagonal baby wrap',
         'Three-star rating','User-centered diagram','Open-end wrench','Magnifying glass']
NOTES = [
    'CIRCLE: round facial silhouette. Mirrored five-point stars and centered smile retained; star holes and face/eye clearances cannot fit in this candidate. Smaller eyes would erase their openings.',
    'SQUARE: room for cloud, sun, three rays and three rain strokes. The lower cloud edge is opened, following Lucide cloud-sun-rain, to remove the narrow band beneath its shoulder. Weather layout is intentionally asymmetric.',
    'VRECT_L: upright hood and blanket. The face is a radius-6 circle at (24,19); the enclosing hood is radius 16 at (24,20). Facial details omitted. Two blanket folds meet at a shared node. This face opening is enclosed by clothing, not a detached stick-figure head.',
    'VRECT_M: broad circular head and rounded wrap. Radius-14 head at (24,18); wrap attaches at the head sides, and the fold meets its lower cardinal point. These are real clothing contacts, not a detached head/body gap. No eyes or fingers. Circular anatomy follows human_ref/user.svg.',
    'HRECT_M: the widest and shallowest permitted rectangle. Three identical upright stars retained. A faithful row remains much shallower than this envelope, and shrinking the stars further would destroy their holes. Diagonal or staggered rows would change the requested horizontal arrangement.',
    'SQUARE: square above, circle and triangle below, bust inside three orbit arcs. Human head radius 3 at (24,24); head bottom 27, shoulder top 35, exactly 8 centerline / 4 ink units. This analytical human gap is correct, but the surrounding shapes and arcs do not clear each other. The complete arrangement remains a failed candidate.',
    'SQUARE: diagonal wrench fills the envelope. Single coherent contour, open jaw and radius-5 rounded heel; lightning modifier omitted as required by the component brief. Lucide wrench informed the jaw and heel construction.',
    'SQUARE: radius-15 lens and attached diagonal handle; plus modifier omitted as required by the component brief. Lucide search informed the two-part construction. Handle attaches at an exact integer 3-4-5 circle point.',
]

def main():
    jobs=json.loads((OUT/'jobs.json').read_text())
    for j,name,note in zip(jobs,NAMES,NOTES):
        icon=create(j['icon_id'])
        svg=icon.to_svg()
        (OUT/(j['icon_id']+'.svg')).write_text(svg)
        report=icon.validate_icon()
        (OUT/(j['icon_id']+'.validation.txt')).write_text(report.describe()+'\n')
        qa=inspect_icon(icon)
        qa.pop('_svg',None)
        (OUT/(j['icon_id']+'.qa.json')).write_text(json.dumps(qa,indent=2,default=str)+'\n')
        j.update(name=name,model_status=report.status,qa_status=qa['status'],notes=note,
                 errors=qa['errors'],warnings=qa['warnings'])
        print(j['index'],name,qa['status'],flush=True)
    (OUT/'jobs.json').write_text(json.dumps(jobs,indent=2)+'\n')
    for theme,bg,ink in [('light','#ffffff','#111111'),('dark','#15181d','#ffffff')]:
        sheet=Image.new('RGB',(1040,600),bg)
        draw=ImageDraw.Draw(sheet)
        for i,j in enumerate(jobs):
            svg=(OUT/(j['icon_id']+'.svg')).read_text().replace('currentColor',ink)
            x=i%4*260;y=i//4*300
            for size,dx,dy in [(144,58,20),(48,106,185)]:
                png=cairosvg.svg2png(bytestring=svg.encode(),output_width=size,output_height=size)
                tile=Image.open(io.BytesIO(png)).convert('RGBA')
                sheet.paste(tile,(x+dx,y+dy),tile)
                if size==48:
                    tile.save(OUT/(j['icon_id']+f'-{theme}-48.png'))
            draw.text((x+15,y+253),f'{i+1}. {j["name"]}',fill=ink)
            draw.text((x+15,y+273),'QA: '+j['qa_status'].upper(),fill='#208f65' if j['qa_status']=='pass' else '#c86b47')
        sheet.save(OUT/(theme+'.png'))
    cards=[]
    for j in jobs:
        svg=(OUT/(j['icon_id']+'.svg')).read_text()
        svg=svg[svg.index('<svg'):]
        findings=''.join('<li>'+html.escape(s)+'</li>' for s in j['errors']+j['warnings'])
        cards.append(f'<article><h2>{j["index"]}. {j["name"]}</h2><div class="large">{svg}</div><div class="native">{svg}</div><p class="{j["qa_status"]}">QA: {j["qa_status"].upper()}</p><p>{j["notes"]}</p><p><a href="{j["icon_id"]}.svg">SVG</a> · <a href="{j["icon_id"]}.qa.json">QA evidence</a></p><details><summary>Validation findings</summary><ul>{findings or "<li>No errors or warnings.</li>"}</ul></details></article>')
    (OUT/'index.html').write_text('''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>Batch 04 · Independent icon-solo</title><style>
    *{box-sizing:border-box}body{font:15px/1.5 system-ui;margin:32px;background:#f5f6f8;color:#141821}body.dark{background:#15181d;color:#f5f6f8}main{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:24px}article{border:1px solid #8885;border-radius:12px;padding:20px}h1{font-size:28px}h2{font-size:18px}.large,.native{text-align:center;margin:20px}.large svg{width:144px;height:144px}.native svg{width:48px;height:48px}.pass{color:#168259}.fail,.review{color:#c76b42}a{color:inherit}button{font:inherit;padding:8px 16px;margin:0 0 24px}li{margin:10px 0;font-size:13px}</style><h1>Batch 04 · Independent icon-solo</h1><p>Fresh drawings from the saved briefs and original references. No distilled geometry or previews inspected. Large views are 3×; small views are native 48px.</p><button onclick="document.body.classList.toggle('dark')">Toggle light / dark</button><main>'''+''.join(cards)+'</main></html>')
    report=['# Batch 04 — independent icon-solo drawings','',
        'Eight independently authored SOLO48 candidates, using AUTHOR = `gpt-6` (new model-author label). Prior drawings and distilled previews were not inspected. Existing source files were searched for identity only; no drawing geometry was reused. Fresh variant modules were scaffolded directly to avoid copying the comparison artwork.','',
        '- [Interactive review](index.html) — native 48px and 3×, theme toggle, QA details.',
        '- [Light sheet](light.png) · [Dark sheet](dark.png).',
        '- `jobs.json` maps each candidate to its Python source and original UUID.',
        '- Five candidates pass model validation and full build QA with zero warnings. Three are failed comparison candidates, not approved icons.','',
        '## Construction evidence','',
        'Original source references were rendered into `references.png`. Local Lucide originals and atomic-debug SVGs inspected: face-slightly-smiling, star, cloud-sun-rain, baby, shapes, wrench, search. Human references inspected: `icon_set/references/human_ref/user.svg` and `full_body_ref.png`. No existing Pictographic candidate geometry was inspected.','',
        'The icon-solo skill requires “status must be "valid" with zero warnings” and says “A reported blocker beats a weakened rule.” The three failures below remain explicit; no profile, tolerance, connection rule or exception was changed.','',
        '## Per-icon review','']
    for j in jobs:
        report += [f'### {j["index"]}. {j["name"]} — {j["qa_status"].upper()}','',j['notes'],'',
            f'- Source: `{j["python"]}`',f'- [SVG]({j["icon_id"]}.svg) · [Full QA]({j["icon_id"]}.qa.json)','']
        if j['errors'] or j['warnings']:
            report += ['Findings:']+['- '+s for s in j['errors']+j['warnings']]+['']
    report += ['## Component routing','',
        'The wrench and magnifying-glass briefs explicitly reject combined primitives. Only their standalone SOLO48 subjects were authored. The lightning bolt and plus sign remain separate SUB32 authoring handoffs in `component-briefs.md`; neither was embedded or scaled.','',
        '## Build and tests','',
        'See `build.log` and `test-results.md` for the final execution results. Gallery build locking is respected. Direct QA uses the same `inspect_icon()` function used by the build pipeline.','']
    (OUT/'README.md').write_text('\n'.join(report))

if __name__=='__main__':
    main()
