import re 

def validate_name(name):
    if not re.fullmatch(r"[A-Za-z ]+", name):
        return "Nama lengkap hanya boleh berisi huruf dan spasi."
    return None

def validate_phone(phone):
    if not phone.isdigit():
        return "Nomor telepon hanya boleh berisi angka."
    return None

def validate_email(email):
    if "@" not in email or "." not in email:
        return "Email harus mengandung karakter '@' dan '.'."
    return None

def main():
    print("Silakan masukkan data pendaftaran:")
    name = input("Nama lengkap: ").strip()
    phone = input("Nomor telepon: ").strip()
    email = input("Email: ").strip()

    errors = []

    name_error = validate_name(name)
    if name_error:
        errors.append(name_error)

    phone_error = validate_phone(phone)
    if phone_error:
        errors.append(phone_error)

    email_error = validate_email(email)
    if email_error:
        errors.append(email_error)

    if errors: 
        print("Terjadi kesalahan dalam input:")
        for error in errors:
            print(f"- {error}")
    else: 
        print("Data pendaftaran valid.")

if __name__ == "__main__":
    main()
