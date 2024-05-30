import random
import string
import datetime

url_text = 'File_Text/History_CreatePassword.txt'

def History_password(new_pass):
    date_pass = datetime.datetime.now()
    format_date = date_pass.strftime("%d/%m/%Y")
    try:
        with open(url_text, 'a') as hs_file:
            hs_file.write("[{}]: {}\n".format(format_date, new_pass))
    except FileNotFoundError:
        print("Không thể tìm thấy file 'History_CreatePassword.txt'.")
    except IOError:
        print("Có lỗi trong khi thêm password vào file.")
    except Exception as e:
        print("Lỗi: ", e)

def generate_password(length, include_uppercase=True, include_lowercase=True, include_digits=True, include_special_char=True):
    characters = ''
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_digits:
        characters += string.digits
    if include_special_char:
        characters += string.punctuation

    if len(characters) == 0:
        print("Không có ký tự nào được chọn. Vui lòng nhập (y/n).")
        return None
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def is_valid_length(input_str):
    return input_str.isdigit()

def get_user_choice():
    print("Vui lòng chọn kiểu mật khẩu:\n[1]: Full lựa chọn.\n[2]: Tự thiết lập.")
    return input(">> ")

def Manager():
    password_length_input = input("Vui lòng nhập độ dài của mật khẩu: ")
    while not is_valid_length(password_length_input) or int(password_length_input) <= 0:
        print("Độ dài mật khẩu phải là một số nguyên dương lớn hơn 0.")
        password_length_input = input("Vui lòng nhập lại độ dài của mật khẩu: ")

    password_length = int(password_length_input)
        
    choice = get_user_choice()
    while choice not in ['1', '2']:
        print("Lựa chọn không hợp lệ.")
        choice = get_user_choice()

    if choice == '1':
        new_password = generate_password(password_length)
    else:
        print("VUI LÒNG NHẬP 'y' HOẶC 'n'")
        upper = input("Bao gồm chữ cái Hoa? (y/n): ").lower() == 'y'
        lower = input("Bao gồm chữ cái Thường? (y/n): ").lower() == 'y'
        digits = input("Bao gồm số? (y/n): ").lower() == 'y'
        special = input("Bao gồm ký tự đặc biệt? (y/n): ").lower() == 'y'
        new_password = generate_password(password_length, include_uppercase=upper, include_lowercase=lower, include_digits=digits, include_special_char=special)

    if new_password:
        print("Mật khẩu được tạo là:", new_password)
        History_password(new_password)
    else:
        print("Không thể tạo mật khẩu!")

Manager()
