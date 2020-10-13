import os

def insertionSort(arr):
    for i in range(1, len(arr)):

        key = arr[i]

        j = i-1
        while j >= 0 and key < arr[j] :
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def main():
    # publications = ['New York Times', 'CNN', 'Breitbart', 'New York Post', 'Guardian', 'NPR', 'Reuters', 'Vox', 'Washington Post', 'Atlantic', 'Fox News', 'Buzzfeed News', 'National Review']
    publications = ['AllTheNews']
    results = open(os.getcwd()+"/results.txt", "w+")

    for publication in publications:
        filepath = os.getcwd() + '/src/' + publication + ' cbow.txt'
        # filepath = os.getcwd() + '/src/publications/' + publication + ' cbow.txt'
        file = open(filepath,'r')

        accuracies = {}
        data = file.read().split(']')

        for line in data:
            
            if "model:[vocabulary,percentage_correct,percentage_incorrect" == line:
                continue

            splitline = line.split(',')

            try:
                accuracies[splitline[0].strip().split(":")[0]] = float(splitline[1].strip())
            except IndexError:
                continue

        correctPercentages = []
        for value in accuracies:
            correctPercentages.append((accuracies[value]))

        insertionSort(correctPercentages)

        for model in accuracies:
            if accuracies[model] == correctPercentages[-1]:
                print("--------------------------------------")
                results.write("--------------------------------------\n")
                print(publication+":")
                results.write(publication+":\n")
                print("accuracies:")
                results.write("accuracies:\n")
                for i in accuracies:
                    if i == model:
                        print("\t"+i+":\t"+str(accuracies[i])+"\t<-----")
                        results.write("\t"+i+":\t"+str(accuracies[i])+"\t<-----\n")
                    else:
                        print("\t"+i+":\t"+str(accuracies[i]))
                        results.write("\t"+i+":\t"+str(accuracies[i])+"\n")
                print("######################################")
                results.write("######################################\n")
                print(str(model))
                results.write(str(model)+"\n")
                print("######################################\n\n")
                results.write("######################################\n\n\n")


if __name__== "__main__" :
    main()