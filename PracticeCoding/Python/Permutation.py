#Check if there exists a permutation between two strings: For example, Hello can make the string Olleh as well
# Assumptions: Capital Letters don't matter
#              The number of characters used have to be exactly the same; it cannot exceed or go beyond. For example, wearmon != ear
# Reflection: This could have been done faster. The current running time is O(2n) as I initialize and insert into 2 dictionaries. To do this,
#             I could have instead check for false
#

def permutationCheck(a, b):
    dictionary = {}
    dictionary2 = {}

    # Assuming that
    a = a.lower()
    b = b.lower()

    for i in range(len(a)):
        if a[i] in dictionary:
            dictionary[a[i]] += 1
        else:
            dictionary[a[i]] = 1
    for j in range(len(b)):
        if b[j] in dictionary2:
            dictionary2[b[j]] += 1
        else:
            dictionary2[b[j]] = 1

    for k,v in dictionary.items():
        print(k,v)

    # Differences if False
    set_1 = set(dictionary.items())
    set_2 = set(dictionary2.items())

    value = set_2 - set_1
    print("Differences from set_1 to set_2 is ",value)

    if value == set():
        return True

    # this works as well
    #if dictionary == dictionary2:
    #    return True

    return False





if __name__ == '__main__':

    print(permutationCheck("Hello", "Olleh"))
