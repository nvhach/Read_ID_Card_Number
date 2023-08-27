import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Đường dẫn đến tệp ảnh của thẻ căn cước công dân
image_path = 'cccd.png'
# Đọc ảnh sử dụng thư viện Pillow (PIL)
image = Image.open(image_path)

# Sử dụng Tesseract OCR để trích xuất văn bản từ ảnh
text = pytesseract.image_to_string(image)

# Hàm để tìm chuỗi số liên tiếp dài nhất trong văn bản
def find_IdCard(text):
    current_ID = ""
    longest_ID = ""

    for char in text:
        if char.isdigit():
            current_ID += char
        else:
            if len(current_ID) > len(longest_ID):
                longest_ID = current_ID
            current_ID = ""

    # Kiểm tra chuỗi số cuối cùng
    if len(current_ID) > len(longest_ID):
        longest_ID = current_ID

    return longest_ID

# Lọc và tìm chuỗi số dài nhất từ văn bản trích xuất
id_card_number = find_IdCard(text)

# Kiểm tra xem có chuỗi số nào được tìm thấy hay không
if id_card_number:
    # In ra chuỗi số dài nhất
    print("Số căn cước công dân:", id_card_number)
else:
    print("Không tìm thấy số nào trên thẻ căn cước công dân.")
