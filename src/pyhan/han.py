import os


class Han:
    dataset = {}
    dataset2 = {}

    def __init__(self):
        base_dir = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(base_dir, 'files/st.csv')
        with open(file_path) as f:
            for i in f:
                arr = i.strip().split(',', 1)
                self.dataset[arr[0]] = arr[1].split(',')

        file_path2 = os.path.join(base_dir, 'files/st2.csv')
        with open(file_path2) as f:
            for i in f:
                arr = i.strip().split(',', 1)
                if arr[0] not in self.dataset2:
                    self.dataset2[arr[0]] = []
                self.dataset2[arr[0]].append(arr[1].split(','))

    def predict(self, idx, original):
        character = original[idx]
        if character in self.dataset2:
            current = self.dataset2[character]
            for i in current:
                if len(i) > 1:
                    for ii in i[1:]:
                        arr = ii.split('|')
                        if original[idx + int(arr[0]):idx + int(arr[1])] == arr[2]:
                            return i[0]
                else:
                    return i[0]

    def match(self, idx, original):
        character = original[idx]
        if character not in self.dataset:
            return character
        else:
            arr = self.dataset[character]
            if len(arr) == 1:
                return arr[0]
            else:
                character_predict = self.predict(idx, original)
                return character_predict if character_predict else character

    def to_traditional(self, original):
        return ''.join([self.match(i, original) for i in range(len(original))])


if __name__ == '__main__':
    traditional_text = Han().to_traditional('萝卜去哪了，可以在茶几卜上几卦')
    print(traditional_text)
