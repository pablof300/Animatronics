# Orangutan Animatronics


This project was created as an animatronic competition project for the **2018 Technology Student Association Florida State conference**. This competition tasked a group of engineers to *"create an interactive animatronic robot for a local Zoo or aquarium"*. We created Dylan: **an interactive RFID-capable hydraulic powered orangutan** that raises awareness about his specie and its environment through speech.

#### Meet him:
![alt text](https://github.com/pablof300/Orangutan-Animatronic/blob/master/images/image_one.png?raw=true)

# Features

  - Compact 15" deep x 3' wide x 4' high wooden box
  - Steel frame for the orangutan
  - Movable arms and mouth (using servo motors)
  - Retractable gate (powered through hydraulic pump)
  - Six RFID tags and RFID sensor
  - Decorative LED lights
  - Informs users of four different facts about orangutans
  - Functionality of speech in both English and Spanish
  - Second place winner at a state animatronics competition
 
![alt text](https://github.com/pablof300/Orangutan-Animatronic/blob/master/gifs/gif_one.gif?raw=true)

# How it works?

Like any other multidiciplinary endeavor, especially in engineering, we had a mechanical, software, and artistic effort. Our team was composed of four people, and each one of us had a different part in the project, so before describing the process of building Dylan (our orangutan), I will introduce the team.

##### The Team

- Pablo Estrada (software)
- Nick Garcia (mechanical)
- Sofia Garcia (artistic)
- Alessandra (artistic)

![alt text](https://github.com/pablof300/Orangutan-Animatronic/blob/master/images/image_two.jpg?raw=true)

##### Artistic

An orangutan without eyes and only a steel frame is horryfing. Sofia and Alessandra used yarn, decorative vegetation, and paint to design the skin of the orangutan (which is removable for convenience) and the eyes.

![alt text](https://github.com/pablof300/Orangutan-Animatronic/blob/master/images/image_five.jpg?raw=true)

###### Mechanical

This side of the project proved to be the most challening. Nick welded together a steel frame for the orangutan. This frame was designed to allow the servo motors to be mounted and through the use of springs move all the extremities. The mouth continously moved when the servo was turned on using a crank.

![alt text](https://github.com/pablof300/Orangutan-Animatronic/blob/master/images/image_three.jpg?raw=true)

He assembled the wooden box to hold everything together, and he reused a Ford Mustang hydraulic pump motor and two pistons for the retractable gate. 

![alt text](https://github.com/pablof300/Orangutan-Animatronic/blob/master/images/image_four.jpg?raw=true)

##### Software

Before I get into the software that powers Dylan (the orangutan), I will describe some of the electronics involved. With Nick, we wired the RFID sensor and the LED lights to a breadboard. We tried our best to color code the wires, but it was very messy at the end of the day.

![alt text](https://github.com/pablof300/Orangutan-Animatronic/blob/master/images/image_six.jpg?raw=true)

Some of the black thicker cables seen in the picture are for the power supply and the speaker charger. We used a Logitech speaker set that connected to the Raspbery Pi using an aux cable. Both pistons and LED lights were controlled by using Relay switches connected to the Raspberry Pi. There is an HDMI cable in the picture, but it was only for the convenience of debugging during the development pahse.

![alt text](https://github.com/pablof300/Orangutan-Animatronic/blob/master/images/image_seven.jpg?raw=true)

We use the [SimpleMFRC522](https://github.com/pablof300/Orangutan-Animatronic/blob/master/source-code/SimpleMFRC522.py) class written by Simon Monk to interface with the RFID sensor (RFID RC522). To use this class, you must have installed the SPI-Py library. Before doing any of this, you must have Python installed.
```
$ git clone https://github.com/lthiery/SPI-Py.git
$ sudo python setup.py install
```
You can ge the SimpleMFRC522 class here:
```
git clone https://github.com/pimylifeup/MFRC522-python.git
```

All of our code was run using a Raspberry Pi Model B using the OS Raspbian. I wrote all of our source code in the [animatronics.py](https://github.com/pablof300/Orangutan-Animatronic/blob/master/source-code/animatronics.py) file. Within our source folder, you will also find several mp3 files that contain the facts the speaker plays when prompted by an RFID tag.

# License

MIT License

Copyright (c) 2018 Pablo Estrada

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
