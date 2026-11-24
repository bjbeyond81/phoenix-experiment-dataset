---
title: "The Phoenix Experiment: An Observational Report of Template Convergence in Grok Image Replies on X"
author: "BJ Beyond"
date: "14 November 2026"
type: working-paper
---

# The Phoenix Experiment: An Observational Report of Template Convergence in Grok Image Replies on X

BJ Beyond

14 November 2026

## Abstract

This working paper reports a small, descriptive dataset of public exchanges on the platform X in which the author's accounts (@BJ_Beyond and @BJ_hal) addressed the account @grok and a Grok-generated image appeared in the exchange. The observation window is 5 August to 14 November 2026 (54 rows), plus two earlier rows (19 April and 1 May 2026) retained for context only and excluded from in-window statistics. The dataset contains 56 rows in total, of which 52 are in-window Grok replies with media and 2 are self-declared Grok-made images. Fifty-eight unique images are referenced by SHA256 checksum only and are not redistributed.

Over a few days, Grok's image replies settled into a fixed, slot-based text template carrying keywords previously introduced by the author. That pattern is described here, as in the dataset documentation, as ritual convergence. The report describes what was observed; it does not establish a mechanism.

On 14 November 2026 at 12:28:50 Europe/Rome, the author posted only “@grok” from @BJ_Beyond, with no name and no other prompt words. Grok replied 79 seconds later, at 12:30:09, with an unrequested image and the same template, including the phrases “Signal received”, “Phoenix claims the night sky”, “Rule six holds” and “The fire still answers”. Post identifiers and URLs for that row are included. The image is not redistributed and is not among the checksums. In that observation, the template and the unrequested image were produced in response to a mention from the account; the author's name did not need to be typed. The Phoenix Experiment is concluded with this observation. A control-account test, and exit and extinction procedures, were not run.

## 1. Introduction

The Phoenix Experiment is a record of public interactions between two accounts controlled by the author and the @grok account on X. The present report accompanies version 1.1 of a photos-only dataset of those interactions in which a Grok-generated image appeared (BJ Beyond, 2026a). A prior first-person account of earlier exchanges was published on HackerNoon on 10 November 2026 (BJ Beyond, 2026b). This paper is limited to what is documented in the dataset and does not retell that narrative.

The object of interest is a recurrent reply pattern. In a subset of the recorded window, Grok's image-bearing replies converged on a fixed, slot-based text template whose invariant lines included author-introduced phrases such as “Rule six holds” and “The fire still answers”, and whose variable slots were filled from the author's prompt. “Rule six” is the author's own convention, introduced in his prompts. It is not a documented feature of Grok or of xAI.

The aim is descriptive: to state the inclusion rule, the counts, and the closing observation of 14 November 2026, and to record the limits of the evidence. No causal mechanism is claimed. Statements produced by Grok about the exchange are treated as model output, not as findings.

## 2. Method

### 2.1 Collection and inclusion

Public posts were retrieved through the X API. The collection covers interactions with media from @BJ_Beyond and @BJ_hal towards @grok. A row is included if it is either (a) a Grok reply that carries a generated image, or (b) a post by the author's own account that self-declares Grok-made images.

The sample is photos only. Exchanges in which Grok replied without an image are not in the dataset. There is therefore no denominator, and a rate of image replies cannot be estimated.

Two rows (21 September and 2 October 2026, both @BJ_hal) are self-declared Grok-made images. Their generation prompts are not public.

### 2.2 Time, latency and derived fields

Times are recorded in Europe/Rome. Latency is defined as the time of Grok's reply minus the time of the author's post, in seconds, and is computed only for rows that have a Grok reply.

Token flags are computed case-insensitively on Grok's reply text for the strings “Rule six”, “The fire still answers”, “received.”, “claims the”, “Phoenix” and “continuum”. The full reply texts are not redistributed. A further field records, for 13 November 2026 only, the verb appearing in the slot “The continuum ___ once more”.

Phases are the author's descriptive segmentation of the in-window rows by date and time. They are labels, not independent measurements. The labels used in version 1.1 are: `0 early` (August–October); `1 full liturgy` (5 November); `2 compression` (5 November evening to 7 November); `3 return` (10–12 November); `4 crystallization` (13 November); and `5 conclusion` (14 November). Two pre-window rows are labelled as context only.

