"""Bridge reviewed complete SUB32 studies into the fixed-4px combination engine."""
import json
import xml.etree.ElementTree as ET
from pathlib import Path

if __package__:
    from .workspace import development_dist
else:
    from workspace import development_dist



def engine_document(document):
    """Represent solid round dots as equivalent zero-length round-cap strokes.

    The legacy engine drops fill-only shapes. For these authored 4px assets,
    radius-2 filled circles paint exactly like a 4px round-capped point path.
    No outlines, dots, or source parts are removed.
    """
    root=ET.fromstring(document)
    if float(root.get('stroke-width','0')) != 4:
        raise ValueError('Combination engine requires a reviewed 4px source.')
    for parent in root.iter():
        for node in list(parent):
            if node.tag.split('}')[-1]=='circle' and node.get('stroke')=='none':
                if abs(float(node.get('r','0'))-2)>1e-8:
                    raise ValueError('Filled circle is not a 4px round dot.')
                x,y=node.get('cx','0'),node.get('cy','0')
                node.tag='{http://www.w3.org/2000/svg}path'
                node.attrib.clear();node.set('d',f'M{x} {y}L{x} {y}')
    return ET.tostring(root,encoding='unicode')


def reviewed_states(root):
    manifest=root.parent/'work/state-category-complete/manifest.json'
    if not manifest.exists():return {},[]
    result={};skipped=[]
    assets=root/'assets/combination-state32';public=development_dist(root.parent) / 'gallery/combination-state32'
    assets.mkdir(parents=True,exist_ok=True);public.mkdir(parents=True,exist_ok=True)
    for row in json.loads(manifest.read_text())['records']:
        uid=row['source_id'].lower();result[uid]=[]
        variant=next((v for v in row['versions'] if v['stroke']==4 and v['status']=='drawn'),None)
        if variant is None:
            skipped.append({'source_id':uid,'reason':'No drawable 4px version for this fixed-4px combination engine.'});continue
        source=manifest.parent/'svg'/variant['file']
        try:document=engine_document(source.read_text())
        except ValueError as error:
            skipped.append({'source_id':uid,'reason':str(error)});continue
        file=assets/(uid+'.svg');file.write_text(document);(public/file.name).write_text(document)
        result[uid]=[{'icon':'state32-'+uid,'family':'sub','svg':file.relative_to(root.parent).as_posix(),
                      'export_url':'combination-state32/'+file.name,'native_study':True,'stroke':4}]
    return result,skipped
