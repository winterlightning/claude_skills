# video game control directions — blocked

Source: `pictographic-primitives/_uncategorized_39/video game control directions_171ff3c8-7724-4935-ac18-b58d43e05931.svg`

Keyshape: HRECT_L. BLOCKED: widest horizontal keyshape and enlarged buttons still cannot hold full A/B labels with8-unit clearance. Open pad retained; enclosures and both letters preserved.

Pad center and outline simplified to open cross. Unframed A/B candidate rejected because button enclosures are defining.

Blocked: A/B overlap their circular borders; no acceptable enclosed-letter composition passed. Open-label alternative loses defining button outlines.

References: supplied SVG rendered as reference.png; Lucide original/trash-2.svg and atomic-debug/trash-2.svg: shared handle nodes and coherent rounded contours; Lucide original/tv.svg and atomic-debug/tv.svg: consistent rounded enclosure construction

```text
BUILD GATE FAIL (fail, 7 errors, 2 warnings)
  error: mic [button-a]: button-a and button-b are 2.36116 apart on centerlines nearest (22.9322, 23.5039)<->(25.0542, 22.4682); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  error: mic [button-a]: button-a and a are 2.7886 apart on centerlines nearest (8.47931, 36.3375)<->(10, 34); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  error: mic [button-a]: button-a and b are 6.12455 apart on centerlines nearest (23.9248, 26.7759)<->(30, 26); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  error: mic [button-b]: button-b and b are 1.05539 apart on centerlines nearest (29.5371, 26.9484)<->(30, 26); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  error: mic [button-b]: button-b and pad-2 are 4.56086 apart on centerlines nearest (36.7297, 27.6196)<->(38, 32); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  error: mic [b]: b and pad-2 are 6.77063 apart on centerlines nearest (35.4859, 25.7134)<->(38, 32); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  error: holes/pinches: 1 undersized holes; 1 pinches
  warning: internal-spacing [b / b-top]: b-0 and b-top-1 have 3.5224 units of ink clearance over 4.1881 units; requires 4; review required
  warning: internal-spacing [b]: b-1 and b-3 have 3.5224 units of ink clearance over 4.1881 units; requires 4; review required
```
