# Face Detection by Phantom 4 Pro + Aircraft in Real Time

This is a project created for Basics of Artificial Vision and Biometrics course in University of Salerno, Master's Degree in Information 
Security.

The aim of the present project is to study and explain the features of the Phantom 4 Pro + aircraft and analyze its operating methods in 
order to identify human faces during live streaming of videos. For this purpose, it will be used Paul Viola and Michael Jones' face 
detection algorithm, which includes Haar features and cascade classifiers to identify faces, eyes and ears of an individual.

What we produced at the end of these studies was a real system architecture (see figure).

![Alt Text](http://thenewrevival.altervista.org/images/architettura.png)

## How to use

The aim of the present project became to realize a new architecture that could help us to distinguish faces and its features, especially eyes and ears, while
filming a live streaming by the above-mentioned aircraft.
The created system needs some important steps to be executed correctly: first of all, a server (in our cases nginx) has to be started. Then, you obviously
need a live video recorded by Phantom 4 Pro+, whose capabilities of the camera are one of its best and most underrated features. The sensor is good, but the
video capture speeds it can reach are better. The next stage consists in associating the drone with the nginx server: in order to do it, make sure both Phantom 4 Pro+ and the computer are connected to the same network; so, find out the IP address of the device working as the server and put it
as the URL network required to reproduce live streaming using RTMP protocol in the "Choose platform" configuration of the drone. At this point, both the devices are connected and the stream of the detection can begin: if it works, you
would see rectangles and circles of different colours surrounding faces, eyes and ears of the framed people.


