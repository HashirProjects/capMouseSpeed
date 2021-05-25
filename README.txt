Does what it says on the tin.

The issue with the cursor stuttering can be fixed by rasing the sample rate, 
but doing so means the cursor moves more during calculations than when the speed is being sampled.
I tried using another thread but this meant that the correction the computer does is also counted in the speed and the program doesnt work.