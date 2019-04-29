import random

def generate_code(code_len=4):
    
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    count = len(all_chars) - 1

    # print(count)
    code = ''
    for _ in range(code_len):
        random_index = random.randint(0, count)
        code += all_chars[count]
    print(code)
    pass


if __name__ == "__main__":
    generate_code()