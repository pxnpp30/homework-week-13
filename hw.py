def linear_search(arr, key):
    found = 0
    for i in range(len(arr)):
        if arr[i] == key:
            print("Element is found at position", i+1)
            found = 1
    if found == 0:
        print("Element is Not present in the array")

def binary_search(arr, low, high, key):
    if low <= high:
        mid = (low + high)//2
        if arr[mid] == key:
            print("The element is present at index:", mid)
        elif key < arr[mid]:
            binary_search(arr, low, mid-1, key)
        else:
            binary_search(arr, mid+1, high, key)
    else:
        print("Unsuccessful Search")

def interpolation_search(data, arr):
    lo = 0
    hi = len(arr) - 1
    comp = 0
    index = -1

    while lo <= hi and data >= arr[lo] and data <= arr[hi]:
        if arr[hi] == arr[lo]:
            if arr[lo] == data:
                index = lo
            break
        mid = lo + int(((hi - lo) * (data - arr[lo])) / (arr[hi] - arr[lo]))
        comp = comp + 1
        print("Comparisons:", comp, "mid =", mid)

        if arr[mid] == data:
            index = mid
            break
        elif arr[mid] < data:
            lo = mid + 1
        else:
            hi = mid - 1

    print("Total comparison made:", comp)
    if index != -1:
        print("Element found at location:", index+1)
    else:
        print("Element not found")

def get_array_input():
    raw = input("Enter numbers: ")
    raw = raw.replace(",", " ")
    parts = raw.split()
    arr = []
    for p in parts:
        try:
            arr.append(int(p))
        except:
            print("Please enter only numbers!")
            return []
    return arr

while True:
    print("\n=== SEARCH MENU ===")
    print("1. Binary Search")
    print("2. Linear Search")
    print("3. Interpolation Search")
    print("4. Exit")
    choice = input("Select menu (1-4): ")

    if choice == "4":
        print("Exit Program")
        break

    arr = get_array_input()
    if len(arr) == 0:
        print("No data in array")
        continue

    key = int(input("Enter key to search: "))

    if choice == "1":
        arr.sort()
        print("Sorted array:", arr)
        binary_search(arr, 0, len(arr)-1, key)
    elif choice == "2":
        linear_search(arr, key)
    elif choice == "3":
        arr.sort()
        print("Sorted array:", arr)
        interpolation_search(key, arr)
    else:
        print("Invalid choice!")

    back = input("\n back to menu? (y/n): ")
    if back.lower() != "y":
        print("Program closed")
        break