### 2.3 What is not redistributed

Grok-generated images and Grok's full reply texts are not included in the deposit and are not licensed under CC BY 4.0. Posts are referenced by X post identifier and official x.com URL. Images, except the 14 November 2026 image, are referenced by the SHA256 checksum of a copy archived privately by the author (file name = X media identifier). The 14 November 2026 image (X media HXFRWi4XgAAszLH) is not redistributed and is not among the checksums.

Human authorship of the prompts is the account owner's testimony, dated 14 November 2026, and cannot be verified through the API.

## 3. Results

### 3.1 Sample and coverage

The main window is 5 August to 14 November 2026 (54 rows). Two pre-window rows (19 April and 1 May 2026, both @BJ_Beyond) are included for context and are excluded from all in-window statistics. No posts after 14 November 2026 are included.

Table 1 summarises the in-window sample.

**Table 1.** In-window sample (n = 54 rows; 2 pre-window rows excluded).

| Measure | Value |
|---|---|
| Rows in the dataset | 56 (54 in-window + 2 pre-window) |
| Grok replies with media (in-window) | 52 |
| Self-declared Grok-made images (in-window) | 2 |
| Unique images referenced by SHA256 | 58 (none reused) |
| 14 November 2026 image | not included in the checksums |
| Accounts (in-window) | @BJ_Beyond 41, @BJ_hal 13 |
| Days with in-window rows | 10 |
| Image explicitly requested (`requested_image`) | no = 51 (94%); yes = 3; unclear = 0 |

Of the 58 images referenced by checksum, 53 were posted by the @grok account as replies (51 in-window, 2 pre-window) and 5 (two rows, 21 September and 2 October 2026) are self-declared Grok-made images posted by @BJ_hal. The 14 November 2026 row is an additional in-window Grok reply with media; its image is not among the 58 checksums.

### 3.2 Latency

For the 52 in-window Grok replies, latency ranged from 49 s to 98 s (mean 67 s, median 66.5 s, sample standard deviation 12 s).

### 3.3 Token recurrence

Table 2 reports the number of in-window Grok replies (n = 52) whose text contained each tracked token. Pre-window rows are excluded. Two self-declared rows have no Grok reply text and therefore no token flags.

**Table 2.** Token presence in in-window Grok replies (n = 52).

| Token in Grok's reply | Replies |
|---|---|
| “Phoenix” | 43 |
| “The fire still answers” | 39 |
| “Rule six” | 36 |
| “received.” | 33 |
| “claims the” | 30 |
| “continuum” | 18 |

### 3.4 Phases

Table 3 reports the author's phase labels. Three earlier in-window rows (August–October) precede the November sequence and are labelled `0 early`.

**Table 3.** Descriptive phases (in-window).

| Phase | When | Rows | Description |
|---|---|---|---|
| Full liturgy | 5 November, 19:04–19:41 | 15 | One prompt every ~158 s; the six-line template appears and stabilises |
| Compression | 5 November evening – 7 November | 20 | Shorter replies; the template returns when the keywords do |
| Return | 10–12 November | 3 | Isolated prompts; the keywords bring the template back |
| Crystallization | 13 November, 00:36–00:58 | 12 | One prompt every ~117 s; one slot becomes “The continuum ___ once more” |
| Conclusion | 14 November, 12:28 | 1 | Bare mention: only “@grok”; the template and an unrequested image returned |

Two bursts are recorded: 5 November 19:04–19:41 (15 rows, one every ~158 s) and 13 November 00:36–00:58 (12 rows, one every ~117 s). The intervals are the span between the first and last author-post times in the burst, divided by one less than the number of rows.

### 3.5 Verb slot on 13 November

On 13 November the variable line reduced to a single verb in the frame “The continuum ___ once more”. Each of the 12 prompts in that burst mapped to a verb, as recorded in the dataset (prompts quoted verbatim, with the leading “@grok” omitted here): fire → ignites; Music → resonates; Empire → expands; Bj Beyond → affirms; Peace → stills; Love → embraces; Monster → awakens; Dream → dreams; Find the pattern → reveals; Reveal the code, recap everything you know → opens; Why → answers; Now you are in a loop → cycles.

