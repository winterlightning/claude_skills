"""ABC monitor with user-authorized exceptional dimensions and native typeface v2.

Plan: 68x52 canvas; rounded screen centerlines (6,6)-(62,38), radius 4;
centered stand from (34,38) to (34,46), 20-unit foot. ABC uses the original
v2 glyph paths, scale 1, shared baseline, and 4-unit ink tracking. Text ink
starts at (12,12). Typeface internals remain user-supplied geometry; this
composition is not submitted as an ordinary SOLO48 icon.
"""
from pathlib import Path
import json
import xml.etree.ElementTree as ET
from icon_set.scripts.side_text import native_text

SOURCE_ICON_ID = 'dd80ecbb-13f8-47dc-9883-44bd19aa7cc6'
SOURCE_PATH = 'pictographic-primitives/other/monitor letters_dd80ecbb-13f8-47dc-9883-44bd19aa7cc6.svg'
AUTHOR = 'gpt-6'
SIZE_EXCEPTION = {'approved_by': 'user', 'request': 'for abc monitor , could you use our typeface v2, they could be exceptional size', 'canvas': [68,52], 'typeface': 'v2', 'glyph_scale': 1}
NS='http://www.w3.org/2000/svg'
ET.register_namespace('',NS)

class Drawing:
    icon_id='monitor-letters-typeface-v2'
    def to_svg(self):
        glyphs={g['character']:g for g in json.loads(Path(__file__).with_name('glyphs-v2.snapshot.json').read_text())['glyphs']}
        text,w,h,placements=native_text('ABC',glyphs,tracking=4)
        self.placements=placements
        self.text_bounds=[12,12,12+w,12+h]
        root=ET.Element(f'{{{NS}}}svg',{'width':'68','height':'52','viewBox':'0 0 68 52','fill':'none','stroke':'currentColor','stroke-width':'4','stroke-linecap':'round','stroke-linejoin':'round'})
        ET.SubElement(root,f'{{{NS}}}title').text='Computer monitor alphabet display — native typeface v2'
        ET.SubElement(root,f'{{{NS}}}rect',{'x':'6','y':'6','width':'56','height':'32','rx':'4'})
        ET.SubElement(root,f'{{{NS}}}path',{'d':'M34 38V46 M24 46H44'})
        group=ET.SubElement(root,f'{{{NS}}}g',{'transform':'translate(12 12)','data-typeface':'v2'})
        for child in ET.fromstring(text):
            if child.tag==f'{{{NS}}}g':group.append(child)
        return ET.tostring(root,encoding='unicode')+'\n'

if __name__=='__main__':
    path=Path(__file__).parent
    icon=Drawing()
    (path/(icon.icon_id+'.svg')).write_text(icon.to_svg())
