def format_name(first_name, last_name):
    if first_name == "" or last_name == "":
        return "Anda belum menginput"
    formated_f_name = first_name.title()
    formated_l_name = last_name.title()
    return f"Result: {formated_f_name} {formated_l_name}"

print(format_name(input("Masukkan nama depan anda : "), input("Masukkan nama belakang anda : ")))