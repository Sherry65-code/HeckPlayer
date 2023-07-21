#define MINIAUDIO_IMPLEMENTATION
#include "miniaudio.h"
#include <unistd.h>
    

// initializing parameters
int fileExists(const char* filename);
ma_result result;
ma_engine engine;
ma_uint64 currentPosition;

// Checking if the file exisits or not
int fileExists(const char* filename) {
    if (access(filename, F_OK) != -1) {
        // File exists
        return 1;
    } else {
        // File does not exist
        return 0;
    }
}

int play(const char *filename) {

	result = ma_engine_init(NULL, &engine);
    if (result != MA_SUCCESS) {
        return -2;
    }
	if (fileExists(filename) == 2) {
		return -1;
	}
    ma_engine_play_sound(&engine, filename, NULL);
	return 0;
}

int stop() {
    ma_engine_uninit(&engine);
	return 0;
}

int pause() {
    // Get the current sound file position in PCM frames
    currentPosition = ma_engine_get_time_in_pcm_frames(&engine);

    // Stop the engine
    ma_engine_stop(&engine);

    return 0;
}

int resume() {
    // Seek to the current sound file position
    ma_engine_set_time_in_pcm_frames(&engine, currentPosition);

    // Resume playback
    ma_engine_start(&engine);

    return 0;
}

