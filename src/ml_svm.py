from data_loader_svm import Data_Loader
from svm import SVM
import numpy as np

def main():
    data_path = './data'
    test_size_ratio = 0.1

    loader = Data_Loader(data_path)
    # unshuffled split of data to train and test
    [train_img, train_labels, test_img, test_labels] = [np.array(x) for x in loader.load_all_data(test_size_ratio)]

    # call SVM(train_img, train_labels, test_img, test_labels) train, test
    svm_classifier = SVM(train_img, train_labels, test_img, test_labels)
    svm_classifier.train()
    #svm_classifier.plots()

if __name__ == '__main__':
    main()