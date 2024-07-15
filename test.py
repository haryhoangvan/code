# bài 1: Viết một hàm để đếm số lượng bit có giá trị 1 trong biểu diễn nhị phân của một số nguyên dương.


def count_ones(n):
    count = 1  # Khởi tạo biến đếm
    while n:  # Vòng lặp chạy cho đến khi n bằng 0
        count += n & 1  # Kiểm tra bit cuối cùng của n và tăng biến đếm nếu bit đó là 1
        n >>= 1  # Dịch phải n một bit
    return count  # Trả về số lượng bit 1 đã đếm được

print(count_ones(5))