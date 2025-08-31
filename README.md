# LightScribe Simulator

This python script simulates burning a label onto a LightScribe disc, to prove my theory that a rotation-tracking sensor was completely unnecessary, and in theory any off-the-shelf drive could've done the job

<br>

## Why?

It started when I was watching a [video by Technology Connections about these discs](https://www.youtube.com/watch?v=40hJStzsBm8)

If you want to know what LightScribe is, I recommend watching that video

But to quickly summarize, it's a way of creating custom labels for blank discs by inserting it in the drive upside down and instead of burning data, the laser will burn an image

<br>

At the ```2:11``` mark of the video he says:

*"This little doodad allows the drive to see the rotational position of the disc"*

At ```3:25``` he says:

*"Now the drive can know the disc's absolute rotational position so it creates a proper image, and not a spirally mess"*

<br>

What made me think it's unnecessary is what he says right after the first quote:

*"Moulded into the plastic of the disc is a spiral pre-groove containing the ATIP... ...this not only guides the laser as it writes data to a blank disc, but it also keeps the disc spinning at the correct speed relative to the data being blasted onto it by the writing laser"*

<br>

So if the disc spins at a constant rate, then why did it need a tracking sensor? The angle of the disc can be figured out based on how much time has passed

```angle = rotationsPerSecond * seconds```

This is what my simulator is here to prove, that a stable image can be burned onto the disc without directly knowing its rotation

<br>

## Possible reasons this wouldn't have worked in reality
I imagine the engineers at HP would've thought of this so maybe there's some critical flaw in my logic here, it'd be cool to actually test this out in a real scenario but I don't have a LightScribe drive or any of the discs

- Maybe computers weren't fast enough back then to calculate the angle in real-time (although given how slowly the disc had to spin I have a hard time believing that)
- Maybe the ATIP was not visible when the disc was upside-down, and it wouldn't keep a constant speed
- If the ATIP was visible, maybe it wasn't perfect at maintaining speed

<br>

## Using the script
You'll need PyGame to run the script, instructions for installing it can be found [here](https://www.pygame.org/wiki/GettingStarted)

Replace ```lightscribe.png``` with your own 512x512 image that you want 'burned' onto the 'disc'. Unlike real LightScribe my simulator supports full-colour images

Settings can be tweaked in the script, I've added descriptions to each variable to describe what it does

<br>

### Getting a complete image
Getting a full image while being able to see the burning process takes almost as long as burning a real disc, as the speed of the disc (and thus how quickly the image is burned onto it) needs to match the speed the code runs

*You'll have to edit the code a bit if you don't care about seeing the burning happen in real-time and just want it done as quickly as possible, I left instructions for that in the script itself*

If you end up with spread out dots instead of an image, you need to lower the ```rotationsPerSecond```

rotationsPerSecond = 5000
<img width="1277" height="747" alt="Screenshot 2025-08-30 210435" src="https://github.com/user-attachments/assets/8f5aa862-8fe5-4729-ad3a-5de8f6c6e02d" />


rotationsPerSecond = 1500
<img width="1277" height="748" alt="Screenshot 2025-08-30 210255" src="https://github.com/user-attachments/assets/9110c8c2-3d57-46e4-a6eb-065278de05b3" />

rotationsPerSecond = 20
<img width="1277" height="747" alt="Screenshot 2025-08-30 210228" src="https://github.com/user-attachments/assets/e1c164f3-68fe-4300-a829-499081c3ef51" />

