# Copas Teriak Copas MONYET
# Gay Teriak Gay Anjeng
# @Rizzvbss | @Kenapanan
# Kok Bacot
# © @KynanSupport
# FULL MONGO NIH JING FIX MULTI CLIENT


from asyncio import sleep
from contextlib import suppress
from random import randint
from typing import Optional


from pyrogram import Client, enums, filters
from pyrogram.raw.functions.channels import GetFullChannel
from pyrogram.raw.functions.messages import GetFullChat
from pyrogram.raw.functions.phone import CreateGroupCall, DiscardGroupCall
from pyrogram.raw.types import InputGroupCall, InputPeerChannel, InputPeerChat
from pyrogram.types import Message
from PyroUbot import *
from PyroUbot.utils import *



daftar_join = []

turun_dewek = False


__MODULE__ = "VoiceChat"
__HELP__ = """
Bantuan Untuk Voice Chat

• Perintah: <code>{0}startvc</code>
• Penjelasan: Untuk memulai voice chat grup.

• Perintah: <code>{0}stopvc</code>
• Penjelasan: Untuk mengakhiri voice chat grup.

• Perintah: <code>{0}leavevc</code>
• Penjelasan: Untuk meninggalkan voice chat grup.

• Perintah: <code>{0}joinvc</code>
• Penjelasan: Untuk bergabung voice chat grup.
"""


async def get_group_call(
    client: Client, message: Message, err_msg: str = ""
) -> Optional[InputGroupCall]:
    chat_peer = await client.resolve_peer(message.chat.id)
    if isinstance(chat_peer, (InputPeerChannel, InputPeerChat)):
        if isinstance(chat_peer, InputPeerChannel):
            full_chat = (await client.invoke(GetFullChannel(channel=chat_peer))).full_chat
        elif isinstance(chat_peer, InputPeerChat):
            full_chat = (
                await client.invoke(GetFullChat(chat_id=chat_peer.chat_id))
            ).full_chat
        if full_chat is not None:
            return full_chat.call
    await message.reply(f"**No group call Found** {err_msg}")
    return False


    
@PY.UBOT("naik|joinvc", sudo=True)
async def joinvc(client, message):
    if message.from_user.id not in KYNAN:
        return await message.reply("**GRATISAN GAUSAH BANYAK TINGKAH BANH !!**")
    if message.from_user.id != client.me.id:
        ky = await message.reply("<code>Processing....</code>")
    else:
        ky = await message.reply("<code>Processing....</code>")
    chat_id = message.command[1] if len(message.command) > 1 else message.chat.id
    with suppress(ValueError):
        chat_id = int(chat_id)
    naek = await client.vc.start(chat_id)
    if naek:
        await ky.edit("**Akun anda sudah berada diatas !!**")
    else:
        try:
            await client.vc.start(chat_id)
        except Exception as e:
            return await ky.edit(f"ERROR: {e}")
        await ky.edit(
        f"• <b>Berhasil Join Voice Chat</b>\n<b>Chat :</b> <code>{message.chat.title}</code>"
    )
        await sleep(1)
        await client.vc.set_is_mute(True)



@PY.UBOT("turun|leavevc", sudo=True)
async def leavevc(client, message):
    global turun_dewek
    if message.from_user.id != client.me.id:
        ky = await message.reply("<code>Processing....</code>")
    else:
        ky = await message.reply("<code>Processing....</code>")
    chat_id = message.command[1] if len(message.command) > 1 else message.chat.id
    with suppress(ValueError):
        chat_id = int(chat_id)
    turun = await client.vc.stop()
    if turun:
        await ky.edit("**Anda sedang tidak berada di dalam obrolan suara manapun.**")
    else:
        try:
            await client.vc.stop()
        except Exception as e:
            return await ky.edit(f"<b>ERROR:</b> {e}")
        msg = "• <b>Berhasil Meninggalkan Voice Chat</b>\n"
        if chat_id:
            msg += f"<b>Chat : </b><code>{message.chat.title}</code>"
        await ky.edit(msg)
        await sleep(1)