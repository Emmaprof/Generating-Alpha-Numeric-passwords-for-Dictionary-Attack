import string
words = []
class Combinations:
    def findResult(self, record, output, n, size):
        if (len(output) == 3):
            words.append(output)
            # Display output
            print(output)
        if (n == 0):
            return
        i = 0
        while(i < size):
            # Find result using recursion
            self.findResult(record, output + str(record[i]), n - 1, size)
            i += 1
def main():
    task = Combinations()
    # character elements
    record = list(string.ascii_letters + string.digits)
    size = len(record)
    # length of the generated string
    n = 3
    task.findResult(record, "", n, size)
main()

print('length', len(words))
with open('C:/Users/hp/Desktop/dict_attack.txt', 'w') as file:
    for word in words:
        file.write(word + '\n')