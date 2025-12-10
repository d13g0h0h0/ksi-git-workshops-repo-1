with open("artifact.txt", "w") as f:
	for i in range(200_000):
		print(i, file=f)
