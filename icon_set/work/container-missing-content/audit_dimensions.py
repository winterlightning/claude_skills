"""Measure rendered visible bounds in each SVG's own viewBox units."""
from pathlib import Path
import json,io,xml.etree.ElementTree as ET,html
import cairosvg
from PIL import Image
OUT=Path(__file__).resolve().parent

def measure(path):
 s=Path(path).read_text();root=ET.fromstring(s);v=[float(x) for x in root.attrib['viewBox'].replace(',',' ').split()]; scale=min(16,2048/max(v[2:]))
 im=Image.open(io.BytesIO(cairosvg.svg2png(bytestring=s.encode(),output_width=round(v[2]*scale),output_height=round(v[3]*scale)))).convert('RGBA');b=im.getchannel('A').getbbox();w=(b[2]-b[0])/scale;h=(b[3]-b[1])/scale
 return {'canvas':v[2:],'ink_width':w,'ink_height':h,'aspect_ratio':w/h}
rows=[]
for r in json.loads((OUT/'generation-status.json').read_text()):
 a=measure(r['reference']);b=measure(r['output']);delta=(b['aspect_ratio']/a['aspect_ratio']-1)*100
 rows.append({'number':r['number'],'name':r['name'],'original':a,'generated':b,'aspect_change_percent':round(delta,1),'review_proportions':abs(delta)>20})
(OUT/'dimension-audit.json').write_text(json.dumps(rows,indent=2)+'\n')
head='<html><meta charset="utf-8"><title>Container content dimension audit</title><style>body{font:15px system-ui;margin:32px}table{border-collapse:collapse}td,th{padding:10px;border-bottom:1px solid #ddd;text-align:left}.flag{background:#fff3d7}</style><h1>Original vs generated dimensions</h1><p>Visible ink measured at 16× resolution in each SVG’s own viewBox units (precision 1/16 unit for 48-unit assets; large originals sampled at up to 2048 pixels). Canvas sizes can differ; aspect ratio is the useful comparison for fitting. Changes over 20% are highlighted for visual review, not automatically failed. Text intentionally has a 32-unit maximum ink height.</p><table><tr><th>Icon</th><th>Original canvas</th><th>Original ink W × H</th><th>Generated canvas</th><th>Generated ink W × H</th><th>Aspect change</th></tr>'
for r in rows:
 a=r['original'];b=r['generated'];head+=f'<tr class="{"flag" if r["review_proportions"] else ""}"><td>{r["number"]}. {html.escape(r["name"])}</td><td>{a["canvas"]}</td><td>{a["ink_width"]:.2f} × {a["ink_height"]:.2f}</td><td>{b["canvas"]}</td><td>{b["ink_width"]:.2f} × {b["ink_height"]:.2f}</td><td>{r["aspect_change_percent"]:+.1f}%</td></tr>'
(OUT/'dimension-audit.html').write_text(head+'</table></html>')
print('Measured',len(rows),'icons;',sum(r['review_proportions'] for r in rows),'aspect changes above 20%')
