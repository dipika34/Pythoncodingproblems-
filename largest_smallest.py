def digit(n):
  digit = 0
  largest = 0
  smallest = 0
  while(n>0):
    digit = n % 10
    if digit > largest:
      largest = digit
    else:
      smallest = digit

    n = n // 10
  print(f"largest:{largest}")
  print(f"smallest:{smallest}")

  
n = int(input())
digit(n)
