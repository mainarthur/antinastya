# Settings

api_id = 123848
api_hash = "19c0f67c62804544b35f0645eae6e716"
session_name = "antinastya_session"

daivinchik_id = 1234060895

#--------------


from telethon import TelegramClient, events
import hashlib
from telethon.tl.types import MessageMediaPhoto
from telethon.tl.types import MessageMediaDocument

client = TelegramClient(session_name, api_id, api_hash)

nastya = ["настя", "анастасия", "настюшка", "настюша", "anastasia", "настафанка", "нести", "nasty", "nastiushka", "nasti",  
"nastya", "anastasiюshka", "онастейша", "настейша", "анастаси", "anastasi", "наська", "настюха", "настенька", "аnasтаси",
"настасья", "nasta", "стейша", "anasтасия", "оностосийааа", "настюхэнс", "настэйша", "anastasssii", "anastaseya",
"анастейшн", "настёна", "настена", "nastea", "ятсан", "настюляшинька", "настейшен", "nastazzzis"]

db_file_name = "data.db"

db_file = open(db_file_name, "r+")

checked = db_file.readlines()
checked = [n for n in checked if n != "\n"]

def m(hash):
	if(hash[len(hash)-1] == "\n"):
		return hash[0:len(hash)-1]
	else:
		return hash

checked = list(map(m, checked))
print(checked)

def save():
	global db_file
	db_file.close()
	db_file = open(db_file_name, "w")
	db_file.write("\n".join(checked))


def isFuckingNastya(name):
	name = name.lower()
	for n in nastya:
		if(n in name):
			return True
	return False


def checkFuckingDirtyHole(text):
	comma = text.index(",")
	name = text[0:comma]
	print(f"name = {name}")
	return isFuckingNastya(name)


def isFuckingSlave(event):
	if(event.message != None):
		if(event.message.reply_markup != None):
			if(event.message.reply_markup.rows != None and len(event.message.reply_markup.rows) == 1):
				row = event.message.reply_markup.rows[0]
				if(row.buttons != None and len(row.buttons) == 4):
					buttons = row.buttons
					if(buttons[0] != None and buttons[0].text == "❤️"):
						if(buttons[1] != None and buttons[1].text == "💌"):
							if(buttons[2] != None and buttons[2].text == "👎"):
								if(buttons[3] != None and buttons[3].text == "💤"):
									return True
	return False


def generateMessageHash(message):
	text2hash = message.message
	if(message.media != None):
		if(isinstance(message.media, MessageMediaPhoto)):
			if(message.media.photo.id != None):
				text2hash += str(message.media.photo.id)
		elif(isinstance(message.media, MessageMediaDocument)):
			if(message.media.document.id != None):
				text2hash += str(message.media.document.id)
	
		print(f"text2hash = \"{text2hash}\"")
	
	return hashlib.sha256(text2hash.encode('utf-8')).hexdigest()


@client.on(events.NewMessage(from_users=[daivinchik_id], func=lambda e: isFuckingSlave(e)))
async def kurwa_handler(event):
	try:	
		messageHash = generateMessageHash(event.message)

		print(f"messageHash = {messageHash}")

		if(messageHash in checked):
			time.sleep(1)
			await client.send_message(daivinchik_id,"👎")
			return
		else:
			checked.append(messageHash)
			save()
	except Exception as e:
		print(e)

	if(event.raw_text != None and checkFuckingDirtyHole(event.raw_text)):
		await client.send_message(daivinchik_id,"👎")

	

async def started():
	print("started called")
	me = await client.get_me()
	await client.send_message(me, "AntiNastya started!")


client.start()
client.loop.run_until_complete(started())
client.run_until_disconnected()
