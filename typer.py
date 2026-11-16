import subprocess, time

text = ("Erik the Red, born Erik Thorvaldsson around 950 in Norway, was a Norse "
"explorer. His family was exiled to Iceland after his father was involved in a "
"killing. Erik was later banished from Iceland around 982 for murder, so he sailed "
"west and explored a new land for three years. He returned and named it Greenland, "
"hoping the attractive name would draw settlers. Around 985, he led a fleet of about "
"25 ships, and roughly 14 arrived safely. He founded the Eastern Settlement, "
"becoming its leading chieftain. His son was Leif Erikson, who later reached North "
"America. Erik died around 1003, likely during an epidemic.")

print("Click where you want to type. Starting in 5 seconds...")
time.sleep(5)
for word in text.split(" "):
    w = (word + " ").replace("\\", "\\\\").replace('"', '\\"')
    subprocess.run(["osascript", "-e",
        f'tell application "System Events" to keystroke "{w}"'])
    time.sleep(0.15)
