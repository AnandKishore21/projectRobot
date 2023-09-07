import socket

HOST = '10.3.141.1' # Server IP or Hostname
PORT = 12345 # Pick an open Port (1000+ recommended), must match the client sport
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ("Socket created")

#managing error exception
try:
	s.bind((HOST, PORT))
except socket.error:
	print ("Bind failed")

s.listen(5)
print ("Socket awaiting messages")
conn, addr = s.accept()
print ("Connected")

# awaiting for message
while True:
	data = conn.recv(1024)
	print ("I sent a message back in response to: ")
	#reply = ''

	# process your message
	if len(data)== 5:
		print ("Congratulations Data recieved")#reply = 'Hi, back!'
	elif data == 'This is important':
		reply = 'OK, I have done the important thing you have asked me!'

	#and so on and on until...
	elif data == 'quit':
		conn.send('Terminating')
		break
	else:
		print ("fail")#reply = 'Unknown command'

	# Sending reply
	#conn.send(reply)
	conn.close() # Close connections