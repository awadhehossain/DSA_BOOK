def binary_search(arr, item):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid][0]  # Access the name in the nested list
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

# Nested list containing names and their corresponding phone numbers
name_number = [
    ["Sophia", "01821947001"],
    ["Liam", "01821947002"],
    ["Olivia", "01821947003"],
    ["Noah", "01821947004"],
    ["Ava", "01821947005"],
    ["Ethan", "01821947006"],
    ["Isabella", "01821947007"],
    ["Mason", "01821947008"],
    ["Mia", "01821947009"],
    ["Lucas", "01821947010"],
    ["Amelia", "01821947011"],
    ["Charlotte", "01821947012"],
    ["Oliver", "01821947013"],
    ["Elijah", "01821947014"],
    ["Emma", "01821947015"],
    ["Aiden", "01821947016"],
    ["Harper", "01821947017"],
    ["Jackson", "01821947018"],
    ["Aria", "01821947019"],
    ["Benjamin", "01821947020"],
    ["Evelyn", "01821947021"],
    ["Henry", "01821947022"],
    ["Abigail", "01821947023"],
    ["Alexander", "01821947024"],
    ["Ella", "01821947025"],
    ["Michael", "01821947026"],
    ["Sofia", "01821947027"],
    ["Sebastian", "01821947028"],
    ["Avery", "01821947029"],
    ["Carter", "01821947030"],
    ["Scarlett", "01821947031"],
    ["James", "01821947032"],
    ["Zoey", "01821947033"],
    ["William", "01821947034"],
    ["Grace", "01821947035"],
    ["Logan", "01821947036"],
    ["Penelope", "01821947037"],
    ["Lucas", "01821947038"],
    ["Victoria", "01821947039"],
    ["Owen", "01821947040"],
    ["Lillian", "01821947041"],
    ["Levi", "01821947042"],
    ["Hannah", "01821947043"],
    ["Matthew", "01821947044"],
    ["Addison", "01821947045"],
    ["Daniel", "01821947046"],
    ["Layla", "01821947047"],
    ["Andrew", "01821947048"],
    ["Chloe", "01821947049"],
    ["Wyatt", "01821947050"],
    ["Nora", "01821947051"],
    ["Gabriel", "01821947052"],
    ["Ellie", "01821947053"],
    ["Ryan", "01821947054"],
    ["Stella", "01821947055"],
    ["Anthony", "01821947056"],
    ["Natalie", "01821947057"],
    ["Dylan", "01821947058"],
    ["Camila", "01821947059"],
    ["Samuel", "01821947060"],
    ["Aurora", "01821947061"],
    ["Christian", "01821947062"],
    ["Hazel", "01821947063"],
    ["Isaac", "01821947064"],
    ["Savannah", "01821947065"],
    ["Hunter", "01821947066"],
    ["Riley", "01821947067"],
    ["Nathan", "01821947068"],
    ["Bella", "01821947069"],
    ["Caleb", "01821947070"],
    ["Lucy", "01821947071"],
    ["Joshua", "01821947072"],
    ["Audrey", "01821947073"],
    ["Lincoln", "01821947074"],
    ["Aurora", "01821947075"],
    ["Christopher", "01821947076"],
    ["Mila", "01821947077"],
    ["Julian", "01821947078"],
    ["Violet", "01821947079"],
    ["Thomas", "01821947080"],
    ["Brooklyn", "01821947081"],
    ["Hudson", "01821947082"],
    ["Paisley", "01821947083"],
    ["Asher", "01821947084"],
    ["Scarlett", "01821947085"],
    ["Zachary", "01821947086"],
    ["Caroline", "01821947087"],
    ["Ezekiel", "01821947088"],
    ["Elliana", "01821947089"],
    ["Jason", "01821947090"],
    ["Leah", "01821947091"],
    ["Easton", "01821947092"],
    ["Ivy", "01821947093"],
    ["Elias", "01821947094"],
    ["Claire", "01821947095"],
    ["Adrian", "01821947096"],
    ["Zoey", "01821947097"],
    ["Josiah", "01821947098"],
    ["Kinsley", "01821947099"],
    ["Nicholas", "01821947100"],
]


# Sorting the nested list by names (first element in each sublist)
name_number.sort(key=lambda x: x[0])

# Print the sorted list
print("Sorted List:")
for person in name_number:
    print(person)

# Input and search
x = input("Which person do you want to access? ")
index = binary_search(name_number, x)

# Output
if index is not None:
    print("Name:", name_number[index][0])
    print("Number:", name_number[index][1])
else:
    print("Person not found.")
