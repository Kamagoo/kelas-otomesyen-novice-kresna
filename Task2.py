x = int(input('masukan nilai : '))

def bil_prima (x):
  for i in range(2, x):
    if x % i == 0:
      return 'ini bukan bilangan prima'

  return 'ini bilangan prima'

print(bil_prima(x))