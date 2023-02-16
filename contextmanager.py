# Here we simply create 
with open('notes.txt', 'w') as file:
    user_text = input("What would you like to write? ")
    file.write(user_text)


file = open('notes.txt', 'w')
try:
    file.write('something else too...')
finally: 
    file.close()
# finally will execute with or without an exception vs try that is dependent

# example of using a lock (multi-threading)
from threading import Lock
lock = Lock()

lock.acquire()
#...We can do something safely - it is thread safe...#
#...And then we always have to call lock.release...#
lock.release()