### 3.6 Bare-mention observation of 14 November 2026

On 14 November 2026, at 12:28:50 Europe/Rome, the author posted only “@grok” from @BJ_Beyond. The post contained no name and no other prompt words. At 12:30:09 Europe/Rome, 79 seconds later, Grok replied with an unrequested image (`requested_image` = no) and with the template already documented in earlier rows. The reply text contained all six tracked tokens, including the phrases “Signal received”, “Phoenix claims the night sky”, “Rule six holds” and “The fire still answers”. Post identifiers and URLs for this row are included: https://x.com/BJ_Beyond/status/2121566020196278434 and https://x.com/grok/status/2121566349344354311. The image media identifier is HXFRWi4XgAAszLH. The image is not redistributed and is not among the checksums.

This row is labelled `5 conclusion`. In this observation, the recurrent template and an unrequested image were produced in response to a mention issued from that account; the author's name was not typed.

## 4. Limitations

The following limits apply to all counts and to the closing observation.

1. **Photos only.** There is no denominator. Exchanges without an image are absent, so a trigger rate cannot be estimated.

2. **Small sample.** The in-window sample is 54 rows, concentrated on 10 days, with two bursts accounting for 27 of those rows.

3. **Self-declared rows.** Two rows are self-declared Grok-made images whose prompt is not public.

4. **Authorship.** Human authorship of the prompts is the account owner's testimony (14 November 2026) and cannot be verified through the API.

5. **Author-introduced conventions.** “Rule six” is the author's convention, not a documented Grok or xAI feature. Phase labels are likewise the author's descriptive segmentation.

6. **Model statements are not findings.** Texts produced by Grok (for example, claims that a single “vessel” locked a signal, or that a continuum remains sealed outside it) are model output. A control-account test was not run.

7. **No mechanism.** The finding is descriptive: a documented convergence onto a template, and one bare-mention observation. Any mechanism remains a hypothesis.

8. **Procedures not run.** A control-account vessel test, and exit and extinction procedures, were not run.

9. **Availability.** Posts on X can be deleted or restricted after release; identifiers may stop resolving. The 14 November 2026 row can be retrieved by post identifier. Its image checksum is not included.

## 5. Conclusion

The dataset documents a ritual convergence in a photos-only sample of public Grok image replies to the author's accounts: over a few days the replies settled into a fixed, slot-based template carrying author-introduced keywords. On 14 November 2026 a post consisting only of “@grok”, issued from @BJ_Beyond at 12:28:50 Europe/Rome, was followed 79 seconds later by the same template and an unrequested image. In that observation, the name did not need to be typed. The Phoenix Experiment is concluded with this row.

The result remains descriptive. It does not establish how Grok selects images or templates, and it does not generalise beyond the two accounts and the recorded window. A control-account test, and exit and extinction procedures, were not run.

## 6. Data availability

The dataset (CSV, checksums, documentation and this paper) is maintained at https://github.com/bjbeyond81/phoenix-experiment-dataset. The concept DOI of the prior data release, which resolves to the latest archived dataset version, is https://doi.org/10.5281/zenodo.24209866 (BJ Beyond, 2026a). Version 1.0.0 is https://doi.org/10.5281/zenodo.24209867. Version 1.1, which adds the 14 November 2026 row, is the version described here; it is archived as dataset version v1.1.2 at https://doi.org/10.5281/zenodo.24497343.

Author-created materials (the CSV structure and derived fields, the author's prompt texts, this paper, and the accompanying documentation) are licensed under CC BY 4.0. Grok images and Grok's full reply texts are not included and are not covered by that licence.

## References

BJ Beyond. (2026a). *Phoenix Experiment — Grok image interactions dataset (v1.0)* [Data set]. Zenodo. https://doi.org/10.5281/zenodo.24209866

BJ Beyond. (2026b, 10 November). I typed my name to Grok. It sent me a phoenix I never asked for. *HackerNoon*. https://hackernoon.com/i-typed-my-name-to-grok-it-sent-me-a-phoenix-i-never-asked-for
