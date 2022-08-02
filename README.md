# ntroduction

Wouldn’t it be amazing if you could move something, change something, create something just by giving inputs using python programming? This concept can be seen in our daily lives. For example, a keyboard can change values on a screen, a mouse can move something on a screen. From changing a value of an LED to controlling a space shuttle, the possibilities of this simple concept can expand. Examples of this concept include controlling the TV by inputting values via a remote, controlling a rover on Mars by changing several input values from Earth. These may be extreme examples but essentially, the fundamentals of the concept remain the same. Based on this, I created a prototype and I documented it below.

# Overview - Raspberry Pi Potentiometer Blinking LEDs

Using a Raspberry Pi Zero, a Breadboard, one potentiometer, a few LEDs and several cables, I was able to create a program that can read a potentiometer value and light up an LED accordingly. This project is a prototype/first test of my tweeting plant project. 


Below is the diagram of the hardware and wiring.

![image](https://user-images.githubusercontent.com/86998121/180335451-94eadb2d-ddae-4ef9-88b4-1928cedf8fa6.png)

The main concept is that the potentiometer should change values, and to represent a change in the values, LEDs will light up based on the range of the value. For example, if the potentiometer value is less than 0.30, then the first LED should light up. If the value is between 0.30 and 0.60, the second LED should light up. If the value is between 0.60 and 1.00 (max), then the final LED should light up. Below is the drawing of the concept.

![image](https://user-images.githubusercontent.com/86998121/180335553-bbded988-7c42-4311-b423-5550a0461ee4.png)

This project replicates the change in values of a soil moisture sensor, a device that detects whether or not the soil is wet for plants to grow. Since my initial hardware and wiring did not work using the capacitive soil moisture sensor, I created this project as a starting point and will scale it up to using a sensor.
