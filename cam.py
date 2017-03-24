#!/usr/bin/env python
from bottle import route, run, static_file
import json
import time
import os

config_file = open( 'config.json' )
environment = json.load( config_file )

cameras = environment['cameras']
relays = environment['relays']
bools = environment['bools']

#print 'Cameras: ' + str(cameras)
#print 'Relays: ' + str(relays)
#print 'Bools: ' + str(bools)

@route('/cameras')
def cameras_list():
    return str(cameras)

@route('/cameras/<cameraid>', method='GET')
def cameras_show( cameraid ):
    return str(cameras[int(cameraid)])


@route('/relays')
def relays_list():
    return str(relays)

@route('/relays/<relayid>', method='GET')
def relays_show( relayid ):
    return str(relays[int(relayid)])

@route('/relays/<relayid>/<value>', method='POST')
def relays_set( relayid, value ):
    relays[int(relayid)]['status']=value
    return str(relays[int(relayid)])


@route('/bools')
def bools_list():
    return str(bools)

@route('/bools/<boolid>', method='GET')
def bools_show( boolid ):
    return str(bools[int(boolid)])

#@route('/static/<filename>')
#def server_static(filename):
#    return static_file(filename, root='/home/zygmuad2/PycharmProjects/supernova')


@route('/cam/get/camera3.jpg', method='GET')
def cam1_get():
#    img = cam.get_image()
#    pygame.image.save(img,"/tmp/camera3-tmp.jpg")
#    os.system("convert -quality 40 /tmp/camera3-tmp.jpg /tmp/camera3.jpg ")
    return static_file('camera3.jpg', root='/tmp')



#os.chdir('/opt/fusion')
#pygame.camera.init()
#cam = pygame.camera.Camera("/dev/video0",(640,480))
#cam.start()


run(host='0.0.0.0', port=8081) 
