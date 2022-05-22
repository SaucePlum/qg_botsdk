# !/usr/bin/env python3
# encoding: utf-8
# 使用创建表情表态API的一个简单实例
from qg_botsdk.qg_bot import BOT
from qg_botsdk.model import Model
from random import choice

some_emojis = ['4', '5', '8', '9', '10', '12', '14', '16', '21', '23', '24', '25', '26', '27', '28', '29', '30']


def deliver(data: Model.MESSAGE):
    if '来个表态' in data.treated_msg:
        chosen_emoji = choice(some_emojis)
        bot.create_reaction(data.channel_id, data.id, '1', chosen_emoji)
        gru = bot.get_reaction_users(data.channel_id, data.id, '1', chosen_emoji)
        if all(gru.result):
            info = f'该消息使用QQ系统表情（id={chosen_emoji}）的全部表态用户：'
            for items in gru.data:
                info += f' {items.username}'
            bot.logger.info(info)
        else:
            warn = f'获取表情表态用户列表错误，code ='
            for items in gru.data:
                if 'code' in items.__dict__.keys():
                    warn += f' {items.code}'
            bot.logger.warning(warn)


if __name__ == '__main__':
    bot = BOT(bot_id='', bot_token='', is_private=True, is_sandbox=True, max_shard=1)
    bot.bind_msg(deliver, treated_data=True)
    bot.start()
