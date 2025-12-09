items = [1.7, 2,2,2,2, 'C', "Apple", 5]
print(f"My itemss : {items}")


#list Operations
items.append("My ele")
items.append(345)
items.append("")
items.append('F')
print(f"My updated items : {items}")

items.insert(0,456)
items.insert(4,'H')
print(f"My updated items : {items}")

items.pop()
print(f"My updated items : {items}")
items.pop(5)
print(f"My updated items pop index : {items}")

items[3] = "Vikram"
print(f"My replace items : {items}")

trimmedItems = items[2:7]
print(f"My items : {items}")
print(f"My trimmed items : {trimmedItems}")

trimmedItems.pop(0)
trimmedItems.pop(2)
#trimmedItems.sort()
sortedItems = sorted(trimmedItems)
print(f"My triimmed sorted items : {sortedItems}")
"""
output:
My itemss : [1.7, 2, 2, 2, 2, 'C', 'Apple', 5]
My updated items : [1.7, 2, 2, 2, 2, 'C', 'Apple', 5, 'My ele', 345, '', 'F']
My updated items : [456, 1.7, 2, 2, 'H', 2, 2, 'C', 'Apple', 5, 'My ele', 345, '', 'F']
My updated items : [456, 1.7, 2, 2, 'H', 2, 2, 'C', 'Apple', 5, 'My ele', 345, '']
My updated items pop index : [456, 1.7, 2, 2, 'H', 2, 'C', 'Apple', 5, 'My ele', 345, '']
My replace items : [456, 1.7, 2, 'Vikram', 'H', 2, 'C', 'Apple', 5, 'My ele', 345, '']
My items : [456, 1.7, 2, 'Vikram', 'H', 2, 'C', 'Apple', 5, 'My ele', 345, '']
My trimmed items : [2, 'Vikram', 'H', 2, 'C']
My triimmed sorted items : ['C', 'H', 'Vikram']
"""

