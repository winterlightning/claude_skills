"""Repair existing SOLO48 modules; no variants or contract changes.
SOURCE_ICON_ID and SOURCE_PATH are preserved per target. AUTHOR = gpt-6.
"""
import json,re,textwrap
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
WORK=Path(__file__).resolve().parent
TARGETS=json.loads((WORK/'targets.json').read_text())
HELPERS='''
l = self.add_line
p = self.add_polyline
link = self.relate

def a(name, start, end, rx, ry=None, sweep=True):
    self.add_arc(name, start, end, radius_x=rx,
                 radius_y=rx if ry is None else ry, sweep=sweep)

def c(name, x, y, radius):
    a(name+'-top', (x-radius,y), (x+radius,y), radius)
    a(name+'-bottom', (x+radius,y), (x-radius,y), radius)
    self.add_contour(name, name+'-top', name+'-bottom', closed=True)

def r(name, x0, y0, x1, y1, radius=4):
    # Equal corner radii and shared tangent endpoints own the rounded box.
    points = [(x0+radius,y0),(x1-radius,y0),(x1,y0+radius),
              (x1,y1-radius),(x1-radius,y1),(x0+radius,y1),
              (x0,y1-radius),(x0,y0+radius)]
    ids=[]
    for index,start in enumerate(points):
        end=points[(index+1)%8]
        if start==end:
            continue
        part=f'{name}-{index}'
        if index%2:
            a(part,start,end,radius)
        else:
            l(part,start,end)
        ids.append(part)
    self.add_contour(name,*ids,closed=True)
'''
def write(index, key, body, note):
 row=TARGETS[index];path=ROOT/row['source_path']
 old=path.read_text();head=old[:old.index('    def build(')]
 head=re.sub(r"AUTHOR\s*=.*", "AUTHOR = 'gpt-6'",head)
 head=re.sub(r'keyshape = Keyshape\.\w+',f'keyshape = Keyshape.{key}',head)
 head=re.sub(r'^""".*?"""',repr(note),head,count=1,flags=re.S)
 body=textwrap.dedent(body).strip()
 helpers=HELPERS
 if not re.search(r'\br\(',body): helpers=helpers[:helpers.index('\ndef r(')]
 if not re.search(r'\bc\(',body):
  start=helpers.index('\ndef c(');end=helpers.find('\ndef r(',start)
  helpers=helpers[:start]+(helpers[end:] if end>=0 else '')
 source=head+'    def build(self):\n'+textwrap.indent('# '+note+'\n'+helpers.strip()+'\n\n'+body+'\n','        ')
 path.write_text(source)
 notes=json.loads((WORK/'notes.json').read_text()) if (WORK/'notes.json').exists() else {}
 notes[row['icon_id']]=note
 (WORK/'notes.json').write_text(json.dumps(notes,indent=2))
