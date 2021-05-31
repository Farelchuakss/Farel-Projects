from time import sleep
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern='^.sadboy(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("`Pertama-tama kamu cantik`")
    sleep(2)
    await typew.edit("`Kedua kamu manis`")
    sleep(1)
    await typew.edit("`Dan yang terakhir adalah kamu bukan jodohku`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.punten(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`\n┻┳|―-∩`"
                     "`\n┳┻|     ヽ`"
                     "`\n┻┳|    ● |`"
                     "`\n┳┻|▼) _ノ`"
                     "`\n┻┳|￣  )`"
                     "`\n┳ﾐ(￣ ／`"
                     "`\n┻┳T￣|`"
                     "\n**Permisi Aku mau nimbrung Kk..**")


@register(outgoing=True, pattern='^.geez(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Edo Gay☑️**")
    await typew.edit("**Edo Gay✅**")
    sleep(1)
    await typew.edit("**Panda gak nyari akun☑️**")
    await typew.edit("**Panda gak nyari akun✅**")
    sleep(2)
    await typew.edit("**Anounymous minta help post☑️**")
    await typew.edit("**Anounymous minta help post✅**")
    sleep(2)
    await typew.edit("**TeBoo minta tolong tumbal ressult☑️**")
    await typew.edit("**TeBoo minta tolong tumbal ressult✅**")
    sleep(2)
    await typew.edit("**Yupi gak wibu☑️**")
    await typew.edit("**Yupi gak wibu✅**")
    sleep(2)
    await typew.edit("**Maxy Bacot☑️**")
    await typew.edit("**Maxy Bacot✅**")
    sleep(2)
    await typew.edit("**Ferdi gak giveaway☑️**")
    await typew.edit("**Ferdi gak giveaway✅**")
    sleep(2)
    await typew.edit("**CUMA FAREL YANG BENER!**")
    
# Create by myself @localheart

CMD_HELP.update({
    "ram-ubot":
    "`.ram`\
    \nUsage: alive bot.\
    \n\n`.sadboy`\
    \nUsage: hiks\
    \n\n`.punten` ; `.geez`\
    \nUsage: coba aja & salam."
})
