import json,io
from pathlib import Path
from PIL import Image,ImageDraw
import cairosvg
ROOT=Path(__file__).parent.resolve()
entries=json.loads((ROOT/'entries.json').read_text())
lines=['# Meaning repair batch — thuan-mac', '',
       'Requested 20 at offset 0; production supplied 19 claimable icons. All 19 received a finish call.', '',
       'Feedback for every icon: “Does not convey the intended meaning.” Bitcoin and briefcase feedback additionally named “bitcoin” and “dollar.”', '',
       'Authored with `AUTHOR = gpt-6`. Original references and rejected drawings were inspected. Each result folder contains the Python original, input metadata, reference render, SVG, light/dark previews and validation evidence.', '',
       '| Icon key | Revision / blocker | Validation | Production outcome | Artifacts |',
       '| --- | --- | --- | --- | --- |']
counts={}
sheet=Image.new('RGB',(840,((len(entries)+3)//4)*230),'white');draw=ImageDraw.Draw(sheet)
for i,e in enumerate(entries):
    run=Path(e['run']).resolve();fix=Path(e['fix']).resolve()
    result=json.loads((fix/'result.json').read_text());design=json.loads((run/'design.json').read_text())
    counts[result['outcome']]=counts.get(result['outcome'],0)+1
    status=result['validation_status']+'; build gate '+result['build_gate']['status']
    note=design['plan'] if result['outcome']=='done' else result['note']
    links=f"[RESULT_DIR]({run}) · [SVG]({run / (e['icon_id']+'.svg')}) · [evidence]({fix/'result.json'})"
    lines.append(f"| solo/{e['icon_id']} | {note} | {status} | {result['outcome']} | {links} |")
    x=i%4*210;y=i//4*230
    draw.text((x+6,y+4),e['icon_id'][:29],fill='black')
    draw.text((x+6,y+19),result['outcome'],fill='black')
    svg=(run/(e['icon_id']+'.svg')).read_text()
    for yy,theme,bg,fg in [(y+40,'light','#ffffff','#111111'),(y+130,'dark','#171717','#eeeeee')]:
        draw.rectangle((x+4,yy,x+204,yy+86),fill=bg)
        for xx,size in [(x+12,48),(x+103,80)]:
            a=Image.open(io.BytesIO(cairosvg.svg2png(bytestring=svg.replace('currentColor',fg).encode(),output_width=size,output_height=size)))
            sheet.paste(a,(xx,yy+3),a)
lines += ['', '## Construction and omissions', '']
for e in entries:
    d=json.loads((Path(e['run'])/'design.json').read_text())
    lines += [f"- **{e['icon_id']}** — {d['keyshape']}. {d['references']}. {d['omissions']}"]
lines += ['', f"Confirmed outcomes: {counts.get('done',0)} done (Ready), {counts.get('cannot-fix',0)} cannot-fix (Disapproved).",'',
          'The user clarified “Tog” as thermal insulation / duvet tog rating; its tag interpretation was replaced by a folded duvet with warmth waves. The Bitcoin adjustment sliders were omitted to prioritize the explicit bitcoin feedback. No registered module, gallery build, publish or push was performed.']
(ROOT/'REPORT.md').write_text('\n'.join(lines)+'\n')
sheet.save(ROOT/'final-contact-sheet.png')
print(json.dumps(counts))
