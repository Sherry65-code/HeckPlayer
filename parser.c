#include "easyaudio.h"
#include <stdlib.h>

void eplay(char *filename) {
	FILE* file = fopen(filename, "r");

	if (file == NULL) {
		return;
	}

	fseek(file, 0, SEEK_END);
	long file_size = ftell(file);
	fseek(file, 0, SEEK_SET);

	char* songname = (char*)malloc(file_size+1);

	size_t read_size = fread(songname, 1, file_size, file);

	if (read_size != file_size) {
		perror("Error");
		fclose(file);
		free(songname);
	}

	songname[file_size] = '\0';

	
	play(songname);
	free(songname);
}

void epause() {
	pause();
}

void eresume() {
	resume();
}

void estop() {
	stop();
}
