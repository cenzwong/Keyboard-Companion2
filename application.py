import uvicorn

if __name__ == "__main__":
    try:
        print("Listening at port 5002")
        uvicorn.run("main:app", host="0.0.0.0", workers=1, port=5002)
    except SystemExit as e:
        print('Error!', e)
        print('Press enter to exit (and fix the problem)')
    