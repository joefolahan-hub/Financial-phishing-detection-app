import matplotlib.pyplot as plt
from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    roc_auc_score,
    accuracy_score,
    ConfusionMatrixDisplay,
    RocCurveDisplay
)

# =========================
# EVALUATION FUNCTION
# =========================
def evaluate(model, X_test, y_test, model_name, dataset_size):
    y_pred = model.predict(X_test)

    acc = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)

    print(f"\n===== {model_name.upper()} ({dataset_size}) =====")
    print(report)

    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))

    try:
        auc = roc_auc_score(y_test, y_pred)
        print("ROC AUC:", auc)
    except:
        print("ROC AUC not available")

    return acc


# =========================
# CONFUSION MATRIX PLOT
# =========================
def plot_confusion(model, X_test, y_test, name, tag):
    ConfusionMatrixDisplay.from_estimator(model, X_test, y_test)
    plt.title(f"Confusion Matrix - {name} ({tag})")
    plt.savefig(f"results/confusion_{name}_{tag}.png")
    plt.close()


# =========================
# ROC CURVE PLOT
# =========================
def plot_roc(model, X_test, y_test, name, tag):
    RocCurveDisplay.from_estimator(model, X_test, y_test)
    plt.title(f"ROC Curve - {name} ({tag})")
    plt.savefig(f"results/roc_{name}_{tag}.png")
    plt.close()