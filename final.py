# -*- coding: utf8 -*
# 1번 좋은 느낌 중형 2번 화이트 대형 3번 시크릿데이 대형

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.IN)  #switch
GPIO.setup(23,GPIO.OUT) #buzz
scale=[262,294,329,349,392,440,493,523]

p=GPIO.PWM(23,100)
p.start(100)
p.ChangeDutyCycle(90)


def detect_text(path):
    """Detects text in the file."""
    from google.cloud import vision
    from google.cloud.vision import types
    import io
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print('Texts:')

    for text in texts:
        print('\n"{}"'.format(text.description))

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))

count=0
p.ChangeFrequency(scale[2])
time.sleep(0.1)

#스위치를 눌러서 어느 제품을 찾을 것인지 설정
for i in range (0,20):
    print(i)
    if GPIO.input(18) is 1:
        count=count+1
        print("input was high")
    time.sleep(0.18)

print(count)
p.stop()

if count==1:
    textlist=['좋은','느낌','중형']
elif count==2:
    textlist=['화이트','대형']
elif count==3:
    textlist=['시크릿데이','대형']
else:
    textlist=[]

if


GPIO.cleanup()