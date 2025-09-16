for i in range(0, 13):
    row = [str(i * j) for j in range(0, 13)]
    print(f"Table de {i}: {' '.join(row)}")