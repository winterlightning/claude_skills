import sys,json,xml.etree.ElementTree as ET,hashlib
from pathlib import Path
sys.path.insert(0,str(Path.cwd()))
import cairosvg
from icon_set.scripts.workspace import build_dist
from icon_set.scripts.contact_sheet import THEMES
W=Path(__file__).parent
results=json.loads((W/'results.json').read_text())
manifest=json.loads((build_dist()/'solo48/manifest.json').read_text())
entries={r['icon_id']:r for r in manifest['icons']}
ns='{http://www.w3.org/2000/svg}'
for r in results:
 entry=entries.get(r['name']);p=Path(r['output']);r['manifest_verified']=entry is not None and p.exists()
 if entry:
  r['manifest_source_verified']=r['uuid'] in json.dumps(entry)
  print(r['name'],r['manifest_verified'],r['manifest_source_verified'])
 else:print('MISSING',r['name'])
for t,theme in THEMES.items():
 parts=[]
 for i,r in enumerate(results):
  p=Path(r['output'])
  if not p.exists():continue
  svg=ET.fromstring(p.read_text().replace('currentColor',theme['ink']))
  svg.set('x',str(20+(i%5)*180));svg.set('y',str(32+(i//5)*140));svg.set('width','48');svg.set('height','48')
  inner=ET.tostring(svg,encoding='unicode')
  parts.append(inner)
  big=ET.fromstring(p.read_text().replace('currentColor',theme['ink']));big.set('x',str(88+(i%5)*180));big.set('y',str(16+(i//5)*140));big.set('width','80');big.set('height','80');parts.append(ET.tostring(big,encoding='unicode'))
  parts.append(f'<text x="{20+(i%5)*180}" y="{112+(i//5)*140}" font-size="12" font-family="sans-serif" fill="{theme["ink"]}">{i+1:02}</text>')
 doc=f'<svg xmlns="http://www.w3.org/2000/svg" width="900" height="280"><rect width="900" height="280" fill="{theme["page"]}"/>'+''.join(parts)+'</svg>'
 (W/f'exports-{t}.svg').write_text(doc);cairosvg.svg2png(bytestring=doc.encode(),write_to=str(W/f'exports-{t}.png'))
(W/'results.json').write_text(json.dumps(results,indent=2))
