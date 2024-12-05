# 3. Write a Program to Implement Tower of Hanoi using Python.

def tower_of_hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    tower_of_hanoi(n - 1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi(n - 1, auxiliary, target, source)

# Number of disks
num_disks = 3

# Solve the Tower of Hanoi problem
tower_of_hanoi(num_disks, 'A', 'C', 'B')
