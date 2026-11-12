# CoRL award update — November 11, 2026

Added CoRL 2026 and its confirmed **Best Paper** winner, **SuperMimic: Scaling Humanoid Whole-Body Control with One Differentiable World Model**.

## Evidence

- [First author Qiayuan Liao's announcement](https://x.com/qiayuanliao/status/2120740445923823846) explicitly reports the Best Paper win. X could not be fetched directly; the exact post was readable through its [public mirror](https://teapawt.net/qiayuanliao/status/2120740445923823846). The data retains the original X URL as the award source.
- [arXiv](https://arxiv.org/abs/2610.28480) confirms the complete title and seven authors and supplies the paper link.
- [Official conference website](https://www.corl.org/) confirms Austin, Texas, USA, November 9–12, 2026.

## Coverage

The [official awards page](https://www.corl.org/program/awards) had no published results when checked. No additional main-conference winners were verified. Best Student Paper, other award categories, and finalists are therefore not added; this entry is not a claim of complete award coverage. Earlier author pages listing SuperMimic as a finalist do not establish a student-paper win. Workshop awards are outside this update's scope.

The October 31 audit's statement that CoRL 2026 was still upcoming remains an accurate historical note; this update records the newly announced result.

## Validation

- Parsed the complete YAML with Ruby/Psych, checked the new entry's required fields and HTTPS links, and confirmed unique venue/year pairs.
- Confirmed all 175 existing conference editions are unchanged. CoRL 2026 is inserted before EMNLP 2026 by conference start date.
- Rendered the existing home-page Liquid template with all 176 editions and verified the new title, authors, paper link, conference dates, and page position.
- `git diff --check` passes.
- Full Jekyll build was unavailable because the local environment lacks the locked Bundler 2.1.4. The Liquid render is a partial build check.
