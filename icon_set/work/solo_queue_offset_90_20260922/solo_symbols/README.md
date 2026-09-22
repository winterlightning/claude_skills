# Five standalone symbols

The user explicitly classified ॐ, Я, Ω, अ and 한 as standalone solo icons and authorized authored geometry. The missing-typeface restriction from the earlier batch report does not apply to these five.

All five Python originals validate as **valid, zero warnings** on SOLO48. Light and dark contact sheets include unscaled 48-pixel renders; visual review found recognizable silhouettes, open counters, and deliberate proportions. Author: `gpt-6-astra`.

| Icon | Keyshape | Construction and visual review |
|---|---|---|
| Om Symbol with Crescent Moon | SQUARE | Retains crescent, dot, upper accent and connected lower lobes; flattened the crescent to open the gap to the lower silhouette. Small source irregularities simplified. |
| Cyrillic Letter Ya | VRECT_L | Broad upper bowl and right stem, with the diagonal leg attached at a shared node; decorative serifs omitted. |
| Greek Letter Omega Symbol | SQUARE | Symmetric broad bowl and matching outward feet; smooth upper arcs and a clear central opening. Tiny foot rounding omitted. |
| Hindi Devanagari Letter A | VRECT_L | Two equal lobes and a curved branch meet the right upright beneath a headline. Fine source flourishes simplified. |
| Korean Hangul Character Han | VRECT_L | Compact circle, top bar and tick, right upright with an arm, and lower angle all remain distinct. Component spacing widened for the profile. |

The original SVG references establish meaning and arrangement. Lucide `omega` and its atomic geometry informed coherent curve-to-stem construction; Lucide `moon` informed the crescent's closed contour. No source coordinates or typeface paths were imported.

Validation evidence: [validation.txt](validation.txt). Review sheets: [light](light.png) and [dark](dark.png). Clean native-size previews: [light](light-preview.png) and [dark](dark-preview.png).

All five exports are verified in `published/solo48/manifest.json` as valid with zero errors and warnings. Exported SVG hashes match the manifest and current Python originals. See [export-verification.json](export-verification.json). The Devanagari branch was moved to the exact lower-lobe attachment point (20,28), eliminating the small enclosed gap found by the first build. The other five items from offset 90 remain unresolved and were outside this follow-up request.
