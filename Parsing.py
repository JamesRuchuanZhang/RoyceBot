import emoji
import demoji

def correct_emojis(temp):
	if "fearful_face" in temp:
		temp = temp.replace("fearful_face", ":fearful:")

	if "cat_face_with_tears_of_joy" in temp:
		temp = temp.replace("cat_face_with_tears_of_joy", ":joy_cat:")

	if "face_with_tears_of_joy" in temp:
		temp = temp.replace("face_with_tears_of_joy", ":joy:")

	if "cold_face" in temp:
		temp = temp.replace("cold_face", ":cold_face:")

	if "weary_face" in temp:
		temp = temp.replace("weary_face", ":weary:")

	if "tired_face" in temp:
		temp = temp.replace("tired_face", ":tired_face:")

	if "grimacing_face" in temp:
		temp = temp.replace("grimacing_face", ":grimacing:")

	if temp == "snake":
		temp = ":snake:"

	if temp == "crab":
		temp = ":crab:"

	return temp

roycePosts = []

with open('osu! UCI - Chat Channels - weeb [371846974862917634].txt', encoding ='utf8') as f:
	lines = f.readlines()

	for x in range(len(lines)):
		if lines[x].rstrip().split('#')[-1] == "1907" and lines[x][0] == '[':
			if lines[x + 1].split(':')[0][0:4] != 'http' and lines[x + 1][0:3] != '```': 
				roycePosts.append(lines[x + 1])

final = open("RoycePostsMaster.txt", "a", encoding = 'utf8')
for line in roycePosts:
	newLine = correct_emojis(emoji.demojize(line, delimiters = ("", "")))
	if newLine != '\n':
		final.write(newLine)
