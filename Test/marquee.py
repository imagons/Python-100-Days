import os
import time

def main():
    content = '爱神的箭回复哈快递费哈快递费'

    while True:
        # 清理屏幕上的输出
        # os.system('cls')
        os.system('clear')
        print(content)

        time.sleep(0.2)
        # 切掉第一个 然后取第一个拼接到最后面
        content = content[1:] + content[0]

if __name__ == '__main__':
    main()