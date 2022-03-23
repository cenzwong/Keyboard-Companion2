if __name__ == "__main__":
    try:
        import uvicorn
        import socket
        print("Listening at port 5002 -> IP Address ", socket.gethostbyname(socket.gethostname()))
        #  socket.gethostbyname_ex(socket.gethostname())[2]
        uvicorn.run("main:app", host="0.0.0.0", workers=1, port=5002)
    except SystemExit as e:
        print('Error!', e)
        print('Press enter to exit (and fix the problem)')
    
