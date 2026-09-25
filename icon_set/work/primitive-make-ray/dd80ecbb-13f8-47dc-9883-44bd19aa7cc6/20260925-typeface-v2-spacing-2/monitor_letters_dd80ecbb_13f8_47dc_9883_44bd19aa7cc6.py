"""Native v2 ABC monitor. User-authorized 2-unit clear ink gaps, 4-unit strokes, 60x46 canvas. Glyph paths remain unchanged; frame height follows exact native text bounds."""
from pathlib import Path
import json
import xml.etree.ElementTree as ET
from icon_set.scripts.side_text import native_text

SOURCE_ICON_ID = 'dd80ecbb-13f8-47dc-9883-44bd19aa7cc6'
SOURCE_PATH = 'pictographic-primitives/other/monitor letters_dd80ecbb-13f8-47dc-9883-44bd19aa7cc6.svg'
AUTHOR = 'gpt-6'
SIZE_EXCEPTION = {'approved_by': 'user', 'request': 'make it spacing = 2 unit instead 4 to make this smaller', 'canvas': [60,46], 'ink_spacing': 2, 'typeface': 'v2', 'glyph_scale': 1}
NS='http://www.w3.org/2000/svg'
ET.register_namespace('',NS)

class Drawing:
    icon_id='monitor-letters-typeface-v2'
    def to_svg(self):
        glyphs={g['character']:g for g in json.loads(Path(__file__).with_name('glyphs-v2.snapshot.json').read_text())['glyphs']}
        text,w,h,placements=native_text('ABC',glyphs,tracking=2)
        self.placements=placements
        self.text_bounds=[10,10,10+w,10+h]
        bottom=14+h
        foot=bottom+6
        root=ET.Element(f'{{{NS}}}svg',{'width':'60','height':'46','viewBox':'0 0 60 46','fill':'none','stroke':'currentColor','stroke-width':'4','stroke-linecap':'round','stroke-linejoin':'round'})
        ET.SubElement(root,f'{{{NS}}}title').text='Computer monitor alphabet display — native typeface v2'
        ET.SubElement(root,f'{{{NS}}}rect',{'x':'6','y':'6','width':'48','height':format(bottom-6,'.12g'),'rx':'4'})
        ET.SubElement(root,f'{{{NS}}}path',{'d':f'M30 {bottom:.12g}V{foot:.12g} M20 {foot:.12g}H40'})
        group=ET.SubElement(root,f'{{{NS}}}g',{'transform':'translate(10 10)','data-typeface':'v2'})
        for child in ET.fromstring(text):
            if child.tag==f'{{{NS}}}g':group.append(child)
        return ET.tostring(root,encoding='unicode')+'\n'

if __name__=='__main__':
    path=Path(__file__).parent
    icon=Drawing()
    (path/(icon.icon_id+'.svg')).write_text(icon.to_svg())
