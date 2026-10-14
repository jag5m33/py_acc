---

## project: dataset: stage: EDA step: 4 status: in-progress date: {{date}} notebook: tags: [eda, eda/04] previous: "[[EDA 03 - Univariate Distributions]]" next: "[[EDA 05 - Summary & Hypotheses]]"

# EDA 04 — Bivariate Relationships

> [!abstract] Goal of this step Two questions, in this order:
> 
> 1. **Feature ↔ target:** which features carry signal?
> 2. **Feature ↔ feature:** which features duplicate each other?

---

## 0. Pick the right tool for each pair

|Pair type|Plot|Statistic|
|---|---|---|
|numeric ↔ numeric|scatter / hexbin (large data)|Pearson (linear), **Spearman** (monotonic, robust)|
|numeric ↔ categorical|box / violin per group|group means + ANOVA / Kruskal–Wallis|
|categorical ↔ categorical|stacked bar / heatmap of crosstab|chi-square + **Cramér's V** (strength 0–1)|
|anything ↔ ordinal target|box per level / mean by level|**Spearman** (respects order, not spacing)|

> [!tip] Large datasets With millions of rows almost every p-value is tiny. Judge by **effect size** (correlation, Cramér's V, difference in group means), not significance.

---

## 1. Feature ↔ target

### Numeric features

|Feature|Plot|Spearman ρ|Direction|Strength|
|---|---|---|---|---|
||||+ / −|weak / moderate / strong|

![[num-vs-target.png]]

### Categorical features

|Feature|Levels compared|Target by level (mean / rate)|Cramér's V / effect|Notes|
|---|---|---|---|---|
||||||

![[cat-vs-target.png]]

### Datetime features

|Feature|Pattern vs target (hour, weekday, month, year)|
|---|---|
|||

> [!warning] Leakage check A relationship that looks **too strong** is the first sign of leakage. Ask: would this value exist _before_ the outcome happened?

Ranked shortlist — strongest signal first: 1. 2. 3.

---

## 2. Feature ↔ feature

### Correlation matrix (numeric)

![[corr-heatmap.png]]

|Pair|Correlation|Keep which?|Reason|
|---|---|---|---|
|||||

> [!info] Rough thresholds **|r| > 0.8** → likely redundant. Keep the one that's cleaner, less missing, or more strongly linked to the target. Redundant features inflate coefficient variance in linear models and make coefficients uninterpretable.

### Categorical overlaps

|Pair|Cramér's V|Same information?|
|---|---|---|
||||

---

## 3. Interactions worth noting

Relationships that **change depending on a third variable** (e.g. temperature matters only when it's raining). Candidates for engineered features later.

|Features|What changes|Feature idea|
|---|---|---|
||||

---

## 4. Questions to carry forward

- [ ]
- [ ]

---

## 5. Decision log

|Column(s)|Proposed decision|Reason|Actioned in|
|---|---|---|---|
|||||

---

## Links

Previous ← [[EDA 03 - Univariate Distributions]] Next → [[EDA 05 - Summary & Hypotheses]] Related → [[Project Overview]] · [[Decision Log]]