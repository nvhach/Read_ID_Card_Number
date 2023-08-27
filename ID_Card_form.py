import pytesseract
from PIL import Image
import tkinter as tk
from tkinter import filedialog

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Hàm để trích xuất ID card từ ảnh và cập nhật giao diện
def trich_xuat():
    duong_dan = filedialog.askopenfilename()

    if duong_dan:
        image = Image.open(duong_dan)
        text = pytesseract.image_to_string(image)
        id_card_number = Tim_IdCard(text)
        
        if id_card_number:
            nhan_id.config(text="Số căn cước công dân: " + id_card_number)
        else:
            nhan_id.config(text="Không tìm thấy số nào trên thẻ căn cước công dân.")

# Hàm để tìm chuỗi số liên tiếp dài nhất trong văn bản
def Tim_IdCard(text):
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

# Tạo giao diện Tkinter
root = tk.Tk()
root.title("Trích xuất số ID card")

# Tạo nút để chọn ảnh
nut_button = tk.Button(root, text="Chọn ảnh CCCD/CMND", command=trich_xuat)
nut_button.pack(pady=20)

# Nhãn Label để hiển thị số ID card
nhan_id = tk.Label(root, text="", font=("Helvetica", 16))
nhan_id.pack()

root.mainloop()
