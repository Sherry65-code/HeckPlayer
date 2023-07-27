build: parser.c easyaudio.h miniaudio.h
	$(CC) -o easyaudio.so parser.c -lm -fPIC -shared
