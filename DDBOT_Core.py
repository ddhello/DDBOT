import os

import telepot
import configparser
import time
from telepot.loop import MessageLoop
config_cfg = "./config.cfg"
config_raw = configparser.RawConfigParser()
config_raw.read(config_cfg)
debug = config_raw.get("Defaults","debug_mode")
bot = telepot.Bot('1182335639:AAFxjOdmageqWMRyZvev3IGwCjXXws-Fjcc')
print("The bot was loaded compeletly.")
def handle(msg):
    debug = config_raw.get("Defaults", "debug_mode")
    print('recevied a message!')
    content_type,chat_type,chat_id = telepot.glance(msg)
    if debug == "True":
        print(msg)
        return
    text = msg['text']
    if text == "!debug":
        if debug == "False":
            if msg['chat']['username'] == "ddhello":
                bot.sendMessage(chat_id,"调试模式已开启")
                print(debug)
                config_raw.set("Defaults","debug_mode","True")
            else:
                bot.sendMessage(chat_id,"无权限开启调试模式")
        else:
            config_raw.set("Defaults","debug_mode","False")
            bot.sendMessage(chat_id,"调试模式已关闭")
            print(debug)
            return
        try:
            with open("./config.cfg", "w+") as f:
                config_raw.write(f)
        except ImportError:
            pass

    if chat_type == "private":
        if text.find("/web_restart") != -1:        #重启网页服务器
            if msg['chat']['username'] == "ddhello":
                bot.sendMessage(chat_id,"好的喵")
                result = os.popen('lnmp restart')
                res = result.read()
                for line in res.splitlines():
                    bot.sendMessage(line)
        else:
                bot.sendMessage(chat_id,"访问被拒绝:权限不足")
        if text.find("/start") != -1:
            bot.sendMessage(chat_id,"欢迎访问肉便器系统V1.0\n正在载入系统....\n载入系统完毕！您的肉便器已经安装程序完毕了哦。哦对了 她是一个机器人，无论怎么调教也不会出事的哦，如果实在电子元件出现问题的话，可以联系@ddhello进行免费维修哦！\n那么，我就这样将她的电源按钮启动了哦！\n祝您使用愉快！")
            bot.sendMessage(chat_id,"您好！咱..咱的名字叫做DDBOT，之后我会尽心全力地服务您的！如果不知道咱能干什么....输入/help就可以查看咱的所有玩法了。\n那个，咱以后会全心全意地当您的肉便器的哦！")
        if text.find("/help") != -1:
            bot.sendMessage(chat_id,"那个那个，咱这就把人家自己所有的秘密全部告诉你了哦！\n/set_capthca   这样可以要求人家在门口守门啦")
MessageLoop(bot,handle).run_as_thread()
while 1:
    time.sleep(10)
