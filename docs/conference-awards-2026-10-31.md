# Conference award update — October 31, 2026

Before this update, the last content commit added **AAAI 2025** (May 20, 2025). The latest conference by event date was **ICLR 2025**, April 24–28, 2025.

Added **36 conference editions** and **343 award records** for existing venue series. Existing conference records and citation counts are unchanged. Entries are sorted by conference start date, newest first.

## Added editions

Each award in `_data/papers.yml` records its verification source. Paper titles link to the publisher, proceedings, preprint, or official project when verified; otherwise they link to the verified award announcement.

| Venue | Editions added | Awards added |
| --- | --- | ---: |
| 3DV | 2025, 2026 | 5 |
| AAAI | 2026 | 15 |
| ACL | 2025, 2026 | 73 |
| CASE | 2024, 2025, 2026 | 9 |
| CoRL | 2025 | 3 |
| CVPR | 2025, 2026 | 12 |
| ECCV | 2022, 2024, 2026 | 9 |
| EMNLP | 2022, 2023, 2024, 2025, 2026 | 106 |
| Humanoids | 2023, 2024, 2025 | 7 |
| ICCV | 2025 | 4 |
| ICLR | 2026 | 3 |
| ICML | 2025, 2026 | 20 |
| ICRA | 2025, 2026 | 22 |
| IROS | 2025, 2026 | 3 |
| NeurIPS | 2025 | 7 |
| RSS | 2025, 2026 | 7 |
| SIGGRAPH | 2025, 2026 | 37 |
| WAFR | 2022 | 1 |

## Verification and coverage limits

- Winners, runners-up, honorable mentions, and test-of-time awards retain their announced categories. Finalists are not presented as winners. SAC highlights, unrelated workshops, personal honors, and TACL awards presented at ACL are excluded.
- ICRA 2026 includes the two verified Best Conference Paper recipients, the verified Best Student Paper recipient, and verified planning/control, manipulation/locomotion, and HRI winners. Its official awards page still lists finalists; other category winners are not inferred from those lists.
- IROS 2025 includes the verified Best Conference Paper and Best Student Paper winners. IROS 2026 includes the verified Best Paper winner. Other IROS category winners remain to be verified.
- CASE 2026 includes the verified Best Conference Paper winner, XFlowMP. Its official page still lists finalists; other categories remain to be verified.
- Humanoids 2023 includes the Best Oral Paper winner, confirmed by the winner’s institution and its award-ceremony photograph. Other 2023 paper categories remain to be verified.
- WAFR 2022 includes the Outstanding Paper winner confirmed by the authors’ MIT laboratory. Reliable award results were not located for WAFR 2018, 2020, 2024, or 2026; no winners or annual editions are fabricated.
- EMNLP 2022’s two Best Paper winners are recorded from an attending researcher’s conference report and matched to ACL Anthology metadata. The report identifies the Tangram paper as Best Long Paper and the authorship paper as Best Short Paper; additional categories remain to be verified.
- CoRL 2026, NeurIPS 2026, and Humanoids 2026 occur after this audit date, so no award entries are added. ICCV and ECCV alternate years; WAFR is biennial. No nonexistent annual editions are added.
- IJCAI-JAIR is a historical award-series label in the existing data rather than an entry in the venue catalog; this update adds no new venue series.

## Primary evidence for editions with incomplete conference award pages

- [ICRA 2026: SymSkill — IEEE RAS](https://www.ieee-ras.org/yifei-simon-shao-on-symskill-and-long-horizon-robot-manipulation/)
- [ICRA 2026: OmniRetarget — authors’ laboratory](https://lecar-lab.github.io/publications.html)
- [ICRA 2026: LASER — University of Stuttgart](https://www.icd.uni-stuttgart.de/news/IEEE-ICRA-2026-Best-Student-Paper-Award/)
- [CASE 2026: XFlowMP — IEEE RAS](https://www.ieee-ras.org/khang-nguyen-on-xflowmp-and-learning-to-plan-robot-movements/)
- [IROS 2025: Best Conference Paper — Shenyang Institute of Automation](https://english.sia.cas.cn/news/Events/202512/t20251212_1136776.html)
- [IROS 2025: Neural MP — coauthor’s research page](https://jim-young6709.github.io/)
- [IROS 2026: LT-Mem — authors’ laboratory](https://team-aprl.github.io/news.html)
- [Humanoids 2023: Best Oral Paper — LIRMM](https://www.lirmm.fr/2023/12/19/congratulations-to-celia-saghour-who-won-the-best-oral-paper-award-at-the-ieee-humanoids-2023-conference/)
- [WAFR 2022: Outstanding Paper — MIT Robot Locomotion Group](https://locomotion.csail.mit.edu/index.html)
- [EMNLP 2022: conference report — AISB](https://aisb.org.uk/conference-reports-empirical-methods-in-natural-language-processing-emnlp-2022/)

## Validation

- Parsed the complete YAML with both Python/PyYAML and Ruby/Psych.
- Confirmed all 139 pre-existing conference records are unchanged.
- Checked unique venue/year pairs, duplicate award/title pairs, required metadata, absolute HTTPS links, and chronological ordering.
- Rendered the existing home-page Liquid template with all data: 175 conference editions and 1,041 award records. Checked every new title, author string, and link against the generated HTML.
- Visually inspected the local browser preview; the latest conference and its award groups display correctly.
- `git diff --check` passes.
- Full Jekyll build could not run: the system Ruby 2.6 environment lacks development tools needed to build the `ffi` dependency. The Liquid render is a partial build check, not a claim that the full GitHub Pages dependency bundle ran.
