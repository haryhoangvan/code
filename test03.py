bài 3:  Viết một hàm để đảo ngược các bit của một số nguyên dương và trả về số nguyên kết quả sau khi đảo ngược.


def reverse_bít(n):
	result = 0
	while n > 0:
		result = (result << 1) | (n & 1)
		n >>= 1 
	return result


print(reverse_bít(13))