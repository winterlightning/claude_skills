import sys,json,xml.etree.ElementTree as ET
from pathlib import Path
sys.path.insert(0,str(Path.cwd()))
from icon_set.scripts.side_text import glyph_map,native_text
SOURCE_ICON_ID='7ecac39c-d98d-4ff3-af33-ae4cbc274cb3'
SOURCE_PATH='pictographic-primitives/other/rectangle buy text_7ecac39c-d98d-4ff3-af33-ae4cbc274cb3.svg'
AUTHOR='gpt-6'
WORD='BUY'
NS='http://www.w3.org/2000/svg'
def generate():
 doc,w,h,placements=native_text(WORD,glyph_map())
 root=ET.Element('{'+NS+'}svg',dict(viewBox='0 0 64 48',width='64',height='48',fill='none',stroke='currentColor',**{'stroke-width':'4','stroke-linecap':'round','stroke-linejoin':'round'}))
 ET.SubElement(root,'{'+NS+'}title').text=WORD+' — native typeface v2'
 if WORD=='ABC':
  frame='M8 3 H56 A4 4 0 0 1 60 7 V34 A4 4 0 0 1 56 38 H8 A4 4 0 0 1 4 34 V7 A4 4 0 0 1 8 3 Z'
  ET.SubElement(root,'{'+NS+'}path',d=frame)
  ET.SubElement(root,'{'+NS+'}path',d='M32 38 V45 M23 45 H41')
  ty=(41-h)/2
 else:
  ET.SubElement(root,'{'+NS+'}rect',x='4',y='7',width='56',height='34',rx='4')
  ty=(48-h)/2
 group=ET.SubElement(root,'{'+NS+'}g',transform=f'translate({(64-w)/2} {ty})')
 for child in ET.fromstring(doc):
  if child.tag.endswith('g'):group.append(child)
 return ET.tostring(root,encoding='unicode'),placements
if __name__=='__main__':
 svg,_=generate();Path(__file__).with_suffix('.svg').write_text(svg)
