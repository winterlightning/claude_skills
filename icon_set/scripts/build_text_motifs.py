"""Compose reused typeface paths with non-letter marks; retain TEXT28 lettering and trim combined ink bounds."""
import json,sys,html
from svgpathtools import parse_path

def compose(item,result):
    paths=[]
    for p in result['placements']:
        for d in p['glyph']['paths']:
            paths.append(parse_path(d).scaled(p['scale']).translated(complex(p['x'],p['y'])))
    W,H=result['width'],result['height'];kind=item['motif']
    def add(d):paths.append(parse_path(d))
    if kind=='flash':add(f'M-7 2 L-20 {H*.57} H-9 L-15 {H-2}')
    elif kind=='document':
        add(f'M-7 -8 H{W+2} L{W+10} 0 V{H+8} H-7 Z')
    elif kind=='chart':
        x=W+10;add(f'M{x} {H-2} H{x+31} M{x+5} {H-2} V{H*.65} M{x+16} {H-2} V{H*.38} M{x+27} {H-2} V2')
    elif kind=='table':
        x=W+10;y=2;b=H-2;m=(y+b)/2
        add(f'M{x} {y} H{x+32} V{b} H{x} Z M{x+16} {y} V{b} M{x} {m} H{x+32}')
    elif kind=='height':
        x=W/2;add(f'M{x-6} -14 L{x} -8 L{x+6} -14 M{x-6} {H+14} L{x} {H+8} L{x+6} {H+14}')
    elif kind=='width':
        y=H/2;add(f'M-15 {y-6} L-9 {y} L-15 {y+6} M{W+15} {y-6} L{W+9} {y} L{W+15} {y+6}')
    elif kind=='format':add(f'M-5 {H+8} H{W+5} M0 {H+18} H{W}')
    elif kind=='wrench':
        # Two opposing open jaws joined by a shaft, as in the original reference.
        y=H+14;x=W/2
        add(f'M0 {y-7} C8 {y-4} 8 {y+4} 0 {y+7} M{W} {y-7} C{W-8} {y-4} {W-8} {y+4} {W} {y+7} M6 {y} H{W-6}')
    else:raise ValueError('Unknown motif '+kind)
    boxes=[p.bbox() for p in paths];left=min(b[0] for b in boxes);top=min(b[2] for b in boxes);right=max(b[1] for b in boxes);bottom=max(b[3] for b in boxes)
    scale=1; width=right-left+4; height=bottom-top+4
    normalized=[p.scaled(scale).translated(complex(2-left*scale,2-top*scale)) for p in paths]
    title=html.escape(item['name']);body=''.join(f'<path d="{p.d()}"/>' for p in normalized)
    doc=f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" fill="none" stroke="currentColor" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"><title>{title}</title>{body}</svg>'
    return {'document':doc,'width':width,'height':height,'bounds':[0,0,width,height],'motif':kind}

if __name__=='__main__':
    inputs=json.load(sys.stdin);json.dump([compose(x['item'],x['result']) for x in inputs],sys.stdout)
