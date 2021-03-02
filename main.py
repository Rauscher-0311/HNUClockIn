import argparse
import time
import random

from vcode_img import vcode_img
from vocr import vocr
from read_inform import read_inform
from hnu_clockin import hnu_clockin

def main(args):
    AT_HOME = args.at_home
    LOGIN_MAX_TRY = args.login_max_try
    CLOCKIN_MAX_TRY = args.clockin_max_try

    inform = read_inform()
    v_i = vcode_img()
    clockin = hnu_clockin(inform, AT_HOME)

    login_count = 0
    while True:
        print("开始获取验证码...")

        token = v_i.get_token()

        time.sleep(random.random())

        try:
            img = v_i.get_img_byte(token)
            vcode = vocr(inform).vcode(img)
            clockin.load_vcode(token, vcode)
        except Exception:
            print("获取验证码失败")
            continue

        print("获取验证码成功")

        print("正在登陆...")

        time.sleep(random.randint(1, 5) + random.random())
        if clockin.login():
            break
        else:
            login_count += 1
            print("登陆第{}次尝试失败...\n".format(login_count))

        if login_count > LOGIN_MAX_TRY:
            break

    if login_count <= LOGIN_MAX_TRY:
        print("登陆成功")

        try_count = 0

        while not clockin.is_clockin():
            try_count += 1
            print("今日未打卡，开始打卡......第{}次尝试".format(try_count))

            time.sleep(random.randint(1,10) + random.random())

            if clockin.clockin():
                print("自动打卡成功")
                break

            if try_count > CLOCKIN_MAX_TRY:
                print("自动打卡失败")
                break

        if try_count <= CLOCKIN_MAX_TRY:
            print("今日已打卡")

    else:
        print("HNU的土豆服务器又炸了:)")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='HNU Clock In')
    parser.add_argument('--at_home', default=1, type=int, help='1 is at home and otherwise 0')
    parser.add_argument('--login_max_try', default=5, type=int, help='the max try times of login')
    parser.add_argument('--clockin_max_try', default=0, type=int, help='the max try times of clockin')

    args = parser.parse_args()

    main(args)