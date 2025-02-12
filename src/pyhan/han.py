import os


class Han:
    dataset = {}

    def __init__(self):
        base_dir = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(base_dir, 'files/st.csv')
        with open(file_path) as f:
            for i in f:
                arr = i.strip().split(',', 1)
                self.dataset[arr[0]] = arr[1].split(',')
                if len(self.dataset[arr[0]]) > 1:
                    print(arr)

    def to_traditional(self, original):
        print(self.dataset)
        pass
        # print(predict_many(original, dataset, read2()))


if __name__ == '__main__':
    Han().to_traditional('我有很多萝卜，可以卜上一卦')
