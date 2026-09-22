from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[3]))
import hashlib,json,cairosvg
from PIL import Image
from icon_set.model.icons.registry import create
from icon_set.scripts.workspace import DEFAULT_DIST
p=Path(__file__).parent
rows=json.loads((p/'accepted.json').read_text())
d=DEFAULT_DIST/'solo48'
manifest={r['icon_id']:r for r in json.loads((d/'manifest.json').read_text())['icons']}
results=[]
canvas=Image.new('RGB',(72*len(rows),144),'white')
for n,r in enumerate(rows):
    row=manifest[r['id']];svg=d/(r['id']+'.svg');data=svg.read_bytes();current=create(r['id']).to_svg().encode()
    assert row['validation']['status']=='valid' and not row['validation']['warnings'],r['id']
    assert hashlib.sha256(data).hexdigest()==row['svg_sha256'],r['id']
    assert data==current,r['id']+' export differs from source'
    result={'uuid':r['uuid'],'icon_id':r['id'],'svg':str(svg),'status':'valid','warnings':0,'sha256':row['svg_sha256'],'matches_original':True}
    results.append(result)
    for j,(bg,ink) in enumerate([('#ffffff','#141413'),('#1c1c19','#f5f4ef')]):
        out=p/(r['id']+f'-export-{j}-48.png')
        cairosvg.svg2png(bytestring=data.replace(b'currentColor',ink.encode()),write_to=str(out),output_width=48,output_height=48,background_color=bg)
        canvas.paste(Image.new('RGB',(72,72),bg),(n*72,j*72));canvas.paste(Image.open(out).convert('RGB'),(n*72+12,j*72+12))
canvas.save(p/'native-preview.png')
(p/'export-verification.json').write_text(json.dumps(results,indent=2))
print('Verified',len(results),'exports: valid, zero warnings, exact source and manifest hash matches.')
