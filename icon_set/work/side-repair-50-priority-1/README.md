# Side-combination repair batch: 50 priority failures

Reviewed the 50 failed side sub-icons in the saved batch.json, ordered by waiting combinations.
41 independently editable variants passed model QA, exported SVG QA, container-circle composition, native light/dark review, and source-part coverage. Nine remain unresolved; audit.json records individual reasons and batch-local SKIP decisions. No skipped original is counted as generated.

Open index.html for original / before / repaired / centerline comparisons, native previews, filtering, and enlargement.

All 50 parent modules and original reference files are unchanged. 41 side-role records, 63 solo/profile links, and 301 combination-pair rows now reference the repaired variants. Independent container-symbol versions and manual review state are unchanged. Previously cached combined SVGs have not been regenerated.

Current side-library inventory: 825 icons; 628 passing, 187 failed, 10 review. 1,569 available pair records have a passing sub option, 181 await one, and seven legacy pairs still need mapping. These counts are eligibility, not regenerated combined SVGs. The remaining queue and next 50 are in ../side-repair-priority/.

Useful references: local Lucide originals and atomic-debug geometry for outlines, handles, matching radii, and repeated parts; human_ref/user.svg for the circular head and exact four-unit head/shoulder ink gap. Each repaired model records its keyshape and source-parts plan. No source parts were deliberately removed from accepted repairs; extra marks invented in prior models were removed where unsupported by the original.

Validation: targeted development build exited 0; 42 regression tests passed after permission for temporary local test sockets; doctor found zero tracked generated files. Verification evidence is in verification.json, release-qa.json and composition-checks.json. The role-routing regression test covers selecting repaired variants without changing the independent symbol.

Do not rerun publish.py after activation. Activation backups preserve the exact prior datasets. Exploratory authoring scripts are batch-specific; the Python variants in model/icons/sub are the authoritative repaired sources.
