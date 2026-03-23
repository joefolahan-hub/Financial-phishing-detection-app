import matplotlib.pyplot as plt

def plot_dataset_comparison():
    sizes = [5000, 82500]

    logistic_acc = [0.95, 0.96]
    svm_acc = [0.97, 0.98]

    plt.figure()
    plt.plot(sizes, logistic_acc, marker='o', label='Logistic Regression')
    plt.plot(sizes, svm_acc, marker='o', label='SVM')

    plt.xlabel("Dataset Size")
    plt.ylabel("Accuracy")
    plt.title("Model Performance vs Dataset Size")
    plt.legend()

    plt.savefig("results/dataset_comparison.png")
    plt.close()

    print("Graph saved in results folder")