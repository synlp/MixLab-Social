# MIX Lab Social

An English research showcase for social media information processing, information extraction, sentiment analysis, multimodal understanding and content safety. Designed as a companion to [MIX Lab Med](https://github.com/synlp/MixLab-Med).

## Preview

Run `python3 -m http.server 8767` in this directory and open `http://localhost:8767`.

## Content and build

`data/publications.json` is the editable catalogue. It contains paper and repository links, concise summaries, release notes and verified citation metadata where available. `scripts/build.py` renders the static homepage and citation files. Run `python3 scripts/build.py` after updating the catalogue. No dependencies or JavaScript build step are needed.

`assets/mobile.css` adapts the layout below 760 px with larger reading text, 44 px action targets, a full-width navigation menu and native research-area and year selectors. Topic selection stays synchronized with the desktop filter buttons. The build versions mobile styles and scripts by content hash so cached pages can load updates reliably.

The work is organized into five visible research areas, with dedicated overviews and subgroups for text sentiment, multimodal sentiment, entities, relations, data, safety and supporting tools. Search and year filters operate across these area blocks.

The catalogue was reviewed against [Yan Song’s NLP Group](https://github.com/synlp), its [representative publication list](https://github.com/synlp/.github/blob/main/README.md), individual repository READMEs and ACL Anthology records on 9 November 2026. General information extraction and language methods are included alongside studies specifically evaluating social media text. A project entry without a publication year does not assert a publication venue or date. The MABSA-LLMPlug journal entry follows its repository citation. Placeholder repositories without an identifiable paper or substantive project description are omitted. PlugLLM-MABSA is represented through the documented MABSA-LLMPlug project rather than counted twice.

Repository links describe the published release accurately. RE-CCG, RE-NGCN, ASA-CD and MemRCRHMD currently announce forthcoming code. TOSA-HMD explicitly provides the core method rather than all experiment scripts. Dataset access and licensing follow the linked project documentation.

The page shares the companion medical showcase’s branding, typography, spacing and components, with an independent navy, white and blue palette. `assets/social.css` contains social-page adjustments. The SVG research illustrations are conceptual; they are not experimental results or architectural reproductions.

## GitHub Pages

Publish the `main` branch at `/ (root)` using GitHub Pages. `.nojekyll` enables buildless static hosting. Every local URL is relative so the site works at a repository subpath.

## Rights

Original papers, repositories, datasets and models retain their respective rights and licenses. Follow each linked source’s license when using its resources.
