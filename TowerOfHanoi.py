def tower_of_hanoi(n, source, target, aux):
  """Recursive function to solve the Tower of Hanoi puzzle."""
  if n == 1:
    print(f'Move disk 1 from {source} to {target}')
    return
  tower_of_hanoi(n - 1, source, aux, target)
  print(f'Move disk {n} from {source} to {target}')
  tower_of_hanoi(n - 1, aux, target, source)

num_disks = int(input('Enter the number of disks: '))
tower_of_hanoi(num_disks, 'A', 'C', 'B')
