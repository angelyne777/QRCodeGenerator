import qrcode
import os
from datetime import datetime

def get_input(prompt, default=None, allow_empty=False):
    while True:
        data = input(prompt).strip()  #strip() ---> removes extra space
        if data or allow_empty:
            return data or default
        print("❗ Input cannot be empty.")

def generate_qr(data, filename, fill_color="black", back_color="white"):
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    img.save(filename)
    img.show()
    print(f"✅ Saved as '{filename}'")

def choose_colors():
    print("\nChoose QR colors (or press Enter for defaults):")
    fill = get_input("Fill color [default=black]: ", "black", allow_empty=True)
    back = get_input("Background color [default=white]: ", "white", allow_empty=True)
    return fill, back

def get_filename(default_name="qrcode"):
    filename = get_input("Filename (without extension) [default=qrcode]: ", default_name, allow_empty=True)
    filename = filename.replace(" ", "_") + ".png"
    return filename

def single_qr_generation():
    print("\n🔸 Single QR Code Generation 🔸")
    data = get_input("Enter text or URL for QR Code: ")
    fill, back = choose_colors()
    filename = get_filename()
    generate_qr(data, filename, fill, back)

def multiple_qr_generation():
    print("\n🔸 Multiple QR Code Generation 🔸")
    try:
        count = int(get_input("How many QR Codes to generate?: "))
        if count <= 0: raise ValueError
    except ValueError:
        print("❗ Invalid number. Returning to menu.")
        return

    folder = "QR_Codes_" + datetime.now().strftime("%Y%m%d_%H%M%S")
    os.makedirs(folder, exist_ok=True)
    print(f"Saving QR codes in folder: '{folder}'")
    fill, back = choose_colors()

    for i in range(1, count + 1):
        print(f"\n[{i}/{count}]")
        data = get_input(f"Enter data for QR Code #{i}: ")
        filename = os.path.join(folder, f"qrcode_{i}.png")
        generate_qr(data, filename, fill, back)

def main_menu():
    print("📌 QR Code Generator 📌")
    
    print("\n===== MENU =====")
    print("1. Generate a Single QR Code")
    print("2. Generate Multiple QR Codes")
    print("3. Exit")

    choice = get_input("Choose (1/2/3): ")

    if choice == '1':
        single_qr_generation()
    elif choice == '2':
        multiple_qr_generation()
    elif choice == '3':
        print("👋 Goodbye!"); 
    else:
        print("❗ Invalid choice.")

if __name__ == "__main__":
    main_menu()

