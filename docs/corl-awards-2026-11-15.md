# CoRL award update — November 15, 2026

Added **RoboTTT: Context Scaling for Robot Policies**, winner of the main-conference **Best Student Paper** award. The existing SuperMimic Best Paper entry is unchanged.

## Evidence and scope

- [NVIDIA's publications page](https://research.nvidia.com/labs/lpr/publications/) explicitly labels RoboTTT as “Best Student Paper Award and Oral” under “Conference on Robot Learning (CoRL) · 2026.” This is the award source in the data.
- [arXiv](https://arxiv.org/abs/2607.15275) verifies the title, all eleven authors in order, and the paper link. The author string follows arXiv, including Linxi "Jim" Fan.
- The [conference website](https://2026.corl.org/) distinguishes the November 9–11 main conference from the November 12 workshops.
- The [official awards page](https://2026.corl.org/program/awards) still did not expose award results through the web reader. No other new main-conference paper-award winners were verified. This update does not claim complete coverage or promote finalists to winners.

## Workshop awards excluded

These newly public results were checked against the workshop organizers' own pages and are deliberately not added to the CoRL main-conference entry:

| Workshop | Paper-award winners excluded | Organizer source |
| --- | --- | --- |
| Agentic Robotics | Agentic World Action Models; EmbodiedSWE: Coding Agents for Long-Horizon Dexterous Robotics | [Workshop awards](https://agentic-robotics-workshop.github.io/) |
| RoboLetics 3.0 | Reflex: Visually Grounded Reactive Humanoid Control; runner-up An Adversarial Multi-Agent Pursuit Game for Locomotor Agility Pretraining | [Workshop awards](https://roboletics.github.io/corl2026/) |
| Grounded 4D Multimodal World Models | OpenLongTail: Generative Scaling of Long-Tail Driving Data | [Workshop recap](https://arlo0o.github.io/Grounded-Driving-World-Models_Workshop/) |

Workshop demo and challenge awards are also excluded. A paper's acceptance at the main conference alone does not make a workshop award a main-conference award.

## Validation

- Parsed the complete YAML with Ruby/Psych; verified required metadata, HTTPS links, unique venue/year pairs, and distinct award/title pairs.
- Confirmed the sole data change is appending RoboTTT to CoRL 2026; all previous award records and conference metadata are unchanged.
- Rendered the existing home-page Liquid template and checked both CoRL award categories, titles, authors, and links.
- `git diff --check` passes.
- Full Jekyll build remains unavailable because the local environment lacks the locked Bundler 2.1.4; the Liquid render is a partial build check.
