from time import time

entries = {}
before_pause = True
pause_time = 0
paused = False

run = True
print('Commands AFTER the recording has started:')
print('Type "pause" when the recording is paused')
print('Type "unpause" when the recording continues')
print('Type "done" when the recording ends to stop the script and get your results\n')

start = input('Press enter here when the recording starts: ')
beginning = time()
while run:
    typed = input("Add timestamp: ")
    if not paused:
        if typed.lower() == 'pause':
            pause_time = time()
            paused = True
        
        elif typed.lower() == 'done':
            run = False
        else:
            stamp = time() - beginning - pause_time - 2  # 2 seconds subtracted to account for typing time
            minutes, seconds = divmod(stamp, 60)
            hours, minutes = divmod(minutes, 60)
            timestamp = "%02d:%02d"%(minutes,seconds) if stamp < 3600 else "%02d:%02d:%02d"%(hours,minutes,seconds)
            if not paused:
                entries[typed] = timestamp  
    elif paused and typed.lower() == 'unpause':
            pause_time = time() - pause_time
            paused = False

output = ''.join([f'{key} - {value} | ' for key, value in entries.items()])
print(output)
with open('output.txt', 'w') as file:
    file.write(output)
input(">:")  # avoid immediately closing the terminal window to see the results. 
