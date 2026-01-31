# def format_name(f_name, l_name):
#     name = f_name + ' ' + l_name
#     return name.title()
#
# formated_string = format_name('dinda', 'labibe')
# print(formated_string)


# def format_name(f_name, l_name):
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     return f"{formated_f_name} {formated_l_name}"
#
# formated_string = format_name("DinDA", "LABIBA")
#
# print(formated_string)

def function_1(text):
    return text + text

def function_2(text):
    return text.title()

output = function_2(function_1("dinda"))

print(output)