def main():
	tesouro = []
	line = ""
	while True:
		try:
			line = input()
			if line not in tesouro:
				tesouro.append(line)
		except EOFError:
			break
	print(len(tesouro))

if __name__ == "__main__":
	main()