"""Lowercase a-z for the official letter set: writes every SVG in Letters/official/lowercase.

Run from anywhere:  python3 Letters/official/source/lowercase.py
Guide lines (centerlines): ascender 2, x-height 7, baseline 17, descender 22.5.
Canvas 19 x 25 (m: 20 x 25), stroke 4, round caps and joins. Edit a path or a metric here and
rerun rather than editing the SVGs by hand; fillet.py builds the soft v tip."""
import os, sys
sys.path.insert(0,os.path.dirname(__file__))
from fillet import rounded
OUT=os.path.join(os.path.dirname(__file__),'..','lowercase'); os.makedirs(OUT,exist_ok=True)
A,X,B,D=2,7,17,22.5
ST='stroke="black" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"'
def svg(w,body): return f'<svg width="{w}" height="25" viewBox="0 0 {w} 25" fill="none" xmlns="http://www.w3.org/2000/svg">\n{body}</svg>\n'
def P(*ds): return ''.join(f'<path d="{d}" {ST}/>\n' for d in ds)
def ell(cx,cy,rx,ry): return f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" {ST}/>\n'
def circ(cx,cy,r): return f'<circle cx="{cx}" cy="{cy}" r="{r}" {ST}/>\n'
DOT=lambda x: f'M{x} 2L{x} 2'
g={}
# bowls: ellipse rx 4.5, ry 5 between x-height and baseline; o is a full circle
g['o']=(19,P('M9 7A4 4 0 0 1 13 11V13A4 4 0 0 1 9 17A4 4 0 0 1 5 13V11A4 4 0 0 1 9 7Z'))
g['a']=(19,P('M13 7V17','M13 7H10A5 5 0 0 0 10 17H13'))
g['b']=(19,P('M5 2V17','M5 7H9A4 4 0 0 1 13 11V13A4 4 0 0 1 9 17H5'))
g['d']=(19,P('M13 2V17','M13 7H9A4 4 0 0 0 5 11V13A4 4 0 0 0 9 17H13'))
g['p']=(19,P('M5 7V22.5','M5 7H9A4 4 0 0 1 13 11V13A4 4 0 0 1 9 17H5'))
g['q']=(19,P('M13 7V22.5','M13 7H9A4 4 0 0 0 5 11V13A4 4 0 0 0 9 17H13'))
g['g']=(19,P('M13 7H9A4 4 0 0 0 5 11V13A4 4 0 0 0 9 17H13','M13 7V19A3.5 3.5 0 0 1 8.3 22.29'))
g['c']=(19,P('M13 7C12 7 11.5 7 10.7 7C7.55 7 5 9.24 5 12C5 14.76 7.55 17 10.7 17C11.5 17 12 17 13 17'))
g['e']=(19,P('M5 12H13V11A4 4 0 0 0 9 7A4 4 0 0 0 5 11V13A4 4 0 0 0 9 17H13'))
g['n']=(19,P('M5 7V17','M5 11C5 8.8 6.8 7 9 7C11.2 7 13 8.8 13 11V17'))
g['h']=(19,P('M5 2V17','M5 11C5 8.8 6.8 7 9 7C11.2 7 13 8.8 13 11V17'))
g['u']=(19,P('M13 7V17','M5 7V13C5 15.2 6.8 17 9 17C11.2 17 13 15.2 13 13'))
g['m']=(20,P('M2 7V17','M2 11C2 8.8 3.8 7 6 7C8.2 7 10 8.8 10 11V17','M10 11C10 8.8 11.8 7 14 7C16.2 7 18 8.8 18 11V17'))
g['r']=(19,P('M6 17V7','M6 11.5C6 9 8 7 10.5 7H12'))
g['i']=(19,P(DOT(9),'M9 7V17'))
g['j']=(19,P(DOT(11),'M11 7V20A2.5 2.5 0 0 1 7.25 22.17'))
g['l']=(19,P('M8 2V14.5A2.5 2.5 0 0 0 10.5 17'))
g['t']=(19,P('M8 3V14A3 3 0 0 0 11 17','M5 7H11'))
g['f']=(19,P('M8 17V6A4 4 0 0 1 12 2','M5.5 7H10.5'))
g['k']=(19,P('M5 2V17','M12 7L5 13','M8 10.5L12.5 17'))
g['s']=(19,P('M12.5 7H9C6.4 7 5.4 9.8 7.4 11L10.6 13C12.6 14.2 11.6 17 9 17H5.5'))
g['v']=(19,P(rounded([((4,7),0),((9,17-1.5),1.5),((14,7),0)])))
g['w']=(19,P('M2 7L5 17L9 10.5L13 17L16 7'))
g['x']=(19,P('M5 7L13 17','M5 17L13 7'))
g['y']=(19,P('M4 7L9.73 17','M14 7L8 22.5'))
g['z']=(19,P('M5.5 7H13L5 17H13'))
for k,(w,body) in g.items(): open(os.path.join(OUT,f'{k}.svg'),'w').write(svg(w,body))
print(''.join(sorted(g)))
