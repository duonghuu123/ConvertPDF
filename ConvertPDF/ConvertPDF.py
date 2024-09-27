import tkinter as tk
from tkinter import filedialog
import pdfplumber

# Hàm đọc nội dung PDF và xuất ra chuỗi
def read_pdf():
    # Mở cửa sổ chọn file PDF
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    
    if file_path:
        with pdfplumber.open(file_path) as pdf:
            content = ''
            for page in pdf.pages:
                content += page.extract_text()
        
        # Hiển thị nội dung PDF
        text_box.delete(1.0, tk.END)  # Xóa nội dung cũ (nếu có)
        text_box.insert(tk.END, content)  # Hiển thị nội dung mới

# Tạo cửa sổ giao diện
window = tk.Tk()
window.title("PDF Reader")

# Nút chọn file PDF
button = tk.Button(window, text="Chọn file PDF", command=read_pdf)
button.pack(pady=10)

# Khung hiển thị nội dung PDF
text_box = tk.Text(window, wrap="word", height=30, width=100)
text_box.pack(padx=10, pady=10)

# Chạy ứng dụng
window.mainloop()
