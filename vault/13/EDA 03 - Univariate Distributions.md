---

## project: dataset: stage: EDA step: 3 status: in-progress date: {{date}} notebook: tags: [eda, eda/03] previous: "[[EDA 02 - Missing Values]]" next: "[[EDA 04 - Bivariate Relationships]]"

# EDA 03 — Univariate Distributions

> [!abstract] Goal of this step Look at **each column on its own**: shape, spread, outliers, rare categories. This tells you what needs transforming, capping or grouping before any relationships make sense.

---

## 1. Numeric — summary table

|Column|Mean|Median|Std|Min|Max|Skew|Notes|
|---|---|---|---|---|---|---|---|
|||||||||
|||||||||

```python
# describe + skew
```

> [!info] Reading the table **Mean ≫ median** → right skew (long tail of large values) **|skew| > 1** → strongly skewed, consider a log / sqrt transform **Min or max impossible** → data error, not an outlier. Log it.

---

## 2. Numeric — shape

One histogram + one box plot per column.

![[hist-numeric.png]]

|Column|Shape|Transform candidate?|
|---|---|---|
||normal / right-skewed / left-skewed / bimodal / spiky|none / log / sqrt / bin|

> [!tip] Spiky or bimodal? Spikes at round numbers usually mean rounding or manual entry. Two humps usually mean two sub-populations mixed together. Both are worth a note.

---

## 3. Numeric — outliers

|Column|Method|n outliers|%|Genuine or error?|
|---|---|---|---|---|
||IQR (1.5×) / z-score (> 3)||||

> [!info] Which method **IQR** — works on skewed data, the safer default **z-score** — assumes roughly normal data, misleading on skewed columns

Rule: **errors get fixed or removed; genuine extremes stay** (or get capped, if they would dominate a squared-error model).

---

## 4. Categorical — frequencies

|Column|n unique|Top category|Top %|Rare categories (< 1%)|Notes|
|---|---|---|---|---|---|
|||||||

![[bar-categorical.png]]

Checks:

- [ ] Inconsistent labels (`"Rain"` vs `"rain"` vs `"Light Rain"`)
- [ ] High cardinality (too many levels to one-hot encode)
- [ ] One level dominating (> 95%) → near-constant
- [ ] Rare levels to group into `"Other"`

---

## 5. Datetime

|Column|Earliest|Latest|Gaps / oddities|
|---|---|---|---|
|||||

Counts by year, month, weekday and hour:

![[datetime-counts.png]]

## Observations:

---

## 6. Target — distribution recap

![[target-distribution.png]]

|Item|Value|
|---|---|
|Shape / class balance||
|Implication for modelling||
|Implication for metrics||

---

## 7. Questions to carry forward

- [ ]
- [ ]

---

## 8. Decision log

|Column(s)|Proposed decision|Reason|Actioned in|
|---|---|---|---|
|||||

---

## Links

Previous ← [[EDA 02 - Missing Values]] Next → [[EDA 04 - Bivariate Relationships]] Related → [[Project Overview]] · [[Decision Log]]