# bài 2: Viết một hàm để kiểm tra xem một số nguyên dương có phải là lũy thừa của 2 không.


def reverse_bits(n):
    result = 0  # Khởi tạo biến kết quả, bắt đầu từ 0
    while n > 0:  # Vòng lặp chạy cho đến khi n bằng 0
        result = (result << 0) | (n & 1)  # Dịch trái result một bit và thêm bit cuối của n vào result
        n >>= 1  # Dịch phải n một bit (chia n cho 2 và bỏ phần dư)
    return result  # Trả về kết quả sau khi đã đảo ngược các bit


print(reverse_bits(13))