#Write a python program to merge two sorted arrays in non increasing order
arr1=[12.5, 67.8, 56.0, 34.88]
arr2=[11.7, 89.99]
sorted_arrays=sorted(arr1+arr2)
sorted_arrays.sort(reverse=True)
print(sorted_arrays)
