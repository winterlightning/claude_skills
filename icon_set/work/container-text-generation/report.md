# Container text generation

Generated 294 text-family SVGs with the Experiment / Typeface layout engine and existing glyph paths. All SVG heights and viewBox heights are exactly 32 units; widths preserve proportions. Case, underlines and multi-line text are retained.

294 source references are linked in Progression, covering 446 container combinations. The refreshed missing-sub inventory has 163 references left, including the 34 unresolved text-related candidates below.

Verification: 9 focused Python tests; typeface and container grouping JavaScript suites; all 294 SVG canvas dimensions and source mappings; native-size rendered review; browser verification of the Text family and fixed-height editor.

Rebuild artwork: `node icon_set/scripts/build_text_icons.cjs`. Gallery builds retain the `text32/manifest.json` records and source links. Typeface exports use their own layout checks rather than solo/sub/container geometric keyshapes.

## Unresolved candidates

- **Automatic Camera Flash** (`6d9d5bd7-6db0-481a-9ec6-b441510546fe`): Mixed artwork: lightning bolt plus A; text-only output cannot fulfill the complete source.
- **Braille Alphabet Dot Pattern** (`9a878067-c24e-4478-bd0a-a0a8e12afcc0`): Braille dots have no glyphs in this typeface.
- **Dollar Sign Document** (`b37bb9fc-399c-4459-8327-fe334e14a831`): Missing currency glyph and document outline.
- **Dollar Sign Financial Bar Chart** (`5dbcbb68-16e1-4360-ae98-eef09cf0bf26`): Missing currency glyph and chart.
- **Dollar Sign with Data Table** (`11a7c3b8-c2a0-4757-ac27-663841d3d0ec`): Missing currency glyph and table.
- **Double Opening Quotation Marks** (`a4bb6523-5409-472a-9edb-6375a39e127d`): Missing quotation mark glyph.
- **Element Of Mathematical Symbol** (`bb9677cc-3914-4404-9543-635f8db0dac8`): Missing mathematical glyph.
- **Email At Symbol** (`05ce412b-7bf2-475f-b716-cff70d4117e0`): Missing at-sign glyph.
- **Hindu Om Symbol** (`4fbbd7ce-d884-4bf7-bd73-518bcdb43d35`): Missing Om glyph.
- **Internal Server Error Alert** (`9c6caa89-6c69-4c63-aded-c90fc8dd3814`): Missing exclamation mark glyph.
- **Japanese Yen Currency Symbol** (`4a06d69f-2edd-4b80-be80-a8b144c9e4ee`): Missing currency glyph.
- **Plus One Symbol** (`014b4126-429a-4160-8632-9d676a0117a8`): Missing plus glyph.
- **Subset of or Equal To Symbol** (`a83c7456-ab64-437d-9647-fc11cd8bf5f0`): Missing mathematical glyph.
- **Text Formatting and Style** (`e0363621-7f83-4768-b93a-69d3b06ec1c9`): Mixed artwork: A plus two formatting lines; not a simple underline.
- **Two Minus One Math Expression** (`17d5ec75-09d3-4664-bd59-09488d4395a3`): Missing minus glyph.
- **Two Point Five Meter Height Limit** (`38ba2a2e-533c-4f13-8799-64c05185a0e7`): Missing decimal point and dimension arrows.
- **Wrench Size 24** (`7074083f-5ac1-4fee-a100-a5eed3e2870a`): Mixed artwork: text and wrench.
- **C Plus Plus Programming Language** (`fe40b320-52ca-41ee-9fde-5c659d270f28`): Missing plus glyph.
- **Digital Time Display 9:40** (`893943bc-8343-4560-8eb4-9293b26dcad3`): Missing colon glyph.
- **Fifty Percent Symbol** (`254107b8-2e1f-4879-9aa3-f41a62637304`): Missing percent glyph.
- **Four Meters Height Limit** (`a47b1045-80c6-488c-96a8-7c8c2d19fc7f`): Mixed artwork: text and height arrows.
- **Four Meters Width Indicator** (`f92f1287-4d1f-4f11-b3d2-cf575c8bb3ec`): Mixed artwork: text and width arrows.
- **Four to Three Aspect Ratio** (`a06e30da-f7cc-4c53-9588-4b22f1c462c1`): Missing colon glyph.
- **Paragraph Text Tool** (`73c9c828-e821-4ad7-b187-92724a7bdd13`): Mixed artwork: T with paragraph lines.
- **Plus Minus Symbol** (`81b9a65e-38c0-48f5-8dea-bf51b80889cf`): Missing plus-minus glyph.
- **PM 2.5 Air Quality** (`8b0a9ddc-8697-4997-850a-98781ee56225`): Missing decimal point glyph.
- **Seventy Percent Symbol** (`2db006bf-b601-494c-82f0-ad85cdab5beb`): Missing percent glyph.
- **Simple Percentage Symbol** (`b6714fe0-b147-4d47-a0f0-425cf97aee98`): Missing percent glyph.
- **Simple Question Mark Symbol** (`eb0fc6ce-ceab-4fe9-a55e-5a7e98c04d7a`): Missing question-mark glyph.
- **Sixteen By Nine Aspect Ratio** (`b2c5933c-a7bb-4f0b-8d93-88dcd37a3d38`): Missing colon glyph.
- **Thai Baht Currency Symbol** (`7c740c03-3323-47d7-93fa-89d191da2b7a`): Missing currency glyph.
- **Thirty Percent Discount Symbol** (`b382b4ba-42e6-4be3-b4ce-eacfbea2233b`): Missing percent glyph.
- **Two to Zero Score** (`7166f712-4d90-4e1d-9e81-eb0a413b8372`): Missing colon glyph.
- **Width Measurement Two Point Five Meters** (`9a1c2aa2-6935-41f2-96ed-4f3ebc7f1fc0`): Missing decimal point and dimension arrows.

Stroke correction: all 294 exports now have effective stroke width 4 in the final 32-unit canvas, including underlines. Geometry and spacing are fitted while stroke remains constant. All path transform/stroke products were checked. Multi-line text necessarily has smaller, heavier-looking glyphs within that fixed height.

Height revision: all 294 active text-family exports now use text28, with canvas/viewBox height 28 and effective stroke width 4. Gallery and Progression links updated; fixed-height layout tests and per-export stroke verification passed.

Ink-height revision: all 294 text28 exports have zero padding on all four sides. Visible stroke ink spans y=0 through y=28, including underlines and descenders. Effective stroke remains 4. Full-batch ink-bound tests passed.
