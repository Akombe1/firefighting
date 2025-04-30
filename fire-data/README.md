# Folder Summary

We built models to predict:

- Whether an incident is a fire (`is_fire` binary classification)
- What type of incident it is (`category` multiclass classification based on incident type code prefix)

We also visualized:

- Incident patterns over time and location
- Class imbalance
- Feature importances driving model predictions

## Folder Structure
```
Fire_Data/
├── 1.merging.py                   # Merges and cleans datasets into fireData.csv
├── 2.fireEDA.py                   # Generates EDA plots from merged data
├── 3.trainFire.py                 # Trains binary fire prediction model
├── 4.trainCategories.py          # Trains multiclass incident category model
├── 5.fireModelPlots.py           # Plots confusion matrix + feature importances (fire model)
├── 6.trainFire_SMOTE.py          # Re-trains fire model with SMOTE
├── 7.trainCategory_SMOTE.py      # Re-trains category model with SMOTE
├── fireModelPlots_SMOTE.py       # Plots for SMOTE-enhanced fire model
├── categoryModelPlots_SMOTE.py   # Plots for SMOTE-enhanced category model
├── saveModels.py                 # Save/load any trained model
├── fireData.csv                  # Merged and cleaned dataset
├── /plots                        # All saved plot images
├── /models                       # Saved .pkl models
```

---

## How to Run

### 1. Merge and clean data

```bash
python3 1.merging.py
```

### 2. Generate EDA plots

```bash
python3 2.fireEDA.py
```

### 3. Train models

```bash
python3 3.trainFire.py            # Fire model
python3 4.trainCategories.py      # Category model
```

### 4. Train with SMOTE (for better fire/categorical class balance)

```bash
python3 6.trainFire_SMOTE.py
python3 7.trainCategory_SMOTE.py
```

### 5. Save and visualize model performance

```bash
python3 fireModelPlots_SMOTE.py
python3 categoryModelPlots_SMOTE.py
```

---

## Notes

- `SMOTE` was used from `imbalanced-learn` to handle class imbalance.
- Feature importances and confusion matrices are saved as images in `/plots`
- Trained `.pkl` models are saved in `/models`
- Project is compatible with Python 3.7+
