from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighboursClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

def ecu(a,b):
    return distance.euclidean(a,b)



def MarvellousKNeighborsClassifier():
    Dataset = load_iris()    # 1 Load the data 

    Data = Dataset.data
    Target = Dataset.target

    Data_train, Data_test, Target_train, Target_test = train_test_split(Data, Target, test_size = 0.5)

    Classifier = KNeighboursClassifier()

    Classifier.fit(Data_train, Target_train)

    Predictions = Classifier.Predict(Data_test)

    Accuracy = accuracy_score(Target_test, Predictions)



    return Accuracy


def main():
    MarvellousKNeighborsClassifier()

print("Accuracy is :", ret Accuracy*100)

if __name__ == "__main__":
    main()