---

## project: dataset: stage: EDA step: 2 status: in-progress date: {{date}} notebook: tags: [eda, eda/02] previous: "[[EDA 01 - First Look]]" next: "[[EDA 03 - Univariate Distributions]]"

# EDA 02 — Missing Values

> [!abstract] Goal of this step Find out **how much** is missing, **where**, and **why**. The "why" decides the fix. Observe and record only; handling happens in cleaning.

---

## 1. Disguised missing values

Check these **first**. Otherwise the counts in section 2 undercount the problem.

- [ ] Sentinel numbers (`-999`, `0`, `9999`) where the value can't really be that
- [ ] Placeholder strings (`"Unknown"`, `"N/A"`, `"None"`, `"-"`, `"?"`)
- [ ] Empty strings / whitespace-only strings
- [ ] Impossible dates (`1900-01-01`, `1970-01-01`)

|Column|Disguised value|Count|Convert to NaN?|
|---|---|---|---|
|||||

---

## 2. Overall picture

|Metric|Value|
|---|---|
|Total cells missing||
|% of all cells||
|Columns with any missing|/|
|Rows with any missing||
|Rows complete (no missing)||

```python
# overall counts
```

---

## 3. Per-column missingness

Sort by % missing, highest first.

|Column|n missing|% missing|Type|Band|
|---|---|---|---|---|
||||||
||||||
||||||

> [!info] Rough bands **< 5%** — minor, usually simple to handle **5–30%** — look at the pattern before deciding **30–60%** — question whether the column earns its place **> 60%** — strong drop candidate, unless missingness itself is informative

![[missing-bar.png]]

---

## 4. Patterns — which columns go missing together?

Look at a missingness heatmap or a correlation matrix of the null indicators.

![[missing-heatmap.png]]

|Column group|Missing together?|Likely shared cause|
|---|---|---|
||||

## Observations:

---

## 5. Why is it missing?

|Mechanism|Meaning|How to spot it|Safe to drop rows?|
|---|---|---|---|
|**MCAR**|Random, unrelated to anything|No link to other columns or target|Yes (just costs data)|
|**MAR**|Depends on _other observed_ columns|Missing rate differs across another column's groups|No, drops bias the sample|
|**MNAR**|Depends on the _missing value itself_|Domain knowledge; can't prove it from the data|No, and imputation is risky|

|Column|Suspected mechanism|Evidence|
|---|---|---|
||||

---

## 6. Missingness vs target

For each column with meaningful missingness, compare the target between rows **with** and **without** the value.

|Column|Target when present|Target when missing|Different?|
|---|---|---|---|
|||||

> [!tip] If they differ The missingness itself carries signal. A binary `col_was_missing` flag may be worth keeping as a feature. Log it below.

---

## 7. Missingness over time

(If the data has a date column.) Does missingness change across years or months? A sudden drop usually means a collection change, not a data quality issue.

![[missing-over-time.png]]

## Observations:

---

## 8. Proposed handling

|Column|% missing|Mechanism|Proposal|Reason|
|---|---|---|---|---|
||||drop column / drop rows / impute median / impute mode / flag + impute / leave||

> [!warning] Leakage reminder Any imputation value (mean, median, mode) must be **fitted on the training split only**, then applied to test.

---

## 9. Questions to carry forward

- [ ]
- [ ]

---

## 10. Decision log

|Column(s)|Proposed decision|Reason|Actioned in|
|---|---|---|---|
|||||

---

## Links

Previous ← [[EDA 01 - First Look]] Next → [[EDA 03 - Univariate Distributions]] Related → [[Project Overview]] · [[Decision Log]]