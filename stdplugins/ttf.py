from uniborg.util import admin_cmd


@borg.on(admin_cmd(pattern="ttf ?(.*)")) # pylint:disable=E0602
async def get(event):
    name = event.text[5:] + ".txt"
    m = await event.get_reply_message()
    with open(name, "w") as f:
        f.write(m.text)
    await event.delete()
    await borg.send_file(event.chat_id,name,force_document=True)