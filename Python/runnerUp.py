# finds the 2nd largest

if __name__ == '__main__':
	num = int(input())
	score = set(map(int, input().split()))
	score.remove(max(score))
	print(max(score))